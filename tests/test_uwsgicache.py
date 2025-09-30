import os
import re
import time

import httpx
from process_tests import TestProcess
from process_tests import dump_on_error
from process_tests import wait_for_strings

TIMEOUT = int(os.getenv("UWSGICACHE_TEST_TIMEOUT", 3))


def assertions(url):
    assert httpx.get(url + "/get/1").text == "None"
    assert httpx.get(url + "/set/1/a").text == "ok"
    assert httpx.get(url + "/get/1").text == "a"
    assert httpx.get(url + "/clear").text == "ok"
    assert httpx.get(url + "/get/1").text == "None"
    assert httpx.get(url + "/set/2/b?timeout=3").text == "ok"
    time.sleep(2)  # 2 * cache-expire-freq
    assert httpx.get(url + "/get/2").text == "b"
    time.sleep(3)  # 1 + 2 * cache-expire-freq
    assert httpx.get(url + "/get/2").text == "None"
    assert httpx.get(url + "/set/3/c?timeout=0").text == "ok"
    time.sleep(2)  # 2 * cache-expire-freq
    assert httpx.get(url + "/get/3").text == "None"
    assert httpx.get(url + "/set/4/d?timeout=None").text == "ok"
    time.sleep(2)  # 2 * cache-expire-freq
    assert httpx.get(url + "/get/4").text == "d"
    assert httpx.get(url + "/add/5/e").text == "True"
    assert httpx.get(url + "/get/5").text == "e"
    assert httpx.get(url + "/add/6/f?timeout=3").text == "True"
    time.sleep(2)  # 2 * cache-expire-freq
    assert httpx.get(url + "/get/6").text == "f"
    time.sleep(3)  # 1 + 2 * cache-expire-freq
    assert httpx.get(url + "/get/6").text == "None"
    assert httpx.get(url + "/add/7/g?timeout=0").text == "True"
    time.sleep(2)  # 2 * cache-expire-freq
    assert httpx.get(url + "/get/7").text == "None"
    assert httpx.get(url + "/add/8/h?timeout=None").text == "True"
    time.sleep(2)  # 2 * cache-expire-freq
    assert httpx.get(url + "/get/8").text == "h"


def test_uwsgi():
    with TestProcess(
        "uwsgi",
        "--http-socket",
        "127.0.0.1:0",
        "--module",
        "test_project.wsgi",
        "--master",
        "--cache-expire-freq",
        "1",
        "--cache2",
        "name=foobar,items=20",
    ) as proc:
        with dump_on_error(proc.read):
            wait_for_strings(proc.read, TIMEOUT, "bound to TCP address 127.0.0.1")
            (url,) = re.findall(r"bound to TCP address (127.0.0.1:\d+) ", proc.read())
            url = "http://" + url
            assertions(url)


def test_locmem():
    with TestProcess(
        "django-admin",
        "runserver",
        "127.0.0.1:0",
        "--traceback",
        "--noreload",
        "--nothreading",
        env=dict(os.environ, UWSGI_CACHE_FALLBACK="y"),
    ) as proc:
        with dump_on_error(proc.read):
            wait_for_strings(proc.read, TIMEOUT, "Starting development server at http://127.0.0.1:")
            (url,) = re.findall(r"Starting development server at (http://127.0.0.1:\d+)/", proc.read())
            assertions(url)
