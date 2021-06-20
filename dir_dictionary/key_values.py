

from typing import ValuesView


student = {'name':'Ishe','age':32,'address':'jersgatan 3D','gender':'female','subject':['math','chemestry','biology']} 



# print(len(student))

x = student.keys()
y = student.values()

# print(x)
# print(y)

# for keys in student:
#     print(keys)

for keys,values in student.items():
    print(keys,values)



