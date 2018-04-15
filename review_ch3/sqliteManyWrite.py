import sqlite3

filename = "test2.sqlite"
conn = sqlite3.connect(filename)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS fruits")
cur.execute("CREATE TABLE fruits (id INTEGER PRIMARY KEY, name STRING UNIQUE, price INTEGER)")

data = [("오렌지",5000),("망고",4000),("사과",2000),("복숭아",1000),("애플망고",5000)]
#인자는 ?로 받는다.
cur.executemany("INSERT INTO fruits(name,price) VALUES(?,?)",data)

conn.commit()
cur = conn.cursor()
priceRange =(4000,6000)
#조건식 부여
cur.execute("SELECT * FROM fruits WHERE price > ? AND price <? ",priceRange)
itemList = cur.fetchall()
for item in itemList:
    print (item)

