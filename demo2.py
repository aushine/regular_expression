import re
import urllib.request
import time
import gevent
from gevent import monkey
content = urllib.request.urlopen("https://h.bilibili.com/196105?from=search&amp;seid=11209062001853798640\\")
print(content.read())