import pandas as pd
from sklearn import svm,metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv('iris.csv')
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
Name = csv ["Name"]

train_data, test_data, train_label, test_label = train_test_split(data,Name)

clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)

result = metrics.accuracy_score(pre,test_label) 
print('정답률',result)
