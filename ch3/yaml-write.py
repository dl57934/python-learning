import yaml 

customer = [
{"name":"bubKyu","age":22,"gender":"man"},
{"name":"nambi","age":24,"gender":"abai"},
{"name":"sangmain","age":38,"gender":"man"}
]
#yaml형식으로 출력
data = yaml.dump(customer)
print(data)

#yaml 데이터 골라서 출력

data = yaml.load(data)

for p in data:
    print("name",p["name"])


