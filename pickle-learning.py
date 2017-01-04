import pickle

try:
    with open('pickle.txt', 'wb') as pickleFile:
        pickle.dump(['a', 'b', 'c'], pickleFile)
    with open('pickle.txt', 'rb') as pickleRead:
        print(pickle.load(pickleRead))
except IOError:
    pass
