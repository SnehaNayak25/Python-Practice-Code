li1 = [1,2,3,4,5]
sq_li = []
for i in li1:
    sq_li.append(i**2)
print(f"Squares: {sq_li}") # [1, 4, 9, 16, 25]

# The above one can be achieved in two lines using list comprehension
# 
# Syntax: for only one condition (when there is no else part)
#           [expression for i in iterable_object condition]
#
#   expression -- the operation to be performed and then returns

li2 = [11,12,13,14]
square_list = [i**2 for i in li2]
print(f"Squares: {square_list}") # [121, 144, 169, 196]

new_li = [ele+2 for ele in li2]
print(f"Adding 2 to each element: {new_li}") # [13, 14, 15, 16] 

li3=list(range(2,20))
even_list=[i for i in li3 if i%2==0]
print(f"Even numbers List: {even_list}") # [2, 4, 6, 8, 10, 12, 14, 16, 18]

'''
Syntax: (When there is else part in condition)
        ['if condition is true' if <condition> else 'if condition is false' for i in iterable_object]
'''

li4 = list(range(1,20))
even_and_odd_list = ['Even' if i%2==0 else 'Odd' for i in li4]
print(f"Combination of even odd numbers: {even_and_odd_list}")
# ['Odd', 'even', 'Odd', 'even', 'Odd', 'even', 'Odd', 'even', 'Odd', 'even', 'Odd', 'even', 'Odd', 'even', 'Odd', 'even', 'Odd', 'even', 'Odd'] 

# Multiple for loops Inside List Comprehension
li = [[10,20],[30,40],[50,60]]
new_li = [ele for i in li for ele in i]
print(f"New flattened list: {new_li}") # [10, 20, 30, 40, 50, 60]
# In the above code first for loop will be executed  
# i = [10,20] [30,40] [50,60] will be present