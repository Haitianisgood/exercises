#coding=utf8
num = 9
if num >= 0 and num <= 10:
  print '0<x<10'
num = 10
if num < 0 or num > 10:
  print 'min 0 or max 10'
else:
  print 'undefine'
num = 8
if (num >= 0 and num <=5) or (num >= 10 and num <= 15):
  print '0<x<8 or 10<x<15'
else:
  print 'undefine'
