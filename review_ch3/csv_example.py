import codecs
filename = "list.csv"
csv = codecs.open(filename,"r","utf-8").read()

data = []

rows = csv.split('\n')
print(rows)
for row in rows:
    if(row==""):print("공백") 
    else: print(row)
    
for a in data:
    print(a[0],a[1],a[2])
