import matplotlib
from urllib.request import urlopen, urlretrieve
import json
import os
from PIL import Image
import matplotlib.pyplot as plt
# google doodles 抓取
# 使用這行可以不用.show 來最後 show 出來
# %matplotlib inline
# 準備一個空的 list 來儲存
urllist = []
for m in range(1,3):
    url="https://www.google.com/doodles/json/2019/" + str(m) + "?hl=zh_TW"
    print("處理月份:", m)
    response = urlopen(url)
    # print(response)
    doodles = json.load(response)
    # print(doodles)
    for d in doodles:
        url = "https:" + d["url"]
        title = d["title"]
        # print("圖片標題:", title)
        # print("圖片網址:", url)
        urllist.append(url)
        # 須自己先建資料夾 -> 自動建資料夾
        dirname = "doodles/" + str(m)
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        fpath = dirname +"/" + url.split("/")[-1]
        # print(url.split("/")[-1])
        urlretrieve(url, fpath)
    print(str(m),"月,總共圖片數:", len(urllist))
    # 把大圖準備成 寬 * 高 個小圖
    # 我想要每列五個圖
    # width = 5
    # 算出來應該會是多少個列
    # height = int(len(urllist) / width) + 1
    # 順便調整整個大圖大小, 我用 20 英吋 * 30 英吋
    # plt.figure(figsize=(20, 30))
    # enumerate 可以回傳 (index, 資料) 這樣的 tuple
    # for (index, url) in enumerate(urllist):
    #     plt.subplot(height, width. index + 1)
    #     response = urlopen(response)
    #     # 利用 PIL 讀取圖片
    #     img = Image.open(response)
    #     plt.axis("off")
    #     plt.imshow(img)



