import random

csv = open('bmi.csv','w',encoding='utf-8')

csv.write('label,height,weight\n')

def getBmi(weight,height):
    bmi = weight / (height/100)**2
    if bmi < 18.5: return 'thin'
    elif bmi <25:   return 'normal'
    else : return 'fat'
for idx in range(20000):
    height = random.randint(120,200)
    weight = random.randint(35,80)
    status = getBmi(weight, height)
    csv.write(status+','+str(height)+','+str(weight)+'\n')

csv.close()
