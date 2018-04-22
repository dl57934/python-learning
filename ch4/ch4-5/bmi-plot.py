import matplotlib.pyplot as plt
import pandas as pd

#index_col=2 가로축 2개의 인자의 값만 사용하겠다.
csvFile = pd.read_csv('bmi.csv',index_col=2)

fig = plt.figure()
#첫인자 행 개수 두번째 인자 렬 세번째는 몇번째 subplot에 적용할 건지
ax = fig.add_subplot(111)

def scatter(lbl,color):
    b = csvFile.loc[lbl]
    #인자 x,y좌표 세번째는 색깔 네번째는 저 색들을 나누는 기준->legend에 쓰임
    ax.scatter(b["weight"],b["height"],c=color,label =lbl)

scatter("fat","red")
scatter("normal","yellow")
scatter("thin","purple")


#loc 어디 둘지 bbox_to_anchor 처음이 0 끝이 1 
#legend의 가운데가 기준으로 이동 시킬 수 있음
#ncol 한줄에 몇개의 contents를 둘 수 있는지 나타낸다. 
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0),
           ncol = 3 ,fancybox = True,shadow=True)
plt.savefig("bmi-test2.png")
