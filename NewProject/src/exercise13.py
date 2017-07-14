'''
Created on Jul 13, 2017
List, For/While Loops, Hash map
@author: iaktas
'''

'''languages_commonly_used is an array'''
languages_commonly_used = ['Javascript','Java','Python','C++','.Net']
index=0;

print "Top 5 programming languages commonly used : "
for language in languages_commonly_used:
    index=index+1
    '''To concatinate, int value must be convert to a string value'''
    print "Number "+str(index)+" is "+language
index=0

print "But I think that I should change my list according to latest GitHub news.."
languages_commonly_used.pop()
languages_commonly_used.pop()
languages_commonly_used.append('Rubby')
languages_commonly_used.append('PHP')


print "New list is :"
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

def age_average_in_the_meeting(employees_in_the_meeting):
    ages_in_the_meeting = employees_in_the_meeting['age']
    age_average_in_meeting = sum(ages_in_the_meeting)/len(ages_in_the_meeting)
    return age_average_in_meeting
    

print "The age average in the meeting was %d" %age_average_in_the_meeting(employees_in_the_meeting)

print "You can find participant info below : "
i=0
while i < len(employees_in_the_meeting['age']):
    name=employees_in_the_meeting['name'][i]
    age=employees_in_the_meeting['age'][i]
    title=employees_in_the_meeting['titles'][i]
    i=i+1
    print "\t Name: %s Age: %d Title: %s" %(name,age,title)

new_participants = {'name':['Aritra', 'Suddhashil', 'Anup'],
                    'age':[34,33,36],
                    'titles':['Senior Consultant', 'Senior Product Catalog Engineer', 'Product Development Engineer']} 


print "Then 3 more participants have been invited to solve an issue. The names of new participants are %s" %new_participants['name']

'''Adding new values in hash map'''
for key, value in employees_in_the_meeting.items():
    if key=='name':
        new_participants_name=new_participants['name']
        for name in new_participants_name:
            value.append(name)
        
    elif key=='age':
        new_participants_age=new_participants['age']
        value.append(new_participants_age[0])
        value.append(new_participants_age[1])
        value.append(new_participants_age[2])
        
    elif key=='titles':
        new_participants_titles=new_participants['titles']
        value.append(new_participants_titles[0])
        value.append(new_participants_titles[1])
        value.append(new_participants_titles[2])

print "The new employee list is %s" %employees_in_the_meeting['name']
print "Now the age average in the meeting is %d" %age_average_in_the_meeting(employees_in_the_meeting)