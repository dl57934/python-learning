import openpyxl 
filename = "stat_104102.xlsx"

book = openpyxl.load_workbook(filename)

sheet = book.worksheets[0]

data = []

for row in sheet.rows:
    data.append([row[0].value, row[9].value])
del data[0]
del data[0]
del data[0]
del data[len(data)-1]
del data[len(data)-1]
for a in data:
    a[1]=a[1].replace(",","")
print(data)

data = sorted(data,key = lambda x:int(x[1]))

for i,t in enumerate(data):
    if (i>=5): break
    print(i,t[0],t[1])
