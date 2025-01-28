'''
1. Method Chaining is the process of calling one method from another method
'''
class GrandParent:
    def  cook(self):
        print('Grand Parent can cook Biryani')

class Parent(GrandParent):
    def cook(self):
        # super().cook()
        print('Parent can cook Maggie')

class Child(Parent):
    def cook(self):
        super().cook()
        super(Parent,self).cook() # In this line it goes to the parent of Parent class
        print('Child wont cook')

c = Child()
c.cook()
