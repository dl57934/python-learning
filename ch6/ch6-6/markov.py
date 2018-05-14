import requests
import json
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
import os,re,json,random

session = requests.session()
url = "https://m.search.naver.com/p/csearch/ocontent/spellchecker.nhn"

header = {
       "accept":"*/*",
       "accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
       "accept-encoding":"gzip, deflate, br",
       "referer":"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%A7%9E%EC%B6%A4%EB%B2%95+%EA%B2%80%EC%82%AC%EA%B8%B0&oquery=%EB%A7%9E%EC%B6%A4%EB%B2%95+%EA%B2%80%EC%82%AC%EA%B8%B0&tqi=TYFkplpySD0ssbj%2FyLossssstIh-432793"
        ,"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
   }

def make_dic(words):
    tmp = ["@"]
    dic = {}
    for word in words:
        tmp.append(word)
        if len(tmp) < 3:continue
        if len(tmp) > 3:tmp = tmp[1:]
        set_word3(dic,tmp)
        if word == ".":
            tmp = ["@"]
            continue
    return dic

def set_word3(dic, s3):
    w1,w2,w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3]+=1

def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dic"
    top = dic["@"]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == ".": break
        w1,w2 = w2,w3
        ret = "".join(ret)
        params = {"_callback":"window.__jindo2_callback._spellingCheck_0","q":ret}
        res = requests.get(url,params=params,headers=header)
        textLength = len(res.text)
        jsonData = res.text[42:textLength-2]
        jsonData =json.loads(jsonData)
        bsData = BeautifulSoup(jsonData["message"]["result"]["html"],'html.parser')
        return bsData.getText()

def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))


toji_file = "toji.txt"
dict_file = "markvo-toji.json"
if not os.path.exists(dict_file):
    fp  = open("BEXX0003.txt",'r', encoding = "utf-16")
    soup = BeautifulSoup(fp.read(),'html.parser')
    body =soup.select_one("body > text")
    text = body.getText()
    text = text.replace("…","")
    twitter = Twitter()
    malist = twitter.pos(text,norm = True)
    words = []
    for word in malist:
        if not word[1] in ["Punctuation"]:
            words.append(word[0])
        if word[0] == ".":
            words.append(word[0])
    dic = make_dic(words)
    json.dump(dic,open(dict_file,'w',encoding="utf-8"))
else:
    dic = json.load(open(dict_file,"r"))
print(dic)
for i in range(3):
    s = make_sentence(dic)



