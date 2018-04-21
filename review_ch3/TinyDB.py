from tinydb import Query,TinyDB

filename = "test2.json"
db = TinyDB(filename)
db.purge_table('fruits')
table = db.table('fruits')

table.insert({'name':'사과','price':5000})
table.insert({'name':'바나나','price':7000})
table.insert({'name':'망고','price':8000})
table.insert({'name':'레몬','price':5500})

print(table.all())

item = Query()
res = table.search(item.name =='사과')
print(res[0]['name'])

res = table.search(item.price >6000)
for i in res:
    print ('-',i['name'],i['price'])



