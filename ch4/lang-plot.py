import matplotlib.pyplot as plt
import pandas as pd
import json

with open('./lang/freq.json',"r",encoding= 'utf-8') as fp:
    freq = json.load(fp)
lang_dic = {}
for idx, label in enumerate(freq[0]['labels']):
    fq = freq[0]['freqs'][idx]
    if not (label in lang_dic):
        lang_dic[label] = fq 
        continue
    for i,v in enumerate(fq):
        lang_dic[label][i] = (lang_dic[label][i]+v)/2

asclist = [[chr(n) for n in range(97,97+26)]]
df = pd.DataFrame(lang_dic, index=asclist)
print(df)
plt.style.use('ggplot')
df.plot(kind = "line",subplots=True)
plt.savefig("lang-plotline.png")


