'''
1. Inherited Method
    Methods which are inherited from parent class and used as it is in the child class.
2. Overridden method
    Methods which are inherited from parent class and implementation is changed in the child class.
3. Specialized Methods
    Methods which belongs to child class only.
    
'''

class Student:
    def cook(self):
        print('Student is cooking')
    def play(self):                   # Inherited Method
        print('Playing Cricket')

class Employee(Student):
    def work(self):                     # Specialized Method
        print('Employee is working')
    def cook(self):                     # Overridden Method
        print('Employee is cooking')

e = Employee()
e.play()
