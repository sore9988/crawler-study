import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_page_meta(url):
    jar = requests.cookies.RequestsCookieJar()
    jar.set("over18", "1", domain="www.ppt.cc")
    if not "公告" in title and not "版bs規" in title:
        response = requests.get(url, cookies=jar).text
        html = BeautifulSoup(response, "html.parser")
        content = html.find("div", id="main-content")
        result = {}
        values = content.find_all("span", class_="article-meta-value")
        result["author"] = values[0].text
        result["board"] = values[1].text
        result["title"] = values[2].text
        result["time"] = values[3].text
        meta = content.find_all("div", class_="article-metaline")
        for m in meta:
            m.extract()
        right_meta = content.find_all("div", class_="article-metaline-right")
        for rm in right_meta:
            rm.extract()
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
        result["score"] = score
        result["content"] = content.text
        return result
    else:
        return None
jar = requests.cookies.RequestsCookieJar()
jar.set("over", "1", domain="www.ptt.cc")
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
df = pd.DataFrame(columns=["作者", "看板", "標題", "時間", "分數", "內容"])
for times in range(5):
    response = requests.get(url, cookies=jar).text
    html = BeautifulSoup(response, "html.parser")
    articles = html.find_all("div", class_="r-ent")
    for single_article in articles:
        title_area = single_article.find("div", class_="title").find("a")
        if title_area:
            title = title_area.contents[0]
            article_url = "https://www.ptt.cc" + title_area["href"]
            result = get_page_meta(article_url)
            if result:
                data = [result["author"], result["board"], result["title"],
                        result["time"], result["score"], result["content"]]
                s = pd.Series(data, index=["作者", "看板", "標題", "時間", "分數", "內容"])
                df = df.append(s, ignore_index=True)
    url = "https://www.ptt.cc" + html.find("a", text=re.compile(r"上頁"))["href"]
    print(url)
df.to_csv("ptt2.csv", index=False, encoding="utf-8")



