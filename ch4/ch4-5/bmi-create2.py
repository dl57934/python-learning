import random

def getStatus(w,h):
    bmi = w/(h/100)**2
    if bmi <18.5: return 'thin'
    elif bmi < 25: return 'normal'
    else: return 'fat'


#1.작성할  파일을 오픈하죠
csvFile = open('learning.csv','w',encoding = 'utf-8')
csvFile.write('weight,height,label\n')
#몸무게 상태 명수 변수 초기화
weightInfo = {'thin':0,'normal':0,'fat':0}

for idx in range(20000):
    w = random.randint(35,80)
    h = random.randint(120,200)
    status = getStatus(w,h)
    weightInfo[status] += 1
    csvFile.write('{0},{1},{2}\n'.format(w,h,status))
csvFile.close()
print(weightInfo)

