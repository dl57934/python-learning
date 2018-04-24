import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as forest

csvFile = pd.read_csv('mushroom.csv',header=None)

data = []
label = []
attrLines =[]
for csv_length,value in csvFile.iterrows():
    label.append(value.ix[0])
    exdata = []
    for num,v in enumerate(value.ix[1:]):
        if csv_length == 0:
            attr = {'dic':{},'cnt':0}
            attrLines.append(attr)
        else:
            attr = attrLines[num]
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v not in attr['dic']:
            idx = attr['cnt']
            attr['dic'][v]= idx
            attr['cnt'] += 1
        else :
            idx = attr['dic'][v]
        d[idx] = 1
        exdata += d
    data.append(exdata)

trainData, testData, trainLabel, testLabel = train_test_split(data,label)

clf = forest()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)
report = metrics.classification_report(pre,testLabel)
print(report)
