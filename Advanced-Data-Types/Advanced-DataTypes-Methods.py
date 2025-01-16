'''
list(iterable_object) - can have only iterable objects as argument
tuple(iterable_object) 
set(iterable_object) 
dict(iterable_object:key:value)
'''
# li1=list(5)  --> TypeError: 'int' object is not iterable

li1 = list('Kod')
print(f"String to list: {li1}") # ['K', 'o', 'd']

li2 = list((10,20))
print(f"Tuple to list: {li2}") # [10, 20]

li3 = list({100,200})
print(f"Set to list: {li3}") # [200, 100]

li4 = list({'name':'Sona','age':20})
print(f"Dictionary to list: {li4}") #  ['name', 'age'] -- List of keys it will return

li5 = list(range(1,11))
print(f"Range to list: {li5}") # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tup1 = tuple([10,20,30])
print(f"List to tuple: {tup1}") # (10, 20, 30)

tup2 = tuple({100,200})
print(f"Set to tuple: {tup2}") # (200, 100)

tup3 = tuple(range(1,11))
print(f"Range to tuple: {tup3}") # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

tup4 = tuple('Kodnest')
print(f"String to tuple: {tup4}") # ('K', 'o', 'd', 'n', 'e', 's', 't')

tup5 = tuple({'name':'Sona','age':20})
print(f"Dictionary to tuple: {tup5}") # ('name', 'age') -- Tuple of keys it will return

set1 = set([10,20,30,20])
print(set1) # {10, 20, 30}

d1 = dict([['name','Sona'],['age',22]])
print(d1) # {'name': 'Sona', 'age': 22}

d2 = dict((('name','Sona'),('age',22)))
print(d2) # {'name': 'Sona', 'age': 22}