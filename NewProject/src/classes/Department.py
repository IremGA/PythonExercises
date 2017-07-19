'''
Created on Jul 18, 2017

@author: iaktas
'''

class Department(object):
    '''
    classdocs
    '''

    def __init__(self, name, isActive, projects):
        '''
        Constructor
            params:
                name, isActive,projects
        '''
        self.name=name
        self.isActive=isActive
        self.projects=projects
        
    def createEmployeeGroupforProject(self, projectName, employees):
        print("\n Here is the "+projectName+" project members in "+self.name+" department: ")
        for employee in employees:
            print("\t "+employee.name+" "+employee.surname)
        
    