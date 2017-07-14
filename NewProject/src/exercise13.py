'''
Created on Jul 13, 2017
List, For/While Loops, Hash map
@author: iaktas
'''

'''languages_commonly_used is an array'''
languages_commonly_used = ['Javascript','Java','Python','C++','.Net']
index=0;

print "Top 5 languages commonly used : "
for language in languages_commonly_used:
    index=index+1
    '''To concatinate, int value must be convert to a string value'''
    print "Number "+str(index)+" is "+language

print ""    
'''Hash map key: string, value: array list'''
employees_in_the_meeting={'name':['David', 'Bulent', 'Abdullah', 'Raphael','Kutyar','Irem'], 
                          'age':[42,40,38,50,35,29], 
                          'titles':['System Architect','Project Manager','Solution Architect', 
                                    'Sales Director', 'System Test Engineer','Product Development Engineer']}

print "There were 6 participants in yesterday's meeting. The names of participants are : %s" %employees_in_the_meeting['name']

ages_in_the_meeting = employees_in_the_meeting['age']
age_average_in_meeting = sum(ages_in_the_meeting)/len(ages_in_the_meeting)

print "The age average in the meeting was %d" %age_average_in_meeting

print "You can find participant info below : "
i=0
while i < len(ages_in_the_meeting):
    name=employees_in_the_meeting['name'][i]
    age=employees_in_the_meeting['age'][i]
    title=employees_in_the_meeting['titles'][i]
    i=i+1
    print "\t Name: %s Age: %d Title: %s" %(name,age,title)

   

