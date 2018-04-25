import pandas as pd 
import matplotlib.pyplot as mtl

csv = pd.read_csv('bmi.csv',index_col=0)
fig = mtl.figure()
ax = fig.add_subplot(1,1,1)
print(csv.loc['normal'])
def scatter(lbl, color):
    b = csv.loc[lbl]
    ax.scatter(b['height'],b['weight'],c=color,label =lbl)

scatter('fat','red')
scatter('normal','yellow')
scatter('thin','blue')

ax.legend()
mtl.savefig('1.png')

