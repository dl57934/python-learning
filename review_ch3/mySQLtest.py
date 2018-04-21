import MySQLdb

conn = MySQLdb.connect(
user = 'root',
passwd = 'dngmadl14',
host = 'localhost',
db='test')
cur = conn.cursor()
cur.execute('DROP TABLE fruits ')
cur.execute("CREATE TABLE fruits(id INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, price INTEGER)")

data =[('nana',22),('ba',24),('ap',25),('ple',26),('mel',28),('on',27)]
for Adata in data:
    cur.execute("INSERT INTO fruits(name,price) VALUES(%s,%s)",Adata)

cur.execute("SELECT * from fruits")
for item in cur.fetchall():
    print(item)
