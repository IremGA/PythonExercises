'''
Created on Jul 10, 2017

@author: iaktas
'''
from __builtin__ import raw_input

print "How old are you?",
age=raw_input()
print"How tall are you (cm)? ", 
height=raw_input()
print "How much do you weight (kg)? ",
weight=raw_input()

print "The result is you %r years old, your height is %r cm, your weight is %r kg" %(
    age,height,weight)



'''
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)
'''