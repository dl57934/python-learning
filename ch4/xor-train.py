from sklearn import svm

xor_data = [
#p,q,result
[0,0,0],
[1,0,1],
[0,1,1],
[1,1,0]
]

data = []
result = []
for row in xor_data:
    data.append([row[0],row[1]])
    result.append(row[2])

clf = svm.SVC()
clf.fit(data,result)
pre = clf.predict(data)

ok = 0; total = 0
print(pre)
for i,answer in enumerate(pre):
    if pre[i] == answer : ok +=1
    total += 1

print('result', ok , '/', total , '=',ok/total)


