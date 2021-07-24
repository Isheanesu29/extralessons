
# Classes' helps us logically group our data and functions for ease and usability to easily use our data functions

class Employee:
    pass # pass is used to tell the compile that this is an empty class


emp_1 = Employee() # the two brackets are the constructor. This how you create an instance of a class
emp_2 = Employee() # both of these instances occupy different places in the memory
print(emp_1)
print(emp_2)

emp_1.firstName = 'Ishe'
emp_1.lastName = 'Murwira'
emp_1.salary = 20000
emp_1.emailAdress = 'imurwira@yahoo.com'

emp_2.firstName = 'John'
emp_2.lastName = 'Jamerson'
emp_2.salary = 25000
emp_2.emailAdress = 'jjamerson@yahoo.com'

print(emp_1.emailAdress)
print(emp_2.salary)

