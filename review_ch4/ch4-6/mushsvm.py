from sklearn.model_selection import train_test_split
from sklearn import svm, metrics 
import pandas as pd

csv = pd.read_csv('mushroom.csv')
label = []
data = []
for idx,v in csv.iterrows():
    data2 = []
    label.append(v[0])
    for value in v.ix[1:]:
        data2.append(ord(value))
    data.append(data2)
    

trainData,testData,trainLabel,testLabel = train_test_split(data,label)

clf = svm.SVC()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)
report = metrics.classification_report(pre,testLabel)
print(report)
