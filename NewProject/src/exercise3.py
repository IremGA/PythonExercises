'''
Created on Jul 10, 2017

@author: iaktas
'''
from distutils.tests import here
from test.test_multiprocessing import _TestZZZNumberOfObjects
x="There are %d types of people. " %10
binary = "binary"
do_not="don't"
y="Those who know %s and those who %s" %(binary, do_not)

print x
print y
#use %r for debugging, since it displays the "raw" data of the variable, but we use s and others for displaying to users
print "I said : %r." %x
print "I also said : '%s'. "%y

hilarious=False
joke_evaluation="Isn't that joke so funny?! %s"

print joke_evaluation%hilarious

w="This is the left side of ..."
e="a string with a right side."

print w+e
print "*"*10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


days="Mon Tue Wed Thu Fri Sat Sun"
months="Jan\nFeb\nMar\nApr\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print "Here are the days : ", days
print "Here are the months : \n", months

print """MAny lines of prints are here 
with 3 double-quota 
xxxx
yyy
_TestZZZNumberOfObjects
"""

#while True:
#   for i in ["/","-","|","\\","|"]:
#       print "%s\r"%i,  



