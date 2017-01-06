import operator
#scope
x = 1

def scope_test():
    global x
    print x
    x = 2
    print x

scope_test()
#argument matching
def test(length,width, size=1, *vargs, **kargs):
    print "test"
a = []
b = {}
test(1, width=2, *a, **b)
#anonymous function
sum = lambda arg1, arg2: arg1 + arg2
print "Value of total : ", sum(10, 20)

#recursion
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot
#bfs
def sumtree_bfs(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot

#dfs
def sumtree_dfs(L):
    tot = 0
    items = list(L)
    print items
    print items
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))
print(sumtree_bfs(L))
print(sumtree_dfs(L))

#functional objects
def echo(message):
    print(message)

x = echo
x('Indirect call!')

#function introspection
print (echo.__name__)

print (dir(echo))
#functional programming
counters = [1, 2, 3, 4]

def inc(x): return x + 10

print(map(inc, counters))
print(map((lambda x: x + 3), counters))
print(map(pow, [1, 2, 3], [2, 3, 4]))

print(filter((lambda x: x > 0), range(-5, 5)))
print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))
print(reduce(operator.add, [1, 2, 3, 4]))

#comprehension
res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print res
print([x ** 2 for x in range(10) if x % 2 == 0])
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
#generator function

def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print(i)

y = gensquares(5)
print next(y)
print next(y)

#generator expression
#generator itself is the iterator
G = (c * 4 for c in 'SPAM')
print(iter(G) is G)

iter(G) is G
I1 = iter(G)
I2 = iter(G)

print next(I1)
print next(I2)

L = [1, 2, 3, 4]

I1, I2 = iter(L), iter(L)

print next(I1)
print next(I2)

def f(a, b, c):
    print('%s, %s, and %s' % (a, b, c))

f(*(i for i in range(3)))
