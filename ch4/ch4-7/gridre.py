import pandas as pd
from sklearn import metrics,svm,model_selection

csv = pd.read_csv('../iris.csv')

data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
name = csv["Name"]

clf = svm.SVC()
scores = model_selection.cross_val_score(clf,data,name,cv=5)
print(scores)
print('평균',scores.mean())
