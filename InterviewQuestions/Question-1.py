for y in range(1,11):
    z = 200

def display(a):
    print(a)
    y = 100
    print(y)

display(50)
print(y) # 10 here for loop y value is displayed , for loop y will has global scope ( display function y will not come because it is local variable)
print(z) # 200
# print(a) we will get error because a is the local variable

'''
1. Explain Login reuired decorator
2. What is List Slicing?
--> Is used to create sublist from main list.
    Syntax: list_name[start:end:steps]

'''