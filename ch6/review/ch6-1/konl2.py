from konlpy.tag import Twitter
import codecs
from bs4 import BeautifulSoup 
text = codecs.open("toji.txt",'r',encoding = "utf-16")
bsData = BeautifulSoup(text,'html.parser')
body = bsData.select_one("body > text")
text = body.getText()
twitter = Twitter()
text = text.split('\n')
dic = {}
for line in text:
    malist = twitter.pos(line)
    for word in malist:
        if word[1] == "Noun":
            if word[0] not in dic:
                dic[word[0]] = 0
            dic[word[0]]+=1

sortedDic = sorted(dic.items(), key=lambda k :k[1], reverse=True)

for word, count in sortedDic[:30]:
    print("{0}({1})".format(word,count),end="")
