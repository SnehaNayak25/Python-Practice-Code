'''

1. In set we can store homogeneous and heterogeneous data.
2. Set is an unordered collection of data.
3. Set does not support indexing of data.
4. In set we cannot store duplicates.
5. Sets are mutable.


'''
s1 = {10,True,'Kodnest',10,20,55.44}
print(f"Original Set: {s1} , Type: {type(s1)}")

# print(s1[0]) --> Error

# add(element) - used to add an element in the set.
s1.add(500)
print(f"After using add() method: {s1}")

# remove(element) - removes the specified element if it is not there then there will be error
s1.remove(55.44)
print(f"After using remove() method: {s1}")

# pop() - Without index will delete and return one element.
popped_ele = s1.pop()
print(f"Deleted element is: {popped_ele}")
print(f"After using pop() method: {s1}")

# del keyword
del s1 # Entire set will be deleted

# del s1[2] --> gives error because it uses index
