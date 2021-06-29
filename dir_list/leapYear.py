

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def daysInMonths(year,month):  # this how they guide you when you enter more letters or less letters in a password
    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and isLeapYear(year):
        return 29
    return month_days[month]

# print(daysInMonths(2020,2))

# print(isLeapYear(2020))
    

    