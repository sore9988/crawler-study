from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
url = "https://www.ptt.cc/bbs/Gossiping/M.1584592191.A.F05.html"
# 加上Header
# r = Request(url)
# r.add_header("user-agent", "Mozilla/5.0")
# response = urlopen(r)

# requests 會自動幫你填上簡單的 Header
import requests
jar = requests.cookies.RequestsCookieJar()
jar.set("over18", "1", domain = "www.ptt.cc")

response = requests.get(url, cookies=jar).text

html = BeautifulSoup(response)
content = html.find("div", id="main-content")
values = content.find_all("span", class_="article-meta-value")
print("作者:",values[0].text)
print("看板:",values[1].text)
print("標題:",values[2].text)
print("時間:",values[3].text)

meta = content.find_all("div", class_="article-metaline")

for m in meta:
    m.extract()

right_meta = content.find_all("div", class_="article-metaline-right")
for single_meta in right_meta:
    single_meta.extract()

pushes = content.find_all("div", class_="push")
scoreup = 0
scoredown = 0
for single_push in pushes:
    pushtag = single_push.find("span", class_="push-tag").text
    if "推" in pushtag:
        scoreup = scoreup + 1
    elif "噓" in pushtag:
        scoredown = scoredown + 1
    single_push.extract()
score = scoreup - scoredown
print("推文分數:", scoreup)
print("噓文分數:", scoredown)
print("總分:", score)

print(content.text)


