#5 special methods(magic/dunder)   #dunder means __, so init surrounded by dunder

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
        self.pay = int(self.pay * self.raise_amount) 
        
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
        
        
    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('user1', 'one', 50000)
emp_2 = Employee('user2', 'two', 60000)




# print(len(emp_1))   #9


# print(len('test'))       #4
# print('test'.__len__())  #4

# print(emp_1 + emp_2)  #110000


# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__repr__())
# print(emp_1.__str__())

# output:
# user1 one - user1.one@company.com
# Employee('user1', 'one', '50000')
# user1 one - user1.one@company.com
# Employee('user1', 'one', '50000')
# user1 one - user1.one@company.com    
