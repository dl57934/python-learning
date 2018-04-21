from sklearn import svm,metrics
import os.path,re,glob,json 

def checklang(fileName):
    name = os.path.basename(fileName)
    #자기가 찾는 것과 일치하는 데이터 반환
    lang = re.match(r'^[a-z]{2,}',name).group()
    with open( fileName,'r',encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    #list 초기화
    cnt = [0 for a in range(0,26)]
    #아스키 값 구함
    code_a = ord("a")
    code_z = ord("z")
    for letter in text:
        n = ord(letter)
        if code_a <= n <=code_z:
            #영어라면
            cnt[n-code_a] += 1
    total = sum(cnt)
    freq = list(map(lambda a: a / total, cnt))
    return (freq,lang)


def loadfiles(path):
    fileList = glob.glob(path)
    label = []
    langData = []
    for fName in fileList:
        data = checklang(fName)
        label.append(data[1])
        langData.append(data[0])
    return (langData, label)


trainData= loadfiles("./lang/train/*.txt")
testData = loadfiles("./lang/test/*.txt")

clf = svm.SVC()
clf.fit(trainData[0],trainData[1])
pre = clf.predict(testData[0])
score = metrics.accuracy_score(pre , testData[1])
report = metrics.classification_report(pre, testData[1])

print ('정답률',score)
print('보고서',report)

