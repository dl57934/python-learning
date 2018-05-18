import json 

text = json.load(open('markov.json','r'))

print(text["걱정"],end="\n")
