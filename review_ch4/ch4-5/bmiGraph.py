import matplotlib.pyplot as plt
import pandas as pd
csv = pd.read_csv('bmi.csv',index_col = 0)
fig  = plt.figure()
ax = fig.add_subplot(1,1,1)

print(csv)

def scatter(lbl, color):
    b = csv.loc[lbl]
    ax.scatter(b['weight'],b['height'], c=color,label =lbl)
scatter('fat','red')
scatter('normal','blue')
scatter('thin','yellow')


ax.legend()
plt.savefig('2.png')




