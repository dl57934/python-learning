import matplotlib.pyplot as plt 
import pandas  as pd
import json 


with open('./lang/freq.json','r',encoding='utf-8') as fp :
    freq = json.load(fp)

langdic = {}
for i,label in enumerate(freq[0]['labels']):    
    fq = freq[0]['freqs'][i]
    if not ( label in langdic):
        langdic[label] = fq
        continue
    for i, v in enumerate(fq):
        langdic[label][i] = (langdic[label][i] + v)/2


ascilist = [chr(n) for n in range(97,97+26)]
dataFrame = pd.DataFrame(langdic,index = ascilist)

plt.style.use('ggplot')
dataFrame.plot(kind = 'bar',subplots = True,ylim=(0,0.15))


