import codecs 
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
import json
fp = codecs.open('toji.txt','r',encoding='utf-16')

word_dic ={}
def three_dic(words):
    threeDic = ["@"]
    dic = {}
    for word in words:
        threeDic.append(word)
        if len(threeDic) < 3: continue
        if len(threeDic) > 3: threeDic = threeDic[1:] 
        setWord_dic(threeDic)
        if word == ".":
            threeDic= ["@"]

def setWord_dic(threeData):
    s1,s2,s3 = threeData
    if s1 not in word_dic: word_dic[s1] = {}
    if s2 not in word_dic[s1]: word_dic[s1][s2]={}
    if s3 not in word_dic[s1][s2]: word_dic[s1][s2][s3]=0
    word_dic[s1][s2][s3] += 1

twitter = Twitter()
bsData = BeautifulSoup(fp,'html.parser')
body = bsData.select_one('body > text')
lines = body.getText()
lines = lines.replace("…","")
words = []
malist = twitter.pos(lines,norm=True)
for word in malist:
    if word[1] not in ["Punctuation"]:
        words.append(word[0])
    if word[0] == ",":
        words.append(word[0])
three_dic(words)
json.dump(word_dic ,open('markov.json','w',encoding ='utf-8'))
