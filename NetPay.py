import PayrollDeductionClass as pdc
import EmployeeClass as ec

def main():

    #get information about the employee 

    name = 'Jimmy Smith'
    employee_id_num = '58475'
    depart = 'Information Systems'
    job_title = 'Developer'
    monthly_salary = 6800.00

    #create an instance of the employee object (should be called Jimmy Smith )
    
    JimmySmith = ec.Employee(name, employee_id_num, depart, job_title, monthly_salary)

    #should create 5 instances of the employee ID

    desc = 'Food Court'
    date = '8/14/2022'
    charge_amt = 22.50
    employee_id = '39119'

    FoodCourt1 = pdc.PayrollDeduction(desc, date, charge_amt, employee_id)

    desc = 'Gift Contribution'
    date = '8/12/2022'
    charge_amt = 25.00
    employee_id = '58475'

    GiftCont = pdc.PayrollDeduction(desc, date, charge_amt, employee_id)

    desc = 'Food Court'
    date = '8/17/2022'
    charge_amt = 15.25
    employee_id = '21547'

    FoodCourt2 = pdc.PayrollDeduction(desc, date, charge_amt, employee_id)

    desc = 'Vending Machine'
    date = '8/22/2022'
    charge_amt = 3.00
    employee_id = '58475'

    VendingMachine1 = pdc.PayrollDeduction(desc, date, charge_amt, employee_id)

    desc = 'Vending Machine'
    date = '8/05/2022'
    charge_amt = 2.75
    employee_id = '58475'

    VendingMachine2 = pdc.PayrollDeduction(desc, date, charge_amt, employee_id)

    #ifs 

    deduction = 0

    if FoodCourt1.get_employee_id() == JimmySmith.get_id_num(): 
        deduction += FoodCourt1.get_charge_amt() 
    if GiftCont.get_employee_id() == JimmySmith.get_id_num():
        deduction += GiftCont.get_charge_amt()
    if FoodCourt2.get_employee_id() == JimmySmith.get_id_num():
        deduction += FoodCourt2.get_charge_amt()
    if VendingMachine1.get_employee_id() == JimmySmith.get_id_num():
        deduction += VendingMachine1.get_charge_amt()
    if VendingMachine2.get_employee_id() == JimmySmith.get_id_num():
        deduction += VendingMachine2.get_charge_amt()
    
    #final output
    
    print('*** Employee Pay ***')
    print('Name:', JimmySmith.get_name())
    print('ID Number:', JimmySmith.get_id_num())
    print('Department:', JimmySmith.get_depart())
    print('Gross Pay: $', format(JimmySmith.get_monthly_salary(), ',.2f'), sep='')
    GrossPay = float(JimmySmith.get_monthly_salary())
    NetPay = GrossPay - deduction
    print('Net Pay: $', format(NetPay, ',.2f'), sep='')

main()