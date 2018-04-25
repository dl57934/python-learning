import pandas as pd
from sklearn import metrics, svm
from sklearn.model_selection import train_test_split
csv = pd.read_csv('iris.csv')
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
name = csv["Name"]

trainData,testData,trainLabel,testLabel = train_test_split(data,name)

clf = svm.SVC()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)
score = metrics.accuracy_score(pre,testLabel)

print(score)


