from sklearn.grid_search import GridSearchCV
from sklearn import svm, metrics
import pandas as pd

trainCsv = pd.read_csv('./trainImages/t10k.csv')
testCsv = pd.read_csv('./trainImages/train.csv')


trainLabel = trainCsv.ix[:,0]
trainData = trainCsv.ix[:,1:]
testLabel = testCsv.ix[:,0]
testData = testCsv.ix[:,1:]

params = [
{"C":[1,10,100,1000],"kernel":["linear"]},
{"C":[1,10,100,1000],"kernel":["rbf"],"gamma":[0.001,0.0001]}
]

clf = GridSearchCV(svm.SVC(),params,n_jobs=-1)
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)

report= metrics.classification_report(pre,testLabel)
print(report)
