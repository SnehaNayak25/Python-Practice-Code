'''
    Strings are immutable: 
    1. Once we declare the string we cannot modify it, if we try to modify the string it will create new string

    2. If new string does not have any reference variable then it will be remove.

    3. Python internally uses string interning

    4. String interning is the process of checking string Intern pool before creating any new object.

       Whenever we want to create new object, Python first will check string intern pool, 
       whether the object already exist or not.

       When Object already exist in th string intern Records then adddress of existing object will be reused.

# '''

s1 =  'Kodnest'
s1.upper()
print(s1)

# Only if we assign s1.upper to one variable then it is converted to upper
s1 =  'Kodnest'
s2 = s1.upper()
print(s2)

# Checking the memory address using id()
s1 = 'K'
print(s1,id(s1))


s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))

# Accessing each character
print(s1[0])  # H
print(s1[-1]) # o

# Address of each chararcter
print('s1 Id of H', id(s1[0]))
print('s2 Id of W', id(s2[0]))

print('s1 Id of o', id(s1[-1]))
print('s2 Id of o', id(s2[1]))

print('s1 Id of l', id(s1[-2]))
print('s1 Id of l', id(s1[-3]))
print('s2 Id of l', id(s1[-2]))

