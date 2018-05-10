import pandas as pd 
#2차원 배열
data = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
]

result = pd.DataFrame(data)
print(result)

#1차원 배열 
data = ["Series","Avangers","Guardians Of the Galaxy"]

result = pd.Series(data)
print(result)

data = {
    "weight":[80.0,70.4,65.5,45.9,51.2],
    "height":[170,180,155,143,154],
    "type":["f","n","n","t","t"]
    }

result = pd.DataFrame(data)
print(result,"\n")


print('몸무게 목록\n',result["weight"])
print('키와 몸무게 목록\n',result[["weight","height"]])
print("result 인덱스 2에서 3까지\n",result[2:4])
print("result 인덱스 2부터 모든 값\n",result[2:])


data = {
    "weight":[80.0,70.4,65.5,45.9,51.2],
    "height":[170,180,155,143,154],
    "gender":["f","m","f","m","f"]
    }
result = pd.DataFrame(data)

ifHeight = result[result.height>=160]
print(ifHeight)

gender = result[result.gender == 'm']
print(gender)

height = result.sort_values(by="height")
print(height)

weight = result.sort_values(by="weight",ascending =False)
print(weight)

data = [
["A","B","C"],
["D","E","F"],
["G","H","I"]
]
result = pd.DataFrame(data)
print(result)
print("\n\n\n")
print(result.T)

