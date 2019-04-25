import urllib.request
import re
web_content = urllib.request.urlopen("https://search.jd.com/Search?keyword=jk&enc=utf-8&wq=jk&pvid=10032cbfee8643fda0de4bf73d2b55b4")
web_content = web_content.read()
img_url = re.findall(r"//img20\.360buyimg\.com/.{1,8}.{20,80}\.jpg", str(web_content))
for i in img_url:
    print(i)