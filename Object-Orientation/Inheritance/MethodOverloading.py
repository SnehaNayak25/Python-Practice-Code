'''
Method Overloading--> is not possible in python 
If there are methods with same name and differ in number of arguments then last declared method will be executed 
'''
class Demo1:
    def disp(self):
        print('Inside disp with 0 parameters')

    def disp(self,a):
        print('Inside disp with 1 parameters')

    def disp(self,a,b):
        print('Inside disp with 2 parameters')
    
d1 = Demo1()
# d1.disp()
# d1.disp(10)
d1.disp(10,20)
