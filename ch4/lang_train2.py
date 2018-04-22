from sklearn import svm, metrics
import json, os.path, glob, re

#파일 읽어와서 확인하는 
def checkLang(filename):
    base = os.path.basename(filename)
    label = re.match('^[a-z]{2,}',base).group()
    with open(filename ,'r',encoding= 'utf-8') as fp:
        text = fp.read()
    text = text.lower()
    lang_dict = [0 for n in range(0,26)]
    ord_a = ord('a')
    ord_z = ord('z')
    for f in text:
        ch = ord(f)
        if ord_a <= ch <= ord_z:
            lang_dict[ch-ord_a] += 1
    total = sum(lang_dict)
    return (list(map(lambda n : n/total,lang_dict)),label)      


def load_file(filename):
    label = []
    data = []
#전체 파일 리스트
    fileList = glob.glob(filename)
    for f in fileList:
        fileData = checkLang(f)
        label.append(fileData[1])
        data .append(fileData[0])
    return (data,label)


study_data  = load_file('./lang/train/*.txt')
test_data  = load_file('./lang/test/*.txt')
clf = svm.SVC()

clf.fit(study_data[0],study_data[1])
pre = clf.predict(test_data[0])
score = metrics.accuracy_score(pre,test_data[1])
report = metrics.classification_report(pre,test_data[1])
print(score)
print(report)
