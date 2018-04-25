from sklearn import svm,metrics
import pandas as pd

data = [ [0,0,0],
        [0,1,1],
        [1,0,1],
        [1,1,0]]

data = pd.DataFrame(data)
label =  data.ix[:,2]
xorData = data.ix[:,0:1]
clf = svm.SVC()
clf.fit(xorData,label)
pre = clf.predict(xorData)

score = metrics.accuracy_score(pre,label)
print(score)

