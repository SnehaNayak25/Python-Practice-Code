'''
Acheiveing Polymorphism using Method Overriding
'''

class Calculator:
    def calculate(self,a,b):
        print('Performs Arithmetic operations ')

class Add(Calculator):
    def calculate(self,a,b):
        print("Addition: ", a+b)

class Sub(Calculator):
    def calculate(self,a,b):
        print("Subtraction: ", a-b)

class Mul(Calculator):
    pass

ref = Add()
ref.calculate(10,20) # 30

ref = Sub()
ref.calculate(20,10) # 10

ref = Mul()
ref.calculate(10,20) # Performs Arithmetic operations
