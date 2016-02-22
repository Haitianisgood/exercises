#!/usr/bin/python
import time;
import calendar


ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:",ticks

localtime = time.localtime(time.time())
print "Local current time:",localtime

localtimeg = time.asctime( time.localtime(time.time()) )
print "Local current time:",localtimeg

cal = calendar.month(2015,8)
print "Here is the calendar:"
print cal
