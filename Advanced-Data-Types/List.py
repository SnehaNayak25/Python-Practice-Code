'''

1. In List we can store homogeneous as well as heterogeneous data.
2. In List we can store duplicate values.
3. List is an ordered collection of data (order of insertion will remain as it is in the output).
4. Lists are mutable (Once we declare list, we can modify it)


'''
# Creation
list1 = [10,20,44.45,True,'Kodnest',20]
print(f"Original List: {list1} , Type: {type(list1)}")

# Accessing specific values
print(f"Accesing each element: {list1[0]}")

# append(element) - will add element at the end of the list and it accepts one parameter
list1.append(300)
print(f"After append() method: {list1}")

# insert(index,element) - adds element at particular position specified by the user
list1.insert(1,12)
print(f"After insert() method: {list1}")

# remove(element) - Removes the first occurence of the specified element
list1.remove(20)
print(f"After remove() method: {list1}")

# It gives error because the element is not present in the list
# list1.remove(13)
# print(f"After remove() method: {list1}") 

# in and not in - To check whether the element is present in list or not
print('Membership Operators:')
print(2000 in list1)  # False
print('Kodnest' in list1) # True
print(2 not in list1) # True
print(10 not in list1) # False

# pop() - Without argument will delete and return last element from list
removed_ele = list1.pop()
print(f"Removed element is: {removed_ele}")
print(f"After remove() method which does not take any argument{list1}")

# pop(index) - - with argument will delete the element at specified index
removed_ele = list1.pop(3)
print(f"Removed element is: {removed_ele}")
print(f"After remove() method which has argument{list1}")

# del keyword - will not return the element
del list1[1]
print(f"After using del keyword {list1}")

del list1
# print(list1)  --> Gives error because del list1 deletes the entire list1
