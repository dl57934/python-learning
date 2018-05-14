def ngram(text , num):
    result = []
    leng = len(text) - num +1
    for i in range(leng):
        result.append(text[i:i+num])
    print(result)
    return result

def calNgram(aText, bText,num):
    aList = ngram(aText,num)
    bList = ngram(bText,num)
    cnt = 0
    result = []
    for a in aList:
        for b in bList:
            if a == b:
                cnt += 1
                result.append(a)
    return cnt/len(aList) , result


a = "오늘 강남에서 맛있는 스파게티를 먹었다."
b = "강남에서 먹었던 오늘의 스파게티는 맛있었다."
r2, word2 = calNgram(a,b,2)
print(r2,word2)
