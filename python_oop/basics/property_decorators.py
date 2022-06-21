#6 property decorators - Getters, Setters, and Deleters

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):        # print(emp_1.email()) --> print(emp_1.email)
        return (f'{self.first}.{self.last}@email.com')
        
    @property                            #. print(emp_1.fullname()) ---> print(emp_1.fullname)
    def fullname(self):
        return (f'{self.first} {self.last}')
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None
    
    
emp_1 = Employee('john', 'cena')




"""
@fullname.deleter
emp_1.fullname = "chris gayle"

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)


output:
chris
chris gayle
chris.gayle@email.com
Delete name!
None
None None
None.None@email.com

"""

"""
@fullname.setter

emp_1.fullname = "chris gayle"
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

output:
chris
chris gayle
chris.gayle@email.com

"""


# print(emp_1.first)
# print(emp_1.fullname)
# print(emp_1.email)

# josh
# josh cena
# josh.cena@email.com






# print(emp_1.first)
# print(emp_1.fullname())
# print(emp_1.email())

# josh
# josh cena
# josh.cena@email.com


# emp_1.first = 'josh'

# print(emp_1.first)
# print(emp_1.fullname())
# print(emp_1.email)

#output
# josh
# josh cena
# john.cena@email.com

