from tinydb import TinyDB, Query
filepath = 'test.json'
db = TinyDB(filepath)
db.purge_table('fruits')
table = db.table('fruits')
table.insert({'name':'apple','price':3000})
table.insert({'name':'peach','price':4000})

print(table.all())
item = Query()
res = table.search(item.name == 'apple')

print(res[0]['price'])

res = table.search(item.price >=3000)
for a in res:
    print (a['name'],a['price'])
