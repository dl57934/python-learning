import csv,codecs

fp = codecs.open("test.csv","w","utf-8")

writer = csv.writer(fp,delimiter=",",quotechar='"')

writer.writerow(["ID","이름","가격"])
writer.writerow(["1000","이상훈","1000000000",])

