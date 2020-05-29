import requests
import glob
import os
url = "https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q=桃園夫妻居家檢疫失聯　疑輕生雙雙陳屍住處"
response = requests.get(url)
audio = response.content
print(audio)
with open("test.mp3", "wb") as f :
    f.write(audio)
# 進階
# flist = glob.glob("./input/*.txt")
# for fname in flist:
#     with open(fname, "r", encoding="utf-8") as f:
#         print("[處理中]:", fname)
#         article = f.read()
#     speed = 1
#     base = "https://translate.google.com/translate_tts?ie=UTF-8&tl=zh-TW&client=tw-ob&q="
#     url = base + article + "&ttsspeed=" + str(speed)
#     response = requests.get(url)
#     audio = response.content
#     savename = fname.replace(".txt", ".mp3")
#     savename = savename.replace("input", "output", 1)
#     if not os.path.exists("./output"):
#         os.mkdir("./output")
#     with open(savename, "wb") as f :
#         print("[儲存中]:", savename)
#         f.write(audio)


