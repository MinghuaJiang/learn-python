try:
    print "hello world"
    raise RuntimeError
except RuntimeError:
    print "error handled"
finally:
    print "do finally"

