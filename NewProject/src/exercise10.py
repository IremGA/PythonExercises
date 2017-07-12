'''
Created on Jul 12, 2017

@author: iaktas
'''
from sys import argv
from random import randint
import linecache


script, input_file=argv
current_file = open(input_file)

def print_all(f):
    print f.read();
    
def rewind(f):
    f.seek(0)
    
def total_characters_in_file(f):
    f.seek(0)
    len(f.read())

def print_number_of_characters_in_file(character_count,f):
    rewind(current_file)
    line =f.read(character_count)
    print line
    
def print_a_specific_line(line_number,f):
    line = linecache.getline(f, line_number)
    print "Read Line: %r" %line


print "Reading all lines in file %s" %(input_file)
print_all(current_file)

print "Rewinding ..."
rewind(current_file)

number_of_lines = len(current_file.readlines())

print "There are %d lines in the current file." %(number_of_lines)
print "Choosing random line number between 1 and %d ... "%(number_of_lines)

rand_line=randint(1,int(number_of_lines))

rewind(current_file)

print "Reading line number %d" %rand_line
print_a_specific_line(rand_line, input_file)

rewind(current_file)
number_of_chars= len(current_file.read())
print "Total character number in current file : %r" %number_of_chars

random_char_num = randint(1,int(number_of_chars))
print "Reading first %d characters in current file"%random_char_num
print_number_of_characters_in_file(random_char_num,current_file)

current_file.close()
