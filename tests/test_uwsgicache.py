import re
import os

import requests
from process_tests import dump_on_error
from process_tests import setup_coverage
from process_tests import TestProcess
from process_tests import TestSocket
from process_tests import wait_for_strings

TIMEOUT = int(os.getenv('UWSGICACHE_TEST_TIMEOUT', 10))


def test_everything():
    with TestProcess('uwsgi', '--http-socket', '127.0.0.1:0') as proc:
        wait_for_strings(proc.read, TIMEOUT, 'bound to TCP address 127.0.0.1')
        url, = re.findall(r"bound to TCP address (127.0.0.1:(\d+) ", proc.read())

        assert requests.get(url + '/set/1/2').text == 'ok'

        assert requests.get(url + '/get/1').text == '2'

        assert requests.get(url + '/clear').text == 'ok'

        assert requests.get(url + '/get/1').text == 'None'
