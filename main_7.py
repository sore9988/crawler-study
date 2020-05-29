import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd

df = pd.DataFrame(columns=["看版", "時間", "標題", "連結"])
dfcon = pd.DataFrame(columns=["標題", "內文"])
page=1
while page <= 3:
    url = "https://tw.appledaily.com/new/realtime/" + str(page)
    try:
        response = requests.get(url).text
    except HTTPError:
        print("[完成] 已到最後一頁")
        break
    html = BeautifulSoup(response)
    content = html.find_all("li", class_="rtddt")
    for i in content:
        path = i.find("a")["href"]
        time = i.find("time").text
        bord = i.find("h2").text
        title = i.find("font").text
        s = pd.Series([bord, time, title, path], index=["看版", "時間", "標題", "連結"])
        df = df.append(s, ignore_index=True)
    print("第", page, "頁處理完成")
    page = page + 1

for d in range(len(df)):
    inurl = df["連結"][d]
    inresponse = requests.get(inurl).text
    inhtml = BeautifulSoup(inresponse)
    intit = inhtml.find_all("meta", property="twitter:title")[0].attrs["content"]
    incont = inhtml.find_all("meta", property="twitter:description")[0].attrs["content"]

    print(intit,incont)   

df.to_csv("applenews1.csv", encoding = "utf-8", index=False)