import pandas as pd 
from sklearn.model_selection import  train_test_split
from sklearn.ensemble import RandomForestClassifier as forest
from sklearn import metrics

csvFile = pd.read_csv('mushroom.csv',header=None) 
label = []
data = []
for idx, value in csvFile.iterrows():
    label.append(value.ix[0])
    dataList = []
    for v in value.ix[1:]:
        dataList.append(ord(v))
    data.append(dataList)

trainData, testData,trainLabel,testLabel = train_test_split(data,label)
clf = forest()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)
report = metrics.classification_report(pre,testLabel)
print(report)
