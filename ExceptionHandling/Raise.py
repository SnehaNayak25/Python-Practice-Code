'''
def disp(a,b):
    print(a/b)
 #  print(a/c) --> NameError: name 'c' is not defined
# disp(10,0) --> ZeroDivisionError: division by zero
disp(10,20)
# disp(10,'Kodnest') --> TypeError: unsupported operand type(s) for /: 'int' and 'str' 

'''

def checkage(age):
    if age < 18 :
        raise ValueError('Age must be greater than 18')
    
try:
    checkage(12)
except ValueError as e:
    print('Error Message: ' , e)


