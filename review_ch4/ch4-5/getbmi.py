import random

def getBmi(weight, height):
    bmi = weight /((height/100)**2)
    if bmi < 20: return 'thin'
    elif bmi < 25: return 'normal'
    else: return 'fat'


fp = open('bmi.csv','w',encoding='utf-8')
fp.write('label,weight,height\n')
for idx in range(1000):
    height = random.randint(160,190)
    weight = random.randint(50,97)
    status = getBmi(weight, height)
    fp.write(str(status)+','+str(weight)+','+str(height)+'\n')




