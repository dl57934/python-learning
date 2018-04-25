from sklearn import metrics, svm
import glob, os.path, re, json


def Judge(filename):
    name = os.path.basename(filename)
    langlbl =re.match(r'^[a-z]{2,}',name).group()
    with open (filename, 'r',encoding='utf-8') as fp:
        data = fp.read()
        data = data.lower()
    cnt = [0 for n in range(26)]
    ord_a,ord_z = ord('a'),ord('z')
    for ch in data:
        ord_ch = ord(ch)
        if ord_a <= ord_ch <= ord_z:
            cnt[ord_ch-ord_a] += 1
    total = sum(cnt)
    newCnt=list(map(lambda n : n/total,cnt))
    return (newCnt,langlbl)


def load_csv(filename):
    label = []
    cnt = []
    fileList = glob.glob(filename)
    for name in fileList:
        Info = Judge(name)
        label.append(Info[1])
        cnt.append(Info[0])
    return {'data':cnt,'label':label}


trainData = load_csv('./lang/train/*.txt')
testData = load_csv('./lang/test/*.txt')

with open('./lang.json','w',encoding='utf-8') as fp:
    json.dump([trainData,testData],fp)


clf = svm.SVC()
clf.fit(trainData['data'],trainData['label'])
pre = clf.predict(testData['data'])
report = metrics.classification_report(pre,testData['label'])
print(report)





        
