import os, re, time, inspect
import psutil, requests
from process_tests import dump_on_error, setup_coverage, TestProcess, TestSocket, wait_for_strings
import django

TIMEOUT = int(os.getenv('UWSGICACHE_TEST_TIMEOUT', 3))


def assertions(url):
    assert requests.get(url + '/get/1').text == 'None'
    assert requests.get(url + '/set/1/a').text == 'ok'
    assert requests.get(url + '/get/1').text == 'a'
    assert requests.get(url + '/clear').text == 'ok'
    assert requests.get(url + '/get/1').text == 'None'
    assert requests.get(url + '/set/2/b?timeout=3').text == 'ok'
    time.sleep(2) # 2 * cache-expire-freq
    assert requests.get(url + '/get/2').text == 'b'
    time.sleep(3) # 1 + 2 * cache-expire-freq
    assert requests.get(url + '/get/2').text == 'None'
    assert requests.get(url + '/set/3/c?timeout=0').text == 'ok'
    time.sleep(2) # 2 * cache-expire-freq
    assert requests.get(url + '/get/3').text == 'None'
    assert requests.get(url + '/set/4/d?timeout=None').text == 'ok'
    time.sleep(2) # 2 * cache-expire-freq
    assert requests.get(url + '/get/4').text == 'd'
    # skipping this test for Django 1.6 in test_locmem (Django 1.6 issue?)
    if django.VERSION[:2] == (1, 6) and inspect.stack()[1][3] != 'test_locmem':
        assert requests.get(url + '/add/4/e').text == 'False'
    assert requests.get(url + '/add/5/e').text == 'True'
    assert requests.get(url + '/get/5').text == 'e'
    assert requests.get(url + '/add/6/f?timeout=3').text == 'True'
    time.sleep(2) # 2 * cache-expire-freq
    assert requests.get(url + '/get/6').text == 'f'
    time.sleep(3) # 1 + 2 * cache-expire-freq
    assert requests.get(url + '/get/6').text == 'None'
    assert requests.get(url + '/add/7/g?timeout=0').text == 'True'
    time.sleep(2) # 2 * cache-expire-freq
    assert requests.get(url + '/get/7').text == 'None'
    assert requests.get(url + '/add/8/h?timeout=None').text == 'True'
    time.sleep(2) # 2 * cache-expire-freq
    assert requests.get(url + '/get/8').text == 'h'


def test_uwsgi():
    with TestProcess('uwsgi',
                     '--http-socket', '127.0.0.1:0',
                     '--module', 'test_project.wsgi',
                     '--master',
                     '--cache-expire-freq', '1',
                     '--cache2', 'name=foobar,items=20') as proc:
        with dump_on_error(proc.read):
            wait_for_strings(proc.read, TIMEOUT, 'bound to TCP address 127.0.0.1')
            url, = re.findall(r"bound to TCP address (127.0.0.1:\d+) ", proc.read())
            url = "http://" + url
            assertions(url)


def get_ports(pid):
    def get(proc):
        return sum(
            (get(p) for p in proc.children()),
            [c.laddr[1] for c in proc.connections() if c.status == 'LISTEN' and c.raddr == ()]
        )
    process = psutil.Process(pid)
    for _ in range(50):
        sockets = get(process)
        if sockets:
            return sockets[0]
        time.sleep(0.05)

def test_locmem():
    with TestProcess('django-admin.py',
                     'runserver', '127.0.0.1:0', '--traceback', '--noreload', '--nothreading',
                     env=dict(os.environ, UWSGI_CACHE_FALLBACK='y')) as proc:
        with dump_on_error(proc.read):
            wait_for_strings(proc.read, TIMEOUT, '127.0.0.1')
            port = get_ports(proc.proc.pid)
            url = "http://127.0.0.1:%s" % port
            assertions(url)
