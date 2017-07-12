'''
Created on Jul 11, 2017

Run with the command in Windows Powershell or any terminal : 
python C:\xx\Workspaces\PythonWS\NewProject\src\exercise9.py C:\xx\Workspaces\PythonWS\NewProject\ex8_sample.txt C:\xx\Workspaces\PythonWS\NewProject\ex9_sample.txt

@author: iaktas
'''
from sys import argv
from os.path import lexists

script, from_file, to_file = argv
print "Copying from %s to %s" %(from_file, to_file)

#we could do these two on one line too, how?
in_file = open(from_file)
indata=in_file.read()

print "The input file is %d bytes long" %len(indata)
print "Does the output file exist? %r" %lexists(to_file)

print "Ready, hit return to continue, CTRL+C to abort"
raw_input()

out_file = open(to_file, "w")
out_file.write(indata)

print "All Done!!"

out_file.close()
in_file.close()