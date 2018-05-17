import os, sys, glob
import json
root = "./newsData/"
wordsData = "./words.json"
mainData = "./data.json"
miniData = "./miniData.json"
word_dic = {"MAX":0}

def makingXY(limit=0):
    fileList = os.listdir(root)
    Y =[]
    X = []
    i = 0
    for fileName in fileList:
        print(fileName)
        if os.path.isdir(root+fileName):
            Xdata = globFile(root+fileName,Y,i,limit)
            X.append(Xdata)
            i+=1
    return X,Y

def globFile(fileName,Y,categoryNum,limit):
    fileList = glob.glob(fileName+"/*.txt.wakati")
    r = []
    result = []
    j = 0
    for fileName in fileList:
        Y.append(categoryNum)
        Xdata = fileRead(fileName)
        Xdata = incWordDic(Xdata)
        cnt = setCnt(Xdata)
        r.append(cnt)
        if limit > 0:
            if limit ==j:break
            j+=1
    result.append(r)
    return result


def fileRead(fileName):
    fp = open(fileName,'r',encoding ='utf-8')
    fp = fp.read().strip()
    return fp.split(" ")

def incWordDic(Xdata):
    result = []
    for data in Xdata:
        if data not in word_dic:
            wid = word_dic[data] = word_dic["MAX"]
            word_dic["MAX"] += 1
        else:
            wid = word_dic[data]
        result.append(wid)
    return result 

def setCnt(wordNum):
    cnt = [ 0 for i in range(word_dic["MAX"])]
    for num in wordNum:
        cnt[num] += 1 
    return cnt 
        
if os.path.exists(wordsData):
    word_dic = json.load(open(wordsData,'r'))
else:
    fileList = glob.glob(root+"*/*.*.wakati")
    for fileName in fileList:
        Xdata = fileRead(fileName)
        incWordDic(Xdata)
    json.dump(word_dic ,open(wordsData,'w'))

X,Y = makingXY()
json.dump({"X":X,"Y":Y},open(mainData,'w'))
