import pandas as pd
from sklearn import metrics, svm
from sklearn.model_selection import train_test_split

csvFile = pd.read_csv('learning.csv')

wData = csvFile['weight']/80
hData = csvFile['height']/200
label = csvFile['label']
#axis = 0 index를 기준으로 axis = 1 colums를 기준으로 실행한다 
wh = pd.concat([wData,hData],axis=1)
print(wh)
#데이터 분리

#trainData, testData, trainLabel, testLabel = train_test_split(wh,label,test_size = 0.33)

#clf = svm.SVC()
#clf.fit(trainData,trainLabel)
#pre = clf.predict(testData)

#score = metrics.accuracy_score(pre,testLabel)
#report = metrics.classification_report(pre,testLabel)

#print(score)
#print(report)


