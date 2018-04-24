from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as forest
import pandas as pd 

csvFile = pd.read_csv('mushroom.csv',header=None)

data =[]
csvList = []
label = []
attr = []
for csv_idx, value in csvFile.iterrows():
    exdata = []
    label.append(value.ix[0])
    for idx , v in enumerate(value.ix[1:]):
        if csv_idx == 0:
            attrLines = {'dic':{},'cnt':0}
            attr.append(attrLines)
        else :
            attrLines = attr[idx]
        d= [0,0,0,0,0,0,0,0,0,0,0,0]
        if v not in attrLines['dic']: 
            idx = attrLines['cnt']
            attrLines['dic'][v] = idx 
            attrLines['cnt']+=1
        else :
            idx = attrLines['dic'][v]
        d[idx] = 1
        exdata += d
    data.append(exdata)

trainData,testData,trainLabel,testLabel = train_test_split(data,label)
clf = forest()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)
score = metrics.accuracy_score(pre,testLabel)
report = metrics.classification_report(pre,testLabel)
print(score)
print(report)



        
