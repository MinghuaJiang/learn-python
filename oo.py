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
print v2.__x