from sklearn import svm, metrics
import pandas as pd

data = [
[0,0,0],
[0,1,1],
[1,0,1],
[1,1,0]
]

frameData = pd.DataFrame(data)
#pandas를 통해서 입력 데이터와 결과 데이터를 쉽게 나눔
inputData = frameData.ix[:,0:1]
resultData = frameData.ix[:,2]

clf = svm.SVC()
#머신러닝 교사학습
clf.fit(inputData, resultData)
#교육시킨 것을 바탕으로 입력값 결과 예측
pre = clf.predict(inputData)
#예측결과와 실제 답을 비교
score = metrics.accuracy_score(pre, resultData)

print(score)
