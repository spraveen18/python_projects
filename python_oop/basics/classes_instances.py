#1  Classes and Instances 

class Employee:
    def __init__(self, first, last, pay):
        self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

    def fullname(self):
        return (f'{self.first} {self.last}')    

emp_1 = Employee('test1', 'user1', 50000)
emp_2 = Employee('test2', 'user2', 60000)


print(emp_1)
print(emp_2)

print(emp_1.fname)
# emp_1.first = 'test1'
# emp_1.last = 'user1'
# emp_1.email = 'test1.user1@company.com'
# emp_1.pay = 50000

# emp_2.first = 'test2'
# emp_2.last = 'user2'
# emp_2.email = 'test2.user2@company.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)


# emp_1 = Employee('test1', 'user1', 50000)
# emp_2 = Employee('test2', 'user2', 60000)


# print(emp_1)
# print(emp_2)


print(emp_1.email) 
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))

#output
# <__main__.Employee object at 0x7efcbcfef7b8> 
# <__main__.Employee object at 0x7efcbcfef7f0> 
# test1.user1@company.com 
# test2.user2@company.com 
# test1 user1 
# test2 user2 
# test1 user1 
# test2 user2
