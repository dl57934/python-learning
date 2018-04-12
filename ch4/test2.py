import sqlite3

filename = "test.sqlite"
con  = sqlite3.connect(filename)
cur = con.cursor()
cur.executescript("""
DROP TABLE IF EXISTS ITEMS;
CREATE TABLE items(id INTEGER PRIMARY KEY, name TEXT UNIQUE , price INTEGER);
""")
data = [("MANGO",7700),("KIWI",4000),("Grape",8000),("Peach",9400),("Permission",7000),("Bannana",4000)]
con.commit()
cur =con.cursor()
cur.executemany("INSERT INTO items(name,price)VALUES(?,?)",data)
con.commit()
data = (4000,7000)
cur.execute("SELECT *  FROM items WHERE price >= ? and price <= ?",data)
fr_list = cur.fetchall()

for fr in fr_list:
    print(fr)





