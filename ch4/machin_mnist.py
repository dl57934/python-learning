from sklearn import svm, metrics

def load_csv(filename):
    lables = []
    images = []
    with open(filename , 'r') as f:
        for line in f:
            cols = line.split(',')
            if len(cols) < 2 : continue
            lables.append(int(cols.pop(0))) 
            vals = list(map(lambda a:int(a)/256,cols))
            images.append(vals)            
    return {"label":lables,"images":images}


clf = svm.SVC()            



data = load_csv("./trainImages/train.csv") 
test = load_csv("./trainImages/t10k.csv")

clf.fit (data["images"],data["label"])
pre = clf.predict(test["images"])
score = metrics.accuracy_score(pre,test["label"])
cl_report = metrics.classification_report(test["label"],pre)

print('정답률',score)
print('리포트',cl_report)
