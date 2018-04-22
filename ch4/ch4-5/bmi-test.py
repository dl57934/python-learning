from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd 

csvData = pd.read_csv('bmi.csv')
label = csvData['label']
h = csvData['height']
w = csvData['weight']
# axis사용하면 인식되어지는 값이 위에 붙는다. 
wh = pd.concat([w,h],axis=1)

trainData, testData, trainLabel, testLabel = train_test_split(wh,label)

clf = svm.SVC()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)
score = metrics.accuracy_score(pre,testLabel)
report = metrics.classification_report(pre,testLabel)
print(score)
print(report)
