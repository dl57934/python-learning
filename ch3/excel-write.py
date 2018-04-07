import openpyxl 

filename = "stat_104102.xlsx"

book  =  openpyxl.load_workbook(filename)

sheet =  book.active
sheet["A24"] = "서울 제외 총명수"

for  i in range(0,9):
    sheet[str(chr(66+i)+"4")] = sheet[str(chr(66+i)+"4")].value.replace(",","")
    sheet[str(chr(66+i)+"5")] = sheet[str(chr(66+i)+"5")].value.replace(",","")
    total = int(sheet[str(chr(66+i)+"4")].value)
    seoul = int(sheet[str(chr(66+i)+"5")].value)
    output = total - seoul 
    print(output)
    sheet[str(chr(66+i)+"24")] = output
    cell = sheet[str(chr(66+i)+"24")]
    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
 
filename = "popular2.xlsx"
book.save(filename)
