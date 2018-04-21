import openpyxl 
filename = "stat_104102.xlsx"
book = openpyxl.load_workbook(filename)
worksheet = book.active
for i in range(0,9):
    worksheet[str(chr(66+i)+"4")] =  worksheet[str(chr(66+i)+"4")].value.replace(",","")
    worksheet[str(chr(66+i)+"5")] =  worksheet[str(chr(66+i)+"5")].value.replace(",","")
    total = int(worksheet[str(chr(66+i)+"4")].value)
    seoul = int(worksheet[str(chr(66+i)+"5")].value)
    out =total - seoul
    print(out)
    worksheet[str(chr(66+i)+"24")] = out
    cell = worksheet[str(chr(66+i)+"24")]
    cell.font = openpyxl.styles.Font(size=14,color = "FF0000")
savename = "example.xlsx"
book.save(savename)
