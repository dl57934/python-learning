import MySQLdb

con = MySQLdb.connect(
user = 'root',
passwd='dngmadl14',
host='localhost',
db='test'
)
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute('''CREATE TABLE items (id INTEGER PRIMARY KEY AUTO_INCREMENT, 
name TEXT ,
price INTEGER)''')
data =[('banana',3000),('apple',4000),('orange',5000)]

cur.executemany("INSERT INTO items(name,price) VALUES(%s,%s)",data)

cur.execute("SELECT * FROM items")

list_data = cur.fetchall()
for a in list_data:
    print(a)
