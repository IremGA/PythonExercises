'''
Created on Jul 19, 2017

@author: iaktas
'''

import Employee
import Department
from __builtin__ import int, str
from datetime import datetime

employeeIrem = Employee.Employee("Irem", "Aktas","Software Engineer", "Istanbul", "Real Time Charging & Billing","250")
employeeKutyar = Employee.Employee("Kutyar", "Oztas","Sr Test Engineer", "Istanbul", "Real Time Charging & Billing","350")
employeeDavid = Employee.Employee("David", "Daryl","Technical Architect", "Istanbul", "Real Time Charging & Billing","450")
employeeAbdullah = Employee.Employee("Abdullah", "Serin","Solution Architect", "Istanbul", "Real Time Charging & Billing","450")
employeeBulent= Employee.Employee("Bulent", "Tatli","Project Manager", "Istanbul", "Real Time Charging & Billing","500")
employeeRaphael = Employee.Employee("Raphael", "Chucky", "Sales Director", "Canada", "Sales","650")
employeeMelahat =Employee.Employee("Melahat", "Garden", "Sales Manager", "Canada", "Sales","600")

employeeIrem.getAnnualLeave(5) 
employee_irem_workedHours = employeeIrem.bookWorkingHoursPerMonth_returnWorkedHours(16*8, 8, 8, 8, 8)
employeeIrem.workedHours = employee_irem_workedHours

employeeAbdullah.getBusinessTravelRequest("Canada")
employeeKutyar.getExpenseRequest(100)

departmentCCProjects = ["Turk Telekom Single Rating","Astelit Gold", "Best Gold", "Turk Telekom Gold"]
departmentSalesProjects= departmentCCProjects
departmentSalesProjects.append("Vodafone India")
departmentSalesProjects.append("Vodacom South Africa")
departmentSalesProjects.append("Claro Peru")
departmentCustomerCare=Department.Department(employeeIrem.departmentName, True, departmentCCProjects)
departmentSales=Department.Department(employeeRaphael.departmentName, True, departmentSalesProjects)
departmentHumanResourcesProjects=[departmentCCProjects[0],departmentCCProjects[3],departmentSalesProjects[6]]
departmentHumanResources = Department.Department("Human Resources", True, departmentHumanResourcesProjects)

singleRatingProjectMemebers=[employeeBulent,employeeAbdullah,employeeDavid,employeeKutyar,employeeIrem]
departmentCustomerCare.createEmployeeGroupforProject(departmentCCProjects[0], singleRatingProjectMemebers)

print("Human Resources Department in Istanbul office is responsible for %s projects in this term"%departmentHumanResources.projects)

astelitProjectMemebers = [employeeIrem, employeeDavid]
departmentCustomerCare.createEmployeeGroupforProject(departmentCCProjects[1], astelitProjectMemebers)

class HumanResources(object):
    def __init__(self,location):
        self.location=location
    
    def increaseEmployeeSalary(self,employee,ratio):
        increased_amount = int(employee.sallaryPerDay)+int(employee.sallaryPerDay)*ratio/100
        employee.sallaryPerDay = str(increased_amount)
        print ("Sallary Per Day info has been updated for "+employee.name+" "+employee.surname+". "+employee.sallaryPerDay+" will be paid after "+str(datetime.now().strftime('%b'))+"/"+str(datetime.now().strftime('%y')) )
         
    def payMonthlySallaryOfEmployee(self,employee):
        sallary_amount= employee.workedHours*int(employee.sallaryPerDay)
        print str(sallary_amount)+" TL Sallary has been paid to "+employee.name+" "+employee.surname+" on "+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+". by %s location"%(self.location) 
            

humanResources = HumanResources("Istanbul")
humanResources.payMonthlySallaryOfEmployee(employeeIrem) 
humanResources.increaseEmployeeSalary(employeeDavid,10)        