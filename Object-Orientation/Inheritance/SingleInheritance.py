class Demo1:
    def displ(self):
        print('Inside disp1')
    
class Demo2(Demo1):
    pass

d2 = Demo2()
d2.displ()