'''
Created on Jul 13, 2017

@author: iaktas
'''

def split_string(str):
    str_prt=str.split(' ');
    return str_prt

def sort_string(str):
    return sorted(str)

def sort_string_reversed(str):
    return sorted(str,reverse=True)

def reverse_string(str):
    return str[::-1]

def get_first(str):
    str_prt=split_string(str)[0]
    return str_prt
    
def get_last(str):
    str_prt=split_string(str)[-1]
    return str_prt  
    
def sort_whole_string(str):
    str_prt=split_string(str)
    return sort_string(str_prt)

def sort_reversed_whole_string(str):
    str_prt=split_string(str)
    return sort_string_reversed(str_prt)

def print_first_and_last(str):
    '''Concatinating strings'''
    return get_first(str) + ' ' + get_last(str)

def make_string_uppercase(str):
    return str.upper()

    
str="Hi I am Claptrap. Recompiling my combat code!"

print("\n")
print(str)
print("\n")

print "Splitting my sentence: %s" %split_string(str)
print "Reversing my sentence: %s" %reverse_string(str)
print "Sorting characters in my sentence: %s" %sort_string(str)
print("\n")

print "Getting my first word : %r" %get_first(str)
print "Getting my last word: %r" %get_last(str)
print "Getting my first and last word: %s" %print_first_and_last(str)

print("\n")
print "Sorting words : %s" %sort_whole_string(str)
print "Reversing Sorted words : %s" %sort_reversed_whole_string(str)

print("\n")
print "Writing my sentence with upper case : %s" %make_string_uppercase(str)
print "Sorting upper case sentence: %s" %sort_whole_string(make_string_uppercase(str))
print "Reversing sorted upper case sentence: %s" %sort_reversed_whole_string(make_string_uppercase(str))

print("\n  Thank you for using Hyperion Robot Services !!! ")
