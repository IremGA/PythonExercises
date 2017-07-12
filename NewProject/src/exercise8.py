'''
Created on Jul 10, 2017

@author: iaktas
'''
from sys import argv
from __builtin__ import raw_input

script, filename = argv

print "We're going to erase %r. " %filename
print "To quit, hit CTRL+C... "
print"To continue, hit RETURN"

raw_input("Which one? > ")

print "Opening the file... "
target = open(filename,'wb+')

print "The content of the file is : \n"


print"Truncating the file. Goodbye!"
target.truncate()

print"Now re-creating the file content... "
line1=raw_input("line 1: \n > ")
line2=raw_input("line 2: \n > ")
line3=raw_input("line 3: \n > ")

print "Writing 3 lines to the file... "

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "The latest content of the file is : ", 
print target.read()

print "Closing the file"
target.close()
