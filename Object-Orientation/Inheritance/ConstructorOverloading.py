'''
1. When we create multiple construcors in same class then 
only last declared constructor will be invoked at the time of object creation.

'''
class Demo1:
    def __init__(self):
        self.x = 100
    def __init__(self):
        self.x = 200
d1 = Demo1()
print(d1.x) # 200