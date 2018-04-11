import openpyxl

filename = "stat_104102.xlsx"
fp = openpyxl.load_workbook(filename)
sheet = fp.active

for i in range(0,9):
    sheet[str(chr(66+i))+"4"].value = sheet[str(chr(66+i))+"4"].value.replace(",","")
    sheet[str(chr(66+i))+"5"].value = sheet[str(chr(66+i))+"5"].value.replace(",","")

for i in range(0,9):
    total = int(sheet[str(chr(66+i))+"4"].value)
    seoul = int(sheet[str(chr(66+i))+"5"].value)
    result = total - seoul
    sheet[str(chr(66+i))+"24"] = result
    cell = sheet[str(chr(66+i))+"24"]
    cell.font = openpyxl.styles.Font(size=14,color="FF0000")
resultname = "test.xlsx"
fp.save(resultname)
