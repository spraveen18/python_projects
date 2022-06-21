#3  Regular methods and classmethods and staticmethods

class Employee:
    
    num_of_employee = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'
        
        Employee.num_of_employee += 1
        
    def fullname(self):
        return (f'{self.first} {self.last}')
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    
    @classmethod         
    def set_raise_amt(cls, amount):  # using cls(class as first argument instead of self(instance))
        cls.raise_amount = amount                          # common convention to use cls instead of class
    
    

            
emp_1 = Employee('test1', 'user1', 50000)
emp_2 = Employee('test2', 'user2', 60000)

Employee.set_raise_amt(1.05)

#emp_1.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

"""
output
1.05
1.05
1.05
"""

"""
class Employee:
    
    num_of_employee = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'
        
        Employee.num_of_employee += 1
        
    def fullname(self):
        return (f'{self.first} {self.last}')
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    
    @classmethod         
    def set_raise_amt(cls, amount):  
        cls.raise_amount = amount 
    
    
    @classmethod
    def from_string(cls, emp_str):           #class method as alternative constructor
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)
    
    
emp_1 = Employee('test1', 'user1', 50000)
emp_2 = Employee('test2', 'user2', 60000)


emp_str_1 = 'newuser-one-70000'
emp_str_2 = 'newuser-two-60000'
emp_str_3 = 'newuser-three-90000'

new_emp_1 = Employee.from_string(emp_str_1)

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)

output
newuser.one@company.com
70000
"""




"""class Employee:
    
    num_of_employee = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'
        
        Employee.num_of_employee += 1
        
    def fullname(self):
        return (f'{self.first} {self.last}')
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    
    @classmethod         
    def set_raise_amt(cls, amount):  
        cls.raise_amount = amount 
    
    
    @classmethod
    def from_string(cls, emp_str):           #class method as alternative constructor
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday()  == 5 or day.weekday() == 6:  #monday-0, tuesday-1,...,sunday-6
            return False
        else:
            return True


emp_1 = Employee('test1', 'user1', 50000)
emp_2 = Employee('test2', 'user2', 60000)
    
    
import datetime

my_date = datetime.date(2022, 6, 21)

print(Employee.is_workday(my_date))

output:
True
"""
