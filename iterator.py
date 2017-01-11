class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipObject2:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item
#necessary here if I would like to have a new iterator object each time when iter is called
class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def next(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
        return item

class Squares:
    # __iter__ + yield generator
    def __init__(self, start, stop):
    # __next__ is automatic/implied
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))
    for x in skipper:
        for y in skipper:
            print(x + y)