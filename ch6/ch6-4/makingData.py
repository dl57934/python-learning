import os, sys, glob,json

root_dir = "./newsData/"
fileName = root_dir+"shData.json"
miniFileName = root_dir +"shMiniData.json"
wordFile = root_dir + "word.json"
word_dic = {"MAX":0}

def setWord_dic(words):
    result = []
    for word in words:
        if word not in word_dic:
            wid = word_dic[word] = word_dic["MAX"]
            word_dic["MAX"] +=1
        else :
            wid = word_dic[word]
        result.append(wid)
    return result

def countFreq(limit = 0):
    X,Y = getResult(limit)
    return X,Y


def getCnt(result):
    cnt = [0 for n in range(word_dic["MAX"])]
    for word in result:
        cnt[word]+=1
    return cnt


def getResult(limit = 0):
    X = []
    Y = []
    i = 0
    categoryNum = 0
    filesName = os.listdir(root_dir)
    for category in filesName:
        i = 0
        files = glob.glob(root_dir+category+"/*.wakati")
        if os.path.isdir(root_dir+category):
            categoryNum+=1
            for fileName in files:
                Y.append(categoryNum-1)
                print(categoryNum-1)
                with open(fileName,"r") as fp:
                    X.append( getCnt(setWord_dic(fp.read().strip().split(' '))))
                if limit > 0:
                    if i > limit:
                        break
                    else:
                        i+=1
    return X,Y

if os.path.exists(wordFile):
    word_dic = json.load(open(wordFile,'r'))
else :
    getResult()
    json.dump(word_dic,open(wordFile,'w'))

X,Y = countFreq(10)
json.dump({"X":X,"Y":Y},open(miniFileName,"w"))
X,Y = countFreq()
json.dump({"X":X,"Y":Y},open(fileName,"w"))
