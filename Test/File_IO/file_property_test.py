# -*- coding: UTF-8 -*-
#!/usr/bin/python
fo = open("foll.txt","wb")
print "Name of the file:", fo.name
print "Closed or not:", fo.closed
print "Opening mode:",fo.mode
print "Softspace flag:",fo.softspace
fo.close()
