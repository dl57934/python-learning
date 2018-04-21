import matplotlib.pyplot as plt 
import pandas 
import json 


with open('./lang/freq.json','r',encoding='utf-8') as fp :
    freq = json.load(fp)


for i,label in enumerate(freq[0]['labels']):
    print(label)
