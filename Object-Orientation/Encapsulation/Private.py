class Demo1:
    def __init__(self,name):
        self.__name =name # Private variable

    def getName(self):    # Getter Method
        return self.__name
    
    def setName(self,newName):  # Setter methods
        self.__name = newName

d1 = Demo1('Akash')
# print(d1.name) --> Error
print(d1.getName())
d1.setName('Preethi')
print(d1.getName())




