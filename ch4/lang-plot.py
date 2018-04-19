import matplotlib.pyplot as plt
import pandas as pd
import json 

with open('./lang/freq.json',"r",encoding= 'utf-8') as fp:
    freq = fp.read()


lang_dic={}
for i,lbl in enumerate(freq[0]['labels']):
    fp = freq[0]["freqs"][i]
    if not (lbl in lang_dic):
        lang_dic[lbl] = fq
        print(lang_dic[lbl])

