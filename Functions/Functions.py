# Without input and without return statement
def add():
    a = 10
    b = 20
    print('Addition is: ',a+b)

# With input and without return statement
def sub(a,b):
    print('Addition is: ',a-b)

# Without input and with return statement
def mul():
    return 10*20

# With input and with return statement
def div(a,b):
    return a/b

# Function call
add()
sub(100,50)
print("Product is:", mul())
print("Division Result is:", div(20,10))
