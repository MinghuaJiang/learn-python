import os
# Any Expression
str = raw_input("Enter your input: ")
print "Received input is : ", str

# Python Expression
str = input("Enter your input: ")
print "Received input is : ", str

fo = open("pickle.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
fo.close()

with open("pickle.txt", "wb") as fd:
    print "Name of the file: ", fd.name
    print "Closed or not : ", fd.closed
    print "Opening mode : ", fd.mode
    print "Softspace flag : ", fd.softspace

os.mkdir("test")
os.rmdir("test")
print(os.getcwd())
