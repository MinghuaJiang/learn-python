import time
import calendar


ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

print "Local current formatted time directly:", time.ctime(ticks)

localtime = time.localtime(ticks)
print "Local current time:", localtime


formatted_time = time.asctime(localtime)
print "Local formatted current time :", formatted_time

print "cpu current time: ", time.clock()

def timer(func, *args):
    start = time.clock()
    for i in range(1000):
        func(*args)
    return time.clock() - start

time.sleep(2)

print time.timezone
print time.tzname
cal = calendar.month(2017, 1)
print "Here is the calendar:"
print cal
print calendar.isleap(2016)
print calendar.weekday(2017,1,3)
