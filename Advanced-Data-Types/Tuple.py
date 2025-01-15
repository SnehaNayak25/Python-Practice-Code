'''

1. In tuple we can store homogeneous as well as heterogeneous data.
2. In tuples we can store duplicates.
3. Tuples are ordered collection of data.
4. Tuples are Immutable (Once we declare we cannot modify it)

'''

# Creation of Tuple
tuple1 = (10,22.55,'Kodnest',True,10)
print(f"Original Tuple: {tuple1}, Type: {type(tuple1)}")

'''

** Modification is not possible that is insertion and deletion **

tuple1.remove(55)
tuple1.pop()
tuple1.append(20)
del tup[2]


'''

# Accessing tuple elements
print(f"Accessing tuple elements: {tuple1[2]}")

del tuple1 # Deletes the entire tuple object
# print(tuple1)  -- gives error because tuple1 is deleted

# Tuple-conactenation
t1 = (10,20,30)
t2 = (40,50)
t3 = t1+t2
print(f"After concatenation: {t3}")
