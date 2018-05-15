import json

data = json.load(open("markov-toji2.json",'r'))

print("생각나는 단어를 적어주세요")
word = input()
print(data[word])
