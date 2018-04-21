import codecs

filename = "list_csv.csv"

csv  =  codecs.open(filename,"r","euc_kr").read()
data = []

rows  =  csv.split("\n")
print(rows)
for row in rows:
    if row == "": continue
    cells =  row.split(',')
    data.append(cells)

for c in data:
    print(c[0],c[1],c[2])

