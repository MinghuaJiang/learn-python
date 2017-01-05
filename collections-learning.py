from collections import Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict

c = Counter()
print c
c = Counter('gallahad')
print c
c = Counter({'red': 4, 'blue': 2})
print c
c = Counter(cats=4, dogs=8)
print c
c = Counter(['apple', 'banana'])
print c
print(c.elements())
print(c.most_common(1))

d = deque('ghi')
print d
d.append('j')
print d
d.appendleft('ab')
print d
print d.pop()
print d.popleft()

d.extend('jkl')
print d
d.rotate(1)
print d
d.rotate(-1)
print d
d.extendleft('123')
print d


def tail(filename, n=10):
    'Return the last n lines of a file'
    return deque(open(filename), n)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print d.items()

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

dict = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print dict

dict2 = OrderedDict()
dict2['a'] = 'A'
dict2['c'] = 'C'
dict2['b'] = 'B'
dict2['d'] = 'D'
dict2['e'] = 'E'

print dict2
