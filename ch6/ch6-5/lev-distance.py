def calc_distance(a,b):
    if a == b : return 0
    a_len = len(a)
    b_len = len(b)
    matrix = [[] for i in range(a_len+1)]
    for i in range(a_len+1):
        matrix[i] = [0  for i in range(b_len+1)]
    
    for i in range(b_len+1):
        matrix[0][i] = i
    
    for i in range(a_len+1):
        matrix[i][0] = i 
    
    for i in range(1,a_len+1):
        aw = a[i-1]
        for j in range(1,b_len+1):
            bw = b[j-1]
            if aw == bw: 
                cost = 0
            else : 
                cost = 1
            matrix[i][j] = min([
                    matrix[i-1][j] + 1,
                    matrix[i][j-1]+1,
                    matrix[i-1][j-1]+cost])
    return matrix[a_len][b_len]
print(calc_distance("가라다라","가나바라"))


trainStation= ["신촌역", "신천군","신천역","신발","마곡역"]
base = trainStation[0]
r = sorted(trainStation ,key = lambda a : calc_distance(base,a))
print(r)

