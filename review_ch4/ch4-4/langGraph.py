import matplotlib.pyplot as plt 
import json
import pandas as pd
lang = {}
with open('lang.json','r',encoding='utf-8') as fp:
    freq = json.load(fp)

for idx, lbl in enumerate(freq[0]['label']):
    text = freq[0]['data'][idx]
    if lbl not in lang:
        lang[lbl] = text
        continue
    for i,v in enumerate(text):
        lang[lbl][i] = (lang[lbl][i] + v)/2

asclist = [[chr(n) for n in range(97,97+26)]]
print(asclist)
df = pd.DataFrame(lang ,index=asclist)
plt.style.use('ggplot')
df.plot(kind='bar', subplots=True)
plt.savefig('1.png')




