import requests
from bs4 import BeautifulSoup
import pandas as pd
df = pd.DataFrame(columns=["時間", "觀看數" "標題", "作者", "路徑", "內文"])
url = "https://www.managertoday.com.tw/articles/view/59188"
response = requests.get(url).text
html = BeautifulSoup(response, "html.parser")
# 以list方式表現 => 加上 [index]
# 嘗試方式 => 找到上層 div ; find / find_all ; 加 [0] ; 加 .text
path = html.find_all("h1")[0].find("a")["href"]
head = html.find_all("h1")[0].find("a").text
# ========>>> 硬取script裡參數的方法 <<<=============
# 找出 post 在哪個 script => 9
eyes = html.find_all("script")
# i = 0
# while i >= 0:
#     print(i, eyes[i])
#     i = i + 1
# 因為 p 為 tag => 找出 total_hits 關鍵字 => 用 split 分出前後 => 取值
p = eyes[9].text
p = p.split("\"total_hits\":")[1]
p = p.split(",")[0]

time = html.find_all("time", itemprop="datePublished")[0].text
time = time.replace("\n", "")
autor = html.find_all("span", itemprop="author")[0].text
article = html.find_all("p")
x = ""
for i in article:
    x = x + "\n" + i.text

s = pd.Series([time, p, head, autor, path, x], index=["時間", "觀看數", "標題", "作者", "路徑", "內文"])
df = df.append(s, ignore_index=True)
print(s)
