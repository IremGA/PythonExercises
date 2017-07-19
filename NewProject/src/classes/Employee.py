'''
Created on Jul 18, 2017

@author: iaktas
'''

class Employee(object):
    '''
    classdocs
    '''
    #global variable of class. Default is 0
    workedHours=0
    def __init__(self, name, surname, title, city, departmentName,sallaryPerDay):
        '''
        Constructor
            params:
                name 
                surname
                title
                city 
                departmentName 
            
        '''
        self.name=name
        self.surname=surname
        self.title=title
        '''Location Office or city '''
        self.city=city
        self.departmentName=departmentName
        self.sallaryPerDay=sallaryPerDay
    
    def getAnnualLeave(self, days):
        print "Hi %s ! Your %d days annual leave request has been sent to responsible person in the office" %(self.name,days)
    
    def getBusinessTravelRequest(self, toWhere):
        print "Hi %s %s ! Your business travel to %s has been taken " %(self.name, self.surname, toWhere)

    def getExpenseRequest(self, howMuch):
        print "Hi %s !Your expense request (%d TL) has been forwarded to responsible person. " %(self.name, howMuch)

    def bookWorkingHoursPerMonth_returnWorkedDays(self, hours_worked, hours_annualLeave, hours_sickLeave, hours_bankHoliday, hours_unpaid_leave):
        print "Hi %s ! Your working hours per week has been sent to responsible person."%(self.name)
        print "\t Worked Hours : %d" %hours_worked
        print "\t Annual Leave Hours: %d" %hours_annualLeave
        print "\t Sick Leave Hours: %d" %hours_sickLeave
        print "\t Bank Holiday Hours: %d" %hours_bankHoliday
        print "\t Unpaid Leave Hours: %d" %hours_unpaid_leave
        return 20-hours_unpaid_leave/8


