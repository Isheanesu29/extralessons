


class Employee:

    raise_amountGlobal = 15.003 # that is a global variable
    gmail = '@gmail.com'

    def __init__(self,firstName,lastName,salary,gender=None): # None helps to declare a optional parameter, not mandatory 
        self.first = firstName  # self represents this class, the instance of this class
        self.last = lastName
        self.pay = salary
        self.email = firstName + '.' + lastName + self.gmail # always use self to access the instances of that file
        self.gen = gender
    
    def apply_raiseLocal(self):
        raise_amountLocal = 10.002
        new_pay = int(self.pay + raise_amountLocal) # raise amount is a local variable. It does not work with self,. raise amount will only work for this function
        return new_pay

    def apply_raiseGlobal(self):
        new_pay = int(self.pay + self.raise_amountGlobal)
        return new_pay


emp_1 = Employee('Ishe','Murwira',20000)
emp_2 = Employee('John','Jamerson',25000,'Male')
emp_3 = Employee ('Susan','Rusike',15000,'Female')

print(emp_1.apply_raiseGlobal())
print(emp_1.apply_raiseLocal())
