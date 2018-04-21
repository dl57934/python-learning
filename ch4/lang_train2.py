from sklearn import svm,metrics
import os.path,re,json,glob

def checkLang(filename):
    basename = os.path.basename(filename)
    label = re.match(r'^[a-z]{2,}',basename).group()
    with open(filename,'r',encoding='utf-8') as fp:
        text = fp.read()
    text = text.lower()
    lang = [0 for n in range(0,26)]
    ordA = ord('a')
    ordB = ord('z')
    for letter in text:
        inputOrd = ord(letter)
        if ordA <= inputOrd <= ordB:
            lang[inputOrd - ordA] += 1
    total = sum(lang)
    freq = list(map(lambda n:n/total,lang))
    return (freq,label)


def load_file(filename):
    label = []
    freq = []
    fileList = glob.glob(filename)
    for f in fileList:
        data = checkLang(f)
        label.append(data[1])
        freq.append(data[0])
    return (freq,label)


testData = load_file("./lang/test/*.txt")
trainData = load_file('./lang/train/*.txt')

clf = svm.SVC()
clf.fit(trainData[0],trainData[1])
pre = clf.predict(testData[0])

score = metrics.accuracy_score(pre,testData[1])
report = metrics.classification_report(pre,testData[1])

print(score)
print(report)
