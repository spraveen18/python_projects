#4 Inheritance - Creating Subclasses

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
        

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)       #super() used to give access to methods and properties of a parent or sibling class
        #Employee(self, first, last, pay)  # also use this instead of super
        self.prog_language = prog_language
        
#dev_1 = Employee('developer1', 'one', 50000)

dev_1 = Developer('developer1', 'one', 50000)  # by changing raise amt in subclass it didn't have any effect on our
dev_2 = Developer('developer2', 'two', 60000)  # Employee instances    

# print(dev_1.email)       # --> developer1.one@company.com                             
# print(dev_2.email)       # --> developer2.two@company.com

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


#print(help(Developer))




"""

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)       #super() used to give access to methods and properties of a parent or sibling class
        #Employee(self, first, last, pay)  # also use this instead of super
        self.prog_language = prog_language
            
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):  #never pass mutable arguments like lists or dict. as default arguments 
        super().__init__(first, last, pay)       
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
             self.employees.append(emp)
               
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())
        
#dev_1 = Employee('developer1', 'one', 50000)

dev_1 = Developer('developer1', 'one', 50000, 'Python')  # by changing raise amt in subclass it didn't have any effect on our
dev_2 = Developer('developer2', 'two', 60000, 'Java')  # Employee instances 


mgr_1 = Manager('manager1', 'one', 90000, [dev_1])

print(mgr_1.email)   # ouput ---->  manager1.one@company.com


# mgr_1.print_emps()  # ---> developer1 one

# mgr_1.add_emp(dev_2)

# mgr_1.print_emps()   #---> developer1 one
#                      #---> developer2 two

    
     
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()      # ---> developer2 two


# print(isinstance(mgr_1, Manager))       # True  
# print(isinstance(mgr_1, Employee))      # True
# print(isinstance(mgr_1, Developer))     # False



print(issubclass(Developer, Employee))   
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

#output
# True
# True
# False

"""
