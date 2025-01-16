'''
1. In dict we cannot store duplicate keys.
2. But duplicate values can be stored.
3. Dictionary is mutable.

'''

d1 = {'name':'Sneha','age':27,'phone':23456}
print(f"Original Dictionary: {d1} , Type : {type(d1)}") #{'name': 'Sneha', 'age': 27, 'phone': 23456}

d1['name'] = 'Driti'
print(d1) # {'name': 'Driti', 'age': 27, 'phone': 23456}

marks = {'Sci':85,'Maths':85,'Sci':78} # {'Sci': 78, 'Maths': 85}
print(f"Duplicate Key: {marks}")

mark = {'Sci':85,'Maths':85}
print(f"Duplicate Values: {marks}") # {'Sci': 78, 'Maths': 85}

for i in d1.keys():
    print(f"Keys: {i}")

for i in d1.values():
    print(f"Values: {i}")

for i in d1.items():
    print(f"Keys and Values: {i}")