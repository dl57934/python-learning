import pandas as pd
from sklearn import metrics,svm
from sklearn.grid_search import GridSearchCV

train = pd.read_csv('../trainImages/train.csv')
test = pd.read_csv('../trainImages/t10k.csv')

trainLabel = train.ix[:,0]
trainData = train.ix[:,1:577]
testLabel = test.ix[:,0]
testData = test.ix[:,1:577]

params = [
{"C":[1,10,100,1000],"kernel":["linear"]},
{"C":[1,10,100,1000],"kernel":["rbf"],"gamma":[0.001,0.0001]}
]
clf = GridSearchCV(svm.SVC(),params ,n_jobs=-1)
clf.fit(trainData,trainLabel)
print("학습기: ",clf.best_estimator_)
pre = clf.predict(testData)
acScore = metrics.accuracy_score(testLabel,pre)
print(acScore)

