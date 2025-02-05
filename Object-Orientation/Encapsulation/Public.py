'''
Access Modifiers in Python - To determine the accessibility of data members and member functions
1. Public 
    - By default variables are public
    - It should be accessed inside the same class, outside of any class, inside the child class and inside non-child class.
    - Syntax: 
        variable_name
2. Private
    - It should be accessed inside the same class in which we declared.
    - Syntax: (double underscore is used before the the variable name)
        __variable_name
3. Protected
    - It can be accessed inside the same class, outside of any class, inside the child class and inside non-child class.
    - The variables which are protected should be accessed inside the same class and inside the child class and this is programmers duty to follow these rules.
    - Syntax: (single underscore is used before the the variable name)
        _variable_name

'''

class Demo1:
    def __init__(self,name):
        self.firstname = name
    def disp1(self):
        print(self.firstname)
d1 = Demo1('Akash')
print(d1.firstname)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print(self.firstname)
d2 = Demo2('Pooja')
print(d2.firstname)
d2.disp2()

