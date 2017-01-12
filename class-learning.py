from abc import ABCMeta, abstractmethod

class Vector:
    __x = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2

#hidden attribute, will raise error
print v2._Vector__x

class Spam:
    def doit(self, message):
        print(message)

object1 = Spam()
x = object1.doit
x('hello world')

object1 = Spam()
t = Spam.doit
t(object1, 'howdy')


class Super():
    __metaclass__=ABCMeta
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass

# Default behavior
# Expected to be defined
class Inheritor(Super):
    pass # Inherit method verbatim

class Replacer(Super):
    def method(self):
        print('in Replacer.method') # Replace method completely

class Extender(Super):
    # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')
    # Fill in a required method

class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
    def method(self):
        "I am: spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)

class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

class Printer:
    def __init__(self, val):
        self.val = val

    def __repr__(self):        #__str__ is not suitable for nested case or interactive prompt
        return str(self.val)

class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

class Staticmethod:
    numInstances = 0
    # Use static method for class data
    def __init__(self):
        Staticmethod.numInstances += 1
    def printNumInstances():
        print("Number of instances: %s" % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)

class Classmethod:
    numInstances = 0

    # Trace class passed in
    def __init__(self):
        Classmethod.numInstances += 1

    def printNumInstances(cls):
        print("Number of instances: %s %s" % (cls.numInstances, cls))

    printNumInstances = classmethod(printNumInstances)

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
    klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
    y = Super()
    doc = spam()
    doc.method()
    index = Indexer()
    print index[2]

    objs = [Printer(2), Printer(3)]
    for x in objs: print(x)
    print (objs)

    x = Wrapper([1, 2, 3])
    x.append(4)
    print (x.wrapped)