import pandas as pd 

filename = "stat_104102.xlsx"

book = pd.read_excel("popular2.xlsx",sheet_name = "Sheet0",header = 2)

print(book)
