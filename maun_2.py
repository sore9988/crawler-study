from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd
df = pd.DataFrame(columns=["評分", "日文店名", "英文店名", "Blog"])
page=53
while True:
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    try:
        response = urlopen(url)
    except HTTPError:
        print("[完成] 已到最後一頁")
        break
    html = BeautifulSoup(response)
    resturant = html.find_all("li", class_="list-rst")
    # print(resturant)
    for r in resturant:
        en = r.find("a", class_="list-rst__name-main")
        ja = r.find("small", class_="list-rst__name-ja")
        scores = r.find("b", class_="c-rating__val")
        s = pd.Series([scores.text, en.text, ja.text, en["href"]]
                      , index=["評分", "日文店名", "英文店名", "Blog"])
        df = df.append(s, ignore_index=True)
    print("處理完第" , page , "頁")
    page = page + 1
print(df)
# df.to_csv("tabelog.csv", encoding="utf-8", index=False)