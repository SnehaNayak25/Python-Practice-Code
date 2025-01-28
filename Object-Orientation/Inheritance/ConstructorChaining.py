'''
1. Constructor chaining is the process of calling one constructor from another constructor.
'''
class GrandParent:
    def __init__(self):
        self.x = 100
class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        self.y = 200

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.z = 300

c = Child()
print(c.z)
print(c.y)
print(c.x)
