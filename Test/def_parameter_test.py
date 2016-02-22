# -*- coding: UTF-8 -*-
#!/usr/bin/python
def printinfo ( arg1, *vartuple ):
#"打印任何传入的参数"
	print "输出: "
	#print  arg1
	for var in vartuple:
	    print var
	return;
printinfo( 10 )
printinfo(70,60,50)


