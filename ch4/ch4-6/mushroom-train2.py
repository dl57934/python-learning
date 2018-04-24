import pandas as pd
from sklearn.ensemble import RandomForestClassifier as Forest
from sklearn import metrics 
from sklearn.model_selection import train_test_split

mr = pd.read_csv('mushroom.csv',header=None)

label = []
data = []
attr_list = []
attr_length = 0
for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    exdata = []
    for col,v in enumerate(row.ix[1:]):
        if row_index == 0 :
            attr = {"dic":{},"cnt":0}
            attr_list.append(attr)
        else:
            #col은 위 칼럼 인덱스 값 0~
            attr = attr_list[col]
        #d는 각배열 인덱스 정보 하나당 서로 다른 특징들을 뜻한다.
        #한마디로 [0]은 x특징이 마크 다른 버섯에 x 가 있어도 d의 [0]에 1이 인정된다. 
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
    
        if v in attr["dic"]:
        #이미 등록된 특징이라면 몇번째 등록됬는지의 관한 값을 가져오기
            idx = attr["dic"][v] 
        else: 
        #처음 나오는 특징 등록하기
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] +=1
        #그 특징 위치에 1더하기
        d[idx] = 1
        exdata += d #12 * 22 개의 데이터를 exdata를 더한다. 
    data.append(exdata)

trainData,testData, trainLabel,testLabel = train_test_split(data,label)


clf = Forest()
clf.fit(trainData,trainLabel)
pre = clf.predict(testData)
score = metrics.accuracy_score(pre,testLabel)
report = metrics.classification_report(pre,testLabel)

print(score)
print(report)
    
    
 




