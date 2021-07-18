



class Employee:

    def __init__(self,firstName,lastName,salary,gender=None): # None helps to declare a optional parameter, not mandatory 
        self.first = firstName  # self represents this class, the instance of this class
        self.last = lastName
        self.pay = salary
        self.email = firstName + '.' + lastName + '@gmail.com'
        self.gen = gender
    
    def fullName(self):
        return f'{self.first,self.last}'
    
    def employeeEmail(self):
        return f'{self.email}'

    def employeeGender(self):
        return f'The gender of this emmploee is: {self.gen}'



emp_1 = Employee('Ishe','Murwira',20000)
emp_2 = Employee('John','Jamerson',25000,'Male')
emp_3 = Employee ('Susan','Rusike',15000,'Female')

print(emp_1.pay)
print(emp_2.employeeEmail())
print(emp_3.fullName())