import sqlite3
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)
cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;

CREATE TABLE items(itemID INTEGER PRIMARY KEY,name STRING UNIQUE ,price INTEGER);

INSERT INTO items(name,price)VALUES("사과","1000");
""")
conn.commit()

cur = conn.cursor()
cur.execute("SELECT itemID,name, price FROM items")
item_list = cur.fetchall()


for it in item_list:
    print(it)
