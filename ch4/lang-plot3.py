import matplotlib.pyplot as plt
import pandas as pd 
import json
#그래프를 만들기 전에 2차원 배열로 만들어주기
with open ('./lang/freq.json','r',encoding = 'utf-8') as fp:
    freq = json.load(fp)


langdic = {}
for idx, label in enumerate(freq[0]['labels']):
    data = freq[0]['freqs'][idx]
    if not (label in langdic):
        langdic[label] = data
        continue
    for i, v in enumerate(data):
        langdic[label][i] = (langdic[label][idx]+v)/2

ascilist = [chr(n) for n in range(97,97+26)]
asciiLine = pd.DataFrame(langdic ,index = ascilist)

plt.style.use('ggplot')
asciiLine.plot(kind="bar",subplots = True, ylim = (0,0.15))
plt.savefig("lang-plot3.png")
