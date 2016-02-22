# -*- coding: UTF-8 -*-
#!/usr/bin/python
fo = open("/tmp/foo.txt","r+")
#fo.write ("Python is a great language.\nYeah its great!!\n")
str = fo.read(10)
print "Read String is :",str
fo.close()
