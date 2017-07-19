'''
Created on Jul 19, 2017

@author: iaktas
'''

import Employee
import Department
from __builtin__ import int, str
from datetime import datetime

#Create Employees
employeeIrem = Employee.Employee("Irem", "Aktas","Software Engineer", "Istanbul", "Real Time Charging & Billing","250")
employeeKutyar = Employee.Employee("Kutyar", "Oztas","Sr Test Engineer", "Istanbul", "Real Time Charging & Billing","350")
employeeDavid = Employee.Employee("David", "Daryl","Technical Architect", "Istanbul", "Real Time Charging & Billing","450")
employeeAbdullah = Employee.Employee("Abdullah", "Serin","Solution Architect", "Istanbul", "Real Time Charging & Billing","450")
employeeBulent= Employee.Employee("Bulent", "Tatli","Project Manager", "Istanbul", "Real Time Charging & Billing","500")
employeeRaphael = Employee.Employee("Raphael", "Chucky", "Sales Director", "Canada", "Sales","650")
employeeMelahat =Employee.Employee("Melahat", "Garden", "Sales Manager", "Canada", "Sales","600")

''' do something for Irem Aktas'''
employeeIrem.getAnnualLeave(5) 

'''arrange booking hours of Irem and convert worked hours in day format'''
employee_irem_workedHours = employeeIrem.bookWorkingHoursPerMonth_returnWorkedDays(16*8, 8, 8, 8, 8)
'''assign worked days to global variable of Employee class'''
employeeIrem.workedHours = employee_irem_workedHours

'''arrange a request for Employee Abdullah'''
employeeAbdullah.getBusinessTravelRequest("Canada")

'''arrange a request for Employee Kutyar'''
employeeKutyar.getExpenseRequest(100)

#append projects
departmentCCProjects = ["Turk Telekom Single Rating","Astelit Gold", "Best Gold", "Turk Telekom Gold"]
departmentSalesProjects= departmentCCProjects
departmentSalesProjects.append("Vodafone India")
departmentSalesProjects.append("Vodacom South Africa")
departmentSalesProjects.append("Claro Peru")
departmentHumanResourcesProjects=[departmentCCProjects[0],departmentCCProjects[3],departmentSalesProjects[6]]


#Create department objects: Customer Care, Sales and Human Resources
departmentCustomerCare=Department.Department(employeeIrem.departmentName, True, departmentCCProjects)
departmentSales=Department.Department(employeeRaphael.departmentName, True, departmentSalesProjects)
departmentHumanResources = Department.Department("Human Resources", True, departmentHumanResourcesProjects)

print("Human Resources Department in Istanbul office is responsible for %s projects in this term"%departmentHumanResources.projects)

#Assign members to the certain project/s in the department
singleRatingProjectMemebers=[employeeBulent,employeeAbdullah,employeeDavid,employeeKutyar,employeeIrem]
departmentCustomerCare.createEmployeeGroupforProject(departmentCCProjects[0], singleRatingProjectMemebers)

astelitProjectMemebers = [employeeIrem, employeeDavid]
departmentCustomerCare.createEmployeeGroupforProject(departmentCCProjects[1], astelitProjectMemebers)

salesMembers = [employeeRaphael, employeeMelahat, employeeBulent,employeeAbdullah]
departmentSales.createEmployeeGroupforProject(departmentSalesProjects[0]+" and "+departmentSalesProjects[3], salesMembers)

#Class Creation for Human Resources
class HumanResources(object):
    def __init__(self,location):
        self.location=location
        
    '''increases salary of an employee with given ratio then assigns new salary value to employee'''
    def increaseEmployeeSalary(self,employee,ratio):
        increased_amount = int(employee.sallaryPerDay)+int(employee.sallaryPerDay)*ratio/100
        #assigning new value to employee
        employee.sallaryPerDay = str(increased_amount)
        print ("Salary Per Day info has been updated for "+employee.name+" "+employee.surname+". "+employee.sallaryPerDay+" will be paid after "+str(datetime.now().strftime('%b'))+"/"+str(datetime.now().strftime('%y')) )
         
    def payMonthlySalaryOfEmployee(self,employee):
        #calculate monthly salary
        sallary_amount= employee.workedHours*int(employee.sallaryPerDay)
        print str(sallary_amount)+" EUR Salary has been paid to "+employee.name+" "+employee.surname+" on "+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+". by %s location"%(self.location) 
            
#Create a human resources object
humanResources = HumanResources("Istanbul")
humanResources.payMonthlySalaryOfEmployee(employeeIrem) 
humanResources.increaseEmployeeSalary(employeeDavid,10)        