import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
csv = pd.read_csv('mushroom.csv')

label = []
data = []

for idx, value in csv.iterrows():
    label.append( value[0])
    minidata = []
    for v in value.ix[1:]:
        minidata.append(ord(v))
    data.append(minidata)

trainData , testData, trainLabel, testLabel = train_test_split(data,label)

clf = RandomForestClassifier()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)
report = metrics.classification_report(pre,testLabel)
print(report)
    

