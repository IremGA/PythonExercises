'''
Created on Jul 13, 2017

@author: iaktas
'''
from __builtin__ import raw_input
from xmlrpclib import boolean
print "Please give answers as 'yes' or 'no' \n"
print """ 

Booting sequence complete. ,
Hello! I am your new steward bot. 
Designation: CL4P-TP, Hyperion Robot, Class C. 
Please adjust factory settings to meet your needs before deployment.

"""

print "Finally! Can you hear me? What do you remember?"

boolean_val = raw_input(">")

if boolean_val.lower()=="yes":
    print "Yes. Remember what? Are... are you my father?"
    is_my_father=raw_input(">")
    if is_my_father.lower()=="yes":
        print "Wheeeee! My Daddy !! I'm flying! I'm really flying!"
    elif is_my_father.lower()=="no":
        print "Are you god? Am I dead?"
        is_god=raw_input(">")
        if is_god.lower()=="yes":
            print "I'M DEAD I'M DEAD OHMYGOD I'M DEAD!..Anyway..Let's get this party started!"
        elif is_god.lower()=="no":
            print "Thanks for giving me a second chance, God. I really appreciate it."
        else :
            print "What?? I didn't get your answer..Badass?! Aaahhh! Save me from the Badass!"
    else :
        print "What?? I didn't get your answer..Badass?! Aaahhh! Save me from the Badass!"
elif boolean_val.lower()=="no":  
    print "The robot is dead, long live the robot! Don't forget me!"    
else :
    print "What?? I didn't get your answer..Badass?! Aaahhh! Save me from the Badass!"