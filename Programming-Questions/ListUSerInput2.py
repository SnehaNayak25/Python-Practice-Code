# # Taking input for List
# li = input('Enter space separated elements: ')
# print(li, type(li)) # 1 2 3 4 5 <class 'str'>
# li= li.split()
# print(li) # ['1', '2', '3', '4', '5']
# li = list(map(int,li))
# print(li) # [1, 2, 3, 4, 5]

# # Taking input for tuple in single line
# tup = tuple(map(int,input('Enter space separated elements: ').split()))
# print(tup) # (1, 2, 3, 4, 5)


li = list(map(int,input('Enter space generated values: ').split()))
print([i for i in li if i%2 == 0]) # [10, 12]




