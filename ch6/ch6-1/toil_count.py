from konlpy.tag import Twitter
from bs4 import BeautifulSoup

with open("BEXX0003.txt","r",encoding="utf-16") as fp:
    text = fp.read()

html = BeautifulSoup(text,"html.parser")

html = html.select_one("body > text")
text = html.getText()

twitter = Twitter()
word_dic={}
words = text.split('\n')
for word in words:
    malist = twitter.pos(word)
    for mal in malist:
        if mal[1] == "Noun":
            if mal[0] not in word_dic:
                word_dic[mal[0]] = 0
            else:
                word_dic[mal[0]] += 1

keys = sorted(word_dic.items(), key=lambda x :x[1],reverse = True)
for item in keys[:30]:
    print("{0}({1}) ".format(item[0],item[1]))
