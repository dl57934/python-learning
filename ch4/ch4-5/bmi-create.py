import random
def calc_bmi(h,w):
    bmi = w/(h/100)**2 
    if bmi < 18.5: return 'thin'
    elif bmi <25: return 'normal'
    else :return 'fat'
fp = open('bmi.csv','w',encoding = 'utf-8')
fp.write("height,weight,label\n")

cnt = {"thin":0,"normal":0,"fat":0}
for data in range(20000):
    h = random.randint(120,200)
    w = random.randint(40,80)
    whatStatus = calc_bmi(h,w)
    cnt[whatStatus] +=1
    fp.write("{0},{1},{2}\n".format(h,w,whatStatus))
fp.close()
print(cnt)

    
    
