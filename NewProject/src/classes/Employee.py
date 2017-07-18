'''
Created on Jul 18, 2017

@author: iaktas
'''

class Employee(object):
    '''
    classdocs
    '''


    def __init__(self, name, surname, title, city, departmentName,sallaryPerDay):
        '''
        Constructor
        '''
        self.name=name
        self.surname=surname
        self.title=title
        '''Office or city '''
        self.city=city
        self.departmentName=departmentName
        self.sallaryPerDay=sallaryPerDay
    
def getAnnualLeave(days):
    print "Your %d annual leave request has been sent to responsible person in the office" %days
    
def getBusinessTravelRequest(toWhere):
    print "Your business travel to %s has been taken " %toWhere

def getExpenseRequest(howMuch):
    print "Your expense request (%d TL) has been forwarded to responsible person. " %howMuch

def bookWorkingHoursPerWeek(hours_worked, hours_annualLeave, hours_sickLeave, hour_bankHoliday):
    print "Your working hours per week has been sent to responsible person."
    print "Worked Hours : %d" %hours_worked
    print "Annual Leave Hours: %d" %hours_annualLeave
    print "Sick Leave Hours: %d" %hours_sickLeave
    print "Bank Holiday Hours: %d" %hour_bankHoliday

