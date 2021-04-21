from s2 import DataBase

db = DataBase()

db.insert_client(1, 'João')
db.insert_client(2, 'Maria')
db.insert_client(3, 'Fabrício')
db.insert_client(4, 'Ricardo')
db.insert_client(5, 'Julia')
db.insert_client(2, 'Clara')
db.insert_client(3, 'Riquelme')
db.insert_client(7, 'Maurício')

db.list_names()
print()
db.list_client()
db.drop_client(4)
db.list_names()
db.list_client()
print()
db.drop_client(2)
db.list_names()
db.list_client()