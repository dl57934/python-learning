import openpyxl
filename = "popular.xlsx"

data = []

book = openpyxl.load_workbook(filename)
shell = book.worksheets[0]

for row in shell.rows:
    data.append([row[0].value, row[9].value])
print(data)
for i in range(0,4):
    del data[0]

del data[len(data)-1]
del data[len(data)-1]
del data[len(data)-1]

for a in data:
    a[1]=a[1].replace(",","")

data = sorted(data,key = lambda x: int(x[1]))

for i,a in enumerate(data):
    if (i>=5): break
    print(i+1,a[0],a[1])
