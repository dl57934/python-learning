from sklearn import svm, model_selection,metrics
import pandas as pd


iris = pd.read_csv('iris.csv')
data = iris[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = iris["Name"]
clf= svm.SVC()
result = model_selection.cross_val_score(clf, data, label,cv=5)
print(result)
print(result.mean())
