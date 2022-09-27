#this program will create the Payroll class 

class PayrollDeduction: 
    
    def __init__(self, desc, date, charge_amt, employee_id):
        self.__desc = desc
        self.__date = date
        self.__charge_amt = charge_amt
        self.__employee_id = employee_id

    
    def set_desc(self, desc):
        self.__desc = desc

    def set_date(self, date):
        self.__date = date
    
    def set_charge_amt(self, charge_amt):
        self.__charge_amt = charge_amt
    
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_desc(self):
        return self.__desc

    def get_date(self):
        return self.__date

    def get_charge_amt(self):
        return self.__charge_amt 
    
    def get_employee_id(self):
        return self.__employee_id
    
