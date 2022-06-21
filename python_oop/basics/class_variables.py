class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

    def fullname(self):
        return (f'{self.first} {self.last}')
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) # int(self.pay * self.raise_amount) calling through self instance
                                                          #using self allows changing values for individual   
    
emp_1 = Employee('test1', 'user1', 50000)
emp_2 = Employee('test2', 'user2', 60000)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


#output
#50000
#52000




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
        self.pay = int(self.pay * Employee.raise_amount) 
                                                         

print(Employee.num_of_employee)            
            
emp_1 = Employee('test1', 'user1', 50000)
emp_2 = Employee('test2', 'user2', 60000)

print(Employee.num_of_employee)


#Employee.raise_amount = 1.05

# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)




# print(emp_1.__dict__)  #{'first': 'test1', 'last': 'user1', 'pay': 50000, 'email': 'test1.user1@company.com'}

print(Employee.__dict__)  

#0utput
# {'__module__': '__main__', 'raise_amount': 1.04, 
# '__init__': <function Employee.__init__ at 0x7efcbce5b730>, 
# 'fullname': <function Employee.fullname at 0x7efcbce5b6a8>, 
# 'apply_raise': <function Employee.apply_raise at 0x7efcbce5b620>,
# '__dict__': <attribute '__dict__' of 'Employee' objects>, 
# '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
