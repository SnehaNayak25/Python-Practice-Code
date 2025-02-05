'''
1. Name mangling  is the process of providing new name to the private variables.
2. These new names will be provided automaticallly by python for all private members.
3. New Name will be provided in the format: 
            _className__variableName
'''
class Demo1:
    def __init__(self,name):
        self.__name =name # Private variable

d1 = Demo1('Akash')
# print(d1.__name) --> Error
print(d1._Demo1__name) 





