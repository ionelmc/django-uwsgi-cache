import os
import re
import time

import psutil
import requests
from process_tests import dump_on_error
from process_tests import setup_coverage
from process_tests import TestProcess
from process_tests import TestSocket
from process_tests import wait_for_strings

TIMEOUT = int(os.getenv('UWSGICACHE_TEST_TIMEOUT', 3))


def assertions(url):
    assert requests.get(url + '/set/1/a').text == 'ok'
    assert requests.get(url + '/get/1').text == 'a'
    assert requests.get(url + '/clear').text == 'ok'
    assert requests.get(url + '/get/1').text == 'None'
    assert requests.get(url + '/set/2/b?timeout=1').text == 'ok'
    time.sleep(0.5)
    assert requests.get(url + '/get/2').text == 'b'
    time.sleep(0.5)
    assert requests.get(url + '/get/2').text == 'None'
    assert requests.get(url + '/set/3/c?timeout=0').text == 'ok'
    assert requests.get(url + '/get/3').text == 'None'
    assert requests.get(url + '/set/4/d?timeout=None').text == 'ok'
    assert requests.get(url + '/get/4').text == 'd'


def test_uwsgi():
    with TestProcess('uwsgi',
                     '--http-socket', '127.0.0.1:0',
                     '--module', 'test_project.wsgi',
                     '--cache2', 'name=foobar,items=10') as proc:
        with dump_on_error(proc.read):
            wait_for_strings(proc.read, TIMEOUT, 'bound to TCP address 127.0.0.1')
            url, = re.findall(r"bound to TCP address (127.0.0.1:\d+) ", proc.read())
            url = "http://" + url
            #assertions(url)
            assert requests.get(url + '/set/1/a').text == 'ok'
            assert requests.get(url + '/get/1').text == 'a'
            assert requests.get(url + '/clear').text == 'ok'
            assert requests.get(url + '/get/1').text == 'None'


def get_ports(pid):
    def get(proc):
        return sum(
            (get(p) for p in proc.children()),
            [c.laddr[1] for c in proc.connections() if c.status == 'LISTEN' and c.raddr == ()]
        )
    return get(psutil.Process(pid))[0]


def test_locmem():
    with TestProcess('django-admin.py',
                     'runserver', '127.0.0.1:0', '--traceback', '--noreload', '--nothreading',
                     env=dict(os.environ, UWSGI_CACHE_FALLBACK='y')) as proc:
        with dump_on_error(proc.read):
            wait_for_strings(proc.read, TIMEOUT, '127.0.0.1')
            port = get_ports(proc.proc.pid)
            url = "http://127.0.0.1:%s" % port
            assertions(url)
