import csv, codecs 

filename = "list_csv.csv"

fp = codecs.open(filename, "r", "euc_kr")

reader = csv.reader(fp, delimiter = ",", quotechar = '"')

for cell in reader:
    print(cell[0], cell[1], cell[2]) 
