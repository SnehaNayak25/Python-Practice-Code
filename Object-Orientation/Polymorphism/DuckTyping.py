'''
Acheiveing Polymorphism using Duck Typing 

1. In the following example ref will not check the type of object.
2. ref only gives importance to the calculate method not the type (that is Add())
2. ref gives only importance to the the methods of the object.
'''

# class Calculator:
#     def calculate(self,a,b):
#         print('Performs Arithmetic operations ')

class Add:
    def calculate(self,a,b):
        print("Addition: ", a+b)

class Sub:
    def calculate(self,a,b):
        print("Subtraction: ", a-b)

class Mul:
    pass

def permit(ref,a,b):
    if type(ref).__name__== 'Mul':
        print('Mul class does not have calculate()')
    else:
        ref.calculate(a,b)

permit(Add(),10,20)
permit(Sub(),20,10)
permit(Mul(),10,20)
