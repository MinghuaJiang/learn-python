import shelve
from oo import Person, Manager

bob = Person('Bob Smith')
# Re-create objects to be stored
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj

db.close()

db = shelve.open('persondb') # Reopen shelve with same filename
for key in sorted(db):
    print(key, '\t=>', db[key]) # Iterate to display database objects
sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue
for key in sorted(db):
    print(key, '\t=>', db[key])
db.close()
