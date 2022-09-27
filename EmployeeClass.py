#This file creates a class named 'Employee'. 


class Employee: 

    def __init__(self, name, id_num, department, job_title, monthly_salary):
        self.__name = name
        self.__id_num = id_num
        self.__depart = department 
        self.__job_title = job_title 
        self.__monthly_salary = monthly_salary 
    
    def set_name(self, name):
        self.__name = name 

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_depart(self, depart):
        self.__depart = depart

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def set_job_title(self, monthly_salary):
        self.__monthly_salary = monthly_salary

    def get_name(self):
        return self.__name 

    def get_id_num(self):
        return self.__id_num

    def get_depart(self):
        return self.__depart

    def get_job_title(self):
        return self.__job_title
    
    def get_monthly_salary(self):
        return self.__monthly_salary