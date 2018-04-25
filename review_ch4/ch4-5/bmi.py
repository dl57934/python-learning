from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

csv = pd.read_csv('bmi.csv')
label = csv.ix[:,0]
data = csv.ix[:,1:]
trainData,testData,trainLabel,testLabel = train_test_split(data,label,test_size=0.33)
clf = svm.SVC()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)

report = metrics.classification_report(pre,testLabel)
print(report)
