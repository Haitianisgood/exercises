# -*- coding: UTF-8 -*-
#!/usr/bin/python

class Parent:
	def myMethod(self):
		print "print parent method"
class Child(Parent):
	def myMethod(self):
		print "print child method"
c = Child()
c.myMethod()
