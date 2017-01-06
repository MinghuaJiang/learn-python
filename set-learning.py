
engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers           # union
print employees
engineering_management = engineers & managers            # intersection
print engineering_management
fulltime_management = managers - engineers - programmers
print fulltime_management

engineers.add('Marvin')
print engineers
print employees
employees.update(engineers)
print employees

print engineers.issubset(employees)

print {1, 3, 2}

print {c * 4 for c in 'SPAM'}

keys = ["x","y","z"]
vals = [1,2,3]
print zip(keys,vals)

print {key: val for (key,val) in zip(keys, vals)}

print dict(zip(keys, vals))