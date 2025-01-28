class StaticMethods:
    @staticmethod
    def add_numbers(a,b):
        return a + b
    
    def calci(self):
        pass

result = StaticMethods.add_numbers(5,3)
print(result)

math_op = StaticMethods()
print(math_op.add_numbers(10,5))