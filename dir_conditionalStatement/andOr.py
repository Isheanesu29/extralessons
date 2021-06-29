

user = 'Admino'
logged_in = True  # bolean is not a string 

if user == 'Admin' and logged_in:  # and adds a statement
    print('Admin is logged in')    # false and true = False
else: 
    print('Admin is not logged in')


if user == 'Admin' or logged_in:  # or will evaluate one statement and pass that one. it does not care about the other one
    print('Admin is logged in')    
else: 
    print('Admin is not logged in')

if not logged_in: 
    print('please log in')     # not turns true to false and the  other way
else:
    print('you are welcome')