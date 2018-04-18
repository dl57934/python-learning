from sklearn import svm, metrics

def load_csv(filename):
    labels = []
    images = []
    with open(filename , 'r') as f:
        for line in f:
            cols = line.split(',')
            if len(cols) < 2 :continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n :int (n) / 256,cols))
            images.append(vals)
    return {'labels':labels, 'images':images}



clf = svm.SVC()            



data = load_csv("./trainImages/train.csv") 
test = load_csv("./trainImages/t10k.csv")

clf.fit(data["images"],data["labels"])
pre = clf.predict(test["images"])
score = metrics.accuracy_score(test["labels"],pre)
cl_report = metrics.classification_report (test["labels"],pre)
print('정답률',score)
print('리포트',cl_report)

