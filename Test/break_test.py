#!/usr/bin/python
for letter in 'Python':
  l = 1
  if letter == 'h':
    break
  print 'Current Letter:',letter

var = 10
while var > 0:
  print 'Current variable value:',var
  var = var -1
  if var == 5:
    break

var = var + 1
l = l + 2
print 'Last changed variable value:',l
print 'Last changed variable value:',var
print "Good bye!"
