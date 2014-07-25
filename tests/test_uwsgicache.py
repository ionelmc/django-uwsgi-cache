import os
import re

import psutil
import requests
from process_tests import dump_on_error
from process_tests import setup_coverage
from process_tests import TestProcess
from process_tests import TestSocket
from process_tests import wait_for_strings

TIMEOUT = int(os.getenv('UWSGICACHE_TEST_TIMEOUT', 10))


def test_uwsgi():
    with TestProcess('uwsgi',
                     '--http-socket', '127.0.0.1:0',
                     '--module', 'test_project.wsgi',
                     '--cache2', 'name=foobar,items=10') as proc:
        with dump_on_error(proc.read):
            wait_for_strings(proc.read, TIMEOUT, 'bound to TCP address 127.0.0.1')
            url, = re.findall(r"bound to TCP address (127.0.0.1:\d+) ", proc.read())
            url = "http://" + url
            assert requests.get(url + '/set/1/2').text == 'ok'
            assert requests.get(url + '/get/1').text == '2'
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
                     'runserver', '127.0.0.1:0',
                     env=dict(os.environ, UWSGI_CACHE_FALLBACK='y')) as proc:
        with dump_on_error(proc.read):
            wait_for_strings(proc.read, TIMEOUT, '127.0.0.1')
            port = get_ports(proc.proc.pid)
            url = "http://127.0.0.1:%s" % port
            assert requests.get(url + '/set/1/2').text == 'ok'
            assert requests.get(url + '/get/1').text == '2'
            assert requests.get(url + '/clear').text == 'ok'
            assert requests.get(url + '/get/1').text == 'None'
