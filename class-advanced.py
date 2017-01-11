#customized decorator

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
# Wrap spam in a decorator object
print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))