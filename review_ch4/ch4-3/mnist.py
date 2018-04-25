from sklearn import svm, metrics
import pandas as pd 
train = pd.read_csv('./mnist/train.csv',header=None)
test = pd.read_csv('./mnist/t10k.csv',header=None)   
trainData = train.ix[:,1:577]
trainarray= []
for idx, data in trainData.iterrows():
    trainarray.append(list(map(lambda n: n/256,data)))
    
trainLabel = train.ix[:,0]
testData = test.ix[:,1:577]
testarray = []
for idx, data in testData.iterrows():
    testarray.append(list(map(lambda n: n/256,data)))
testLabel = test.ix[:,0]

clf = svm.SVC()
clf.fit(trainarray,trainLabel)
pre = clf.predict(testarray)

score = metrics.accuracy_score(pre,testLabel)
print(score)
