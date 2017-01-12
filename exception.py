try:
    print "hello world"
except RuntimeError:
    print "error handled"
else:
    print "no exception occurred"
finally:
    print "do finally"

