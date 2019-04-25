import re
import urllib.request
import time
import gevent
from gevent import monkey
"""1.先把主网页获取,然后把网页中的每一个子网页(跳转)提取到
   2.再在子网页把每一个图片的源文件地址提取到一个列表中存储
   3.遍历图片源文件地址获取每一个图片的内容并写入本地文件中
"""
'''练习停止,相册打开后的页面由js编写的动态网页,urlopen不能获取内容'''
# 图片的
monkey.patch_all()


def image_downloader(image_url):
    folder = "C:/Users/16152/Desktop/material/sakura"
    for url in image_url:
        url = "https:"+url
        image_content = urllib.request.urlopen(url).read()
        with open(folder+"/"+str(int(time.time()))+".jpg", "wb")as f:
            f.write(image_content)


def url_dispose_func(imgs_url):
    url_content = urllib.request.urlopen(imgs_url).read()
    print(url_content)
    #image_url = re.findall(r"https://i0.hdslb.com/bfs/.{40,50}\.[pnjp]{2}g", str(url_content))
    # images_url = re.findall(r"//h\.bilibili.com/[0-9?]{5,10}from=search&amp;seid=[0-9]{15,25}", str(content))
    #print(image_url)


def main():
    url_text = urllib.request.urlopen("https://search.bilibili.com/photo?keyword=%E5%85%AB%E9%87%8D%E6%A8%B1")
    url_content = url_text.read()

    # 获取到了第一页所有的相册跳转链接
    url_dispose = re.findall(r"//h\.bilibili.com/[0-9?]{5,10}from=search&amp;seid=[0-9]{15,25}", str(url_content))

    # 每个相册的跳转都出现了两次,使用set去重
    imgs_url = list(set(url_dispose))

    # 将每个相册的地址送去图片地址处理
    gevent_list = list()
    for dlbum in imgs_url:
        print(dlbum)
        gevent_list.append(gevent.spawn(url_dispose_func, "https:"+dlbum))
        # url_dispose_func("https:"+dlbum)
    gevent.joinall(gevent_list)
    # url_dispose(url_sorce_content)
    # image_url = re.findall(r"//i0.hdslb.com/bfs/.{10,50}\.jpg", str(url_sorce_content))


    # for i in image_url:
    #        # print(i)


if __name__ == "__main__":
    main()

