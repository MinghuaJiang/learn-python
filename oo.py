class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

    def __str__(self):
        return u'%s %s' % (self.name, self.salary)


    def displayCount(self):
        print "Total Employee %d" % Employee.empCount


    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
print emp1
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

class AttrDisplay:

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

    def someThingElse(self):
        pass

class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)

class PrivateExc(Exception): pass
class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value

class Test1(Privacy):
    privates = ['age']
class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

if __name__ == '__main__':
    bob = Person('Bob Smith')
    # Test the class
    sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    # Use the new methods
    sue.giveRaise(.10)
    # instead of hardcoding
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    tom.someThingElse()
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
    x = Test1()
    y = Test2()
    x.name = 'Bob'
    # y.name = 'Sue'
    print(x.name)  # Works
    # Fails
    y.age = 30
    # x.age = 40
    print(y.age)  # Works
    # Fails
