import pandas as pd
from sklearn import metrics 
from sklearn.ensemble import RandomForestClassifier as forest
from sklearn.model_selection import train_test_split

csvFile = pd.read_csv('mushroom.csv')

label = []
data = []
for idx, v in csvFile.iterrows():
    label.append(ord(v.ix[0]))
    listData = []
    for value in v.ix[1:]:
        listData.append(ord(value))
    data.append(listData)

trainData,testData,trainLabel,testLabel = train_test_split(data,label,test_size=0.33)

clf = forest()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)

score = metrics.accuracy_score(pre,testLabel)
report = metrics.classification_report(pre,testLabel)
print(score)
print(report)

