import matplotlib.pyplot as plt
import pandas as pd 

csvFile = pd.read_csv('learning.csv',index_col = 2)

fig = plt.figure()
ax = fig.add_subplot(111)

def scatter(lbl,color):
    b = csvFile.loc[lbl]
    ax.scatter(b['weight'],b['height'],c=color,label=lbl)



scatter('thin','red')
scatter('normal','purple')
scatter('fat','yellow')

ax.legend()
fig.savefig('bmi-test3.png')
