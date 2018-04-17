
from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split

csv = pd.read_csv('iris.csv')
inputName = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
resultName = csv["Name"]
#뒤에 test_case 옵션때문에 150개의 데이터 중 50개가 테스트 데이터로 간다.
trainData, testData, trainResult, testResult = train_test_split(inputName,resultName,test_size=0.33)
clf = svm.SVC()
#머신러닝
clf.fit(trainData, trainResult)
#앞선 훈련 결과로 테스트 데이터 예측값 구하기
pre = clf.predict(testData)

score = metrics.accuracy_score(pre, testResult)

print("정답률",score)
