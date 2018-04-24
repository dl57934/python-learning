from sklearn.ensemble import  RandomForestClassifier as Forest
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd

mushFile = pd.read_csv('mushroom.csv',header=None)


label = []
data = []
attr_list = []
    
for row_index, row in mushFile.iterrows():
    label.append(row.ix[0])
    row_data = []
    for v in row[1:]:
        row_data.append(ord(v))
    data.append(row_data)

trainData,testData,trainLabel,testLabel = train_test_split(data,label,test_size=0.33)

clf = Forest()
clf.fit(trainData, trainLabel)
pre = clf.predict(testData)

accuracy = metrics.accuracy_score(testLabel,pre)
report = metrics.classification_report(testLabel,pre)

print('score',accuracy)
print('report',report)

