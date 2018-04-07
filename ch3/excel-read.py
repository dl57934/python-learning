import openpyxl

filename = "stat_104102.xlsx"

book = openpyxl.load_workbook(filename,read_only=True)
sheet = book.worksheets[0]

data = []
for row in sheet.rows:
    data.append([
    row[0].value,
    row[9].value
    ])

del data[0]
del data[1]
del data[2]
del data[3]
print(data.encode("utf-8"))

data = sorted(data, key=lambda x:x[0])

for i,a in enumerate(data):
    if(i >= 5):break
    print(i+1,a[0],a[1]) 


