import time

import gevent
import urllib.request


def url_open_gevent():
    while True:
        a = urllib.request.urlopen("https://www.baidu.com/")
        print("A-------")
        gevent.sleep(0.2)


def url_open_gevent2():
    while True:
        a = urllib.request.urlopen("https://www.baidu.com/")
        print("B-------")
        gevent.sleep(0.2)
ge1 = gevent.spawn(url_open_gevent)
time.sleep(10)
"""
gevent.joinall([
    gevent.spawn(url_open_gevent),
    gevent.spawn(url_open_gevent2)
])"""
