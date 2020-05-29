import requests
from bs4 import BeautifulSoup
import pandas as pd
df = pd.DataFrame(columns=["時間", "觀看數" "標題", "作者", "路徑", "內文"])
url = "https://www.managertoday.com.tw/columns/view/58909"
response = requests.get(url).text
html = BeautifulSoup(response, "html.parser")

content = html.find_all("dia", class_="meta")
for r in content:
    time = r.find("span", class_="date")
print(content)
