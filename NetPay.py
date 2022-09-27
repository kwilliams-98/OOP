#you need to hardcode everything instead of using the inputs!

import PayrollDeductionClass as pdc
import EmployeeClass as ec

def main():

    #get information about the employee 

    name = input('Enter Employee Name:')
    employee_id_num = input ('Enter Employee ID Number:')
    depart = input('Enter Employee Department:')
    job_title = input('Enter Employee Job Title')
    monthly_salary = float(input ('Enter Employee Salary'))

    #create an instance of the employee object (should be called Jimmy Smith )
    
    employee = ec.Employee(name, employee_id_num, depart, job_title, monthly_salary)

    #should create 5 instances of the employee ID








main()