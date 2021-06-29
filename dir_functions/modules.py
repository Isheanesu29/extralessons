

#  For python to allocate a file that is not in python you have to state where the file is with path.append
# we can also add a path directly to an enviromental variable

import sys
sys.path.append('/Users/user/Desktop/projects/extralessons')

import dir_list.leapYear as lp
import dir_list.search as sh
from  dir_list.leapYear import daysInMonths

animals = ['Dogs','Cats','Rats','Cows','Pigs']

x = lp.daysInMonths(2021,6)
# print(x)
# print(sys.path)

y = sh.find_Index(animals,'Cows')
print(y)