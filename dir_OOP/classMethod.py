

import datetime as dt


class Employee:

    raise_amountGlobal = 15.003 # that is a global variable
    gmail = '@gmail.com'
    num_of_Employee = 0

    def __init__(self,firstName,lastName,salary,gender=None): # None helps to declare a optional parameter, not mandatory 
        self.first = firstName  # self represents this class, the instance of this class
        self.last = lastName
        self.pay = salary
        self.email = firstName + '.' + lastName + self.gmail # always use self to access the instances of that file
        self.gen = gender
        Employee.num_of_Employee += 1 # this will help increment the number of employees.
    
    def apply_raiseLocal(self):
        raise_amountLocal = 10.002
        new_pay = int(self.pay + raise_amountLocal) # raise amount is a local variable. It does not work with self,. raise amount will only work for this function
        return new_pay

    def apply_raiseGlobal(self): # the apply function is a regular method
        new_pay = int(self.pay + self.raise_amountGlobal)
        return new_pay
    
    @staticmethod
    def is_workDay(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        else:
            return True
    
    @classmethod # that is a class method, its different from the other methods
    def set_raiseAmount(cls,amount): # a regular we need an object of that function to call it but a class function we can call it directly
        cls.raise_amountGlobal = amount

# print(f'Number of employees is: {Employee.num_of_Employee}')
emp_1 = Employee('Ishe','Murwira',20000)                  # we created an object for the class and call it an instant of the class. The object we created emp1 is still called the instant of the class
emp_2 = Employee('John','Jamerson',25000,'Male')
emp_3 = Employee ('Susan','Rusike',15000,'Female')
# print(f'Number of employees is: {Employee.num_of_Employee}')

# print(emp_1.apply_raiseGlobal()) 
# print(emp_1.apply_raiseLocal())


# print(Employee.raise_amountGlobal)
# Employee.set_raiseAmount(50)
# print(Employee.raise_amountGlobal)

myDate = dt.date(2021,6,24)
workDay = Employee.is_workDay(myDate)

print(workDay)
