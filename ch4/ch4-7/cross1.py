import pandas as pd
from sklearn import model_selection, svm, metrics
import re, random

csv = pd.read_csv('../iris.csv')

data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

clf = svm.SVC()
scores = model_selection.cross_val_score(clf,data,label,cv=5)
print(scores)
print(scores.mean())
