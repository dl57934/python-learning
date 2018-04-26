from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
import sklearn.metrics as metrics

data = []
label = []
attr = []
csv = pd.read_csv('mushroom.csv')
for idx, value in csv.iterrows():
    miniData = []
    label.append(value[0])
    for i, v in enumerate(value.ix[1:]):
        if idx == 0:
            attrLine = {'lbl':{},'cnt':0}
            attr.append(attrLine)
        else :
            attrLine = attr[i]
        d = [0 for n in range(12)]
        if v not in attrLine['lbl']:
            saveloc = attrLine['cnt']
            attrLine['lbl'][v] = saveloc
            attrLine['cnt']+=1
        else:
            saveloc = attrLine['lbl'][v]
        d[saveloc] = 1
        miniData+=(d)
    data.append(miniData)

trainData,testData,trainLabel,testLabel = train_test_split(data,label)

clf = RandomForestClassifier()
clf.fit(trainData, trainLabel)
pre = clf.predict(testData)
report = metrics.classification_report(pre,testLabel)
print(report)


