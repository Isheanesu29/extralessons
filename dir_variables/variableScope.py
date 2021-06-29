
# when you define a variable inside the function it can only be assesed by that function but when you define it outside it global and be 
# asseced by all function

Global = 5 + 10

def addition():                    # with this example you since you told it to return you have to tell it to print at the bottom
    Local = 10                     # it is different from the below example but does the same thing
    return (Global + Local)

# def addition():              # in this case you do not have to print twice, you can just call the function and you have already declared variable on top                               
#     Local = 10
#     print(Global + Local)

# addition()
    
    

def subtraction():
    Local = 13
    print(Global - Local)

addition()
# subtraction()