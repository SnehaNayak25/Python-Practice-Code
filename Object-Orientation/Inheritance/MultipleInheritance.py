'''
If the parent class and child class have same method name when there is method call  following is used:
MRO Technique --> Method resolution 
1. child class is checkekd first
2. Parent Classes (left - right)

'''

''' Example- 1
class Demo1:
    def disp1(self):
        print('Inside disp1')

class Demo2:
    def disp1(self):
        print('Inside disp2')

class Demo3(Demo1,Demo2):
    pass

d3 = Demo3()
d3.disp1()  # Inside disp1
# d3.disp2()

'''

'''
1. If a child class has constructor then parent class wont be checked
2. If there is no constructor in child class then inheritance(left-right) will be evaluated first
3. Constructors can be inherited in python
'''
# Example-2
class Demo1:
    def __init__(self):
        self.x = 10

class Demo2:
    def __init__(self):
        self.x = 200

class Demo3(Demo2,Demo1):
    # def __init__(self):
    #     self.x = 300
    pass

d3 = Demo3()
print(d3.x) # 300