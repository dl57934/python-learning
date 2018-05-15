import json,os
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

fileName ="BEXX0003.txt"
jsonFile = "markov-toji2.json"

def make_dic(words):
    dic = {}
    text3 = ["@"]
    for word in words:
        text3.append(word)
        if len(text3) < 3: continue
        if len(text3) > 3: text3 = text3[1:]
        setword3(dic,text3)
        if word == ".":
            text3 = ["@"]
            continue
    return dic 

def setword3(dic,text3):
    w1, w2 ,w3 = text3
    if w1 not in dic: dic[w1] ={}
    if w2 not in dic[w1]:dic[w1][w2] = {}
    if w3 not in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

if not os.path.exists(jsonFile):
    
    twitter = Twitter()
    fp = open(fileName,'r',encoding = 'utf-16')
    text = fp.read().strip()
    bs = BeautifulSoup(text,'html.parser')
    text = bs.select_one('body > text')
    text = text.getText()
    text.replace('…','')
    malist = twitter.pos(text,norm=True)
    words = []
    for word in malist:
        if not word[1] in ["Punctuation"]:
            words.append(word[0])
        if word[0] == ".":
            words.append(word[0])
    dic = make_dic(words)
    json.dump(dic, open(jsonFile,'w',encoding='utf-8'))
else:
    dic = json.load(open(jsonFile,'r',encoding='utf-8'))

