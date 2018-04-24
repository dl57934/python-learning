import pandas as pd
from sklearn import model_selection, svm, metrics
from sklearn.grid_search import GridSearchCV

train_csv = pd.read_csv('../trainImages/train.csv')
test_csv = pd.read_csv('../trainImages/t10k.csv')

train_label = train_csv.ix[:, 0]
train_data = train_csv.ix[:, 1:577]
test_label = test_csv.ix[:, 0]
test_data = test_csv.ix[:, 1:577]
print('학습데이터 수: ',len(train_label))

params = [
{"C":[1,10,100,1000],"kernel":["linear"]},
{"C":[1,10,100,1000],"kernel":["rbf"],"gamma":[0.001,0.0001]}
]
#n_jobs = -1 병렬계산할 프로세서 개수 구한다. -1이면 자동으로 코어수에 맞게 프로세스 수를 정해줍니다.
clf = GridSearchCV(svm.SVC(), params, n_jobs=-1)
clf.fit(train_data,train_label)
print('학습기 =',clf.best_estimator_)

pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(pre,test_label)
report = metrics.classification_report(pre,test_label)
print('score: ',ac_score)
print('report: ',report)


