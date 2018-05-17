
def leven(aText,bText):
    aLen = len(aText)+1
    bLen = len(bText)+1
    array = [ [] for a in range(aLen) ]
    for i in range(aLen):
        array[i] = [0 for a in range(bLen)]
    for i in range(bLen):
        array[0][i] = i
    for i in range(aLen):
        array[i][0] = i
    cost = 0
    print(array)
    for i in range(1,aLen):
        for j in range(1,bLen):
           if aText[i-1] != bText[j-1]:
               cost = 1
           else :
               cost = 0
           addNum = array[i-1][j] + 1 #추가
           minusNum = array[i][j-1] + 1 #감소
           modiNum = array[i-1][j-1]+cost #
           minNum = min([addNum,minusNum,modiNum])
           array[i][j] = minNum
            
    return array[aLen-1][bLen-1]
leven("가나다라", "가마바라")
samples = ["신발"]
result = sorted(samples, key = lambda x  : leven("신촌역",x))
print(result)

