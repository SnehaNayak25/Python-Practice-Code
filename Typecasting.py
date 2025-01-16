#  String which is holding integer value then conversion to int is  possible
a = '30'
print(a, type(a))
b = int(a)
print(b, type(b))

#  String which is holding string value then conversion to int is not possible
x ='Kod'
print(x, type(x))
# y = int(x)
# print(y, type(y))


# float()
p = float(input('Enter float type data: ')) # 12.22
print(p, type(p))

'''
bool()

1. While converting int to bool for all non zero values we will get True.
2. while converting to bool, if a variable has zero or empty string then it will return False

'''
q = 12
print(q, type(q))  # int
q = bool(q)
print(q, type(q)) # True 

q = 0
print(q, type(q))  # int
q = bool(q)
print(q, type(q)) # False 

q = ""
print(q, type(q))  # int
q = bool(q)
print(q, type(q)) # False 

# String holding float value cannot be converted to int
# print(int('12.56')) # Gives error

# Float value can be converted int
print(int(12.56))

# Taking float value from user and converting it into int
value = int (float(input('Enter price: Floating value ')))
print(value, type(value))