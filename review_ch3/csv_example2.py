import csv,codecs 
filename = "list.csv"

fp = codecs.open(filename, "r","utf-8")
reader = csv.reader(fp, delimiter=",",quotechar = '"')
for rows in reader:
    print(rows[0],rows[1],rows[2])
