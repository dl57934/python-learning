import csv, codecs 

filename = "solo.csv"

with codecs.open(filename, "w", "euc_kr") as fp:
    writer = csv.writer(fp,delimiter=",",quotechar="'")
    writer.writerow(["name","id","pw"])
    writer.writerow(["asd","qwe","www"])
