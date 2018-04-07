import pandas as pd

filename = "stat_104102.xlsx"

book = pd.read_excel(filename,sheet_name="Sheet0",header=2)

book = book.sort_values(by="2016")
print(book)
