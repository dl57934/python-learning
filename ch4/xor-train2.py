import pandas as pd
from sklearn import svm,metrics
xor_input = [
[0,0,0],
[1,0,1],
[0,1,1],
[1,1,0]
]
xor_df = pd.DataFrame(xor_input)
print(xor_df)

data = xor_df.ix[:,0:1]
result = xor_df.ix[:,2]
clf = svm.SVC()
clf.fit(data,result)
pre = clf.predict(data)

ac_score = metrics.accuracy_score(result,pre)





print('정답률',ac_score)
