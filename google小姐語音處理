import requests
with open("n.txt", "r", encoding="utf-8") as f:
    article = f.read()
# nltk 分句子
from nltk import tokenize
tok_article = tokenize.sent_tokenize(article)
# b為byte的意思
allcontent = b""
baseurl = "https://translate.google.com/translate_tts?ie=UTF-8&tl=zh-TW&client=tw-ob&q="
for sentence in tok_article:
    print("[處理句子]:", sentence)
    url = baseurl + sentence
    response = requests.get(url)
    response.raise_for_status()
    # 把得到的content加在容器後
    audio = response.content
    allcontent = allcontent + audio
with open("all.mp3", "wb") as f:
    f.write(allcontent)


