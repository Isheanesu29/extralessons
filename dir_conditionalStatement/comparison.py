

a = [1,2,3,4,5]
b = [1,2,3,4,5]

# print(a==b)

print(a is b)    # is shows the position a valuable has in memory

print(id(a),id(b)) 

# false values 
False
None
0
''
[]
{}
()

condition = ()

if condition:
    print('evaluate to true')
else:
    print('evaluate to false')