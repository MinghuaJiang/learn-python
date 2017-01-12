#customized decorator

#class decotrator can only be used on function insteaed of class method
class tracer:
    def __init__(self, func):
    # Remember original, init counter
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        # On later calls: add logic, run original
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)

@tracer
def spam(a, b, c):
    return a + b + c # Same as spam = tracer(spam)

def tracer2(func):
    # Remember original
    def oncall(*args):
    # On later calls
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer2
    def spam(self, a, b, c): return a + b + c

@tracer2
def spam2(a, b, c):
    return a + b + c

# Wrap spam in a decorator object
print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))

x = C()
print(x.spam(1, 2, 3))
print(x.spam('a', 'b', 'c'))

class Person:
# Add (object) in 2.X
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")


#Person created with decorator, the same as Person class actually
class Person2:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        "name property docs"
        print('fetch...')
        return self._name
    @name.setter
    def name(self, value):
        print('change...')
        self._name = value
    @name.deleter
    def name(self):
        print('remove...')
        del self._name

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)

del bob.name
print('-'*20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)
