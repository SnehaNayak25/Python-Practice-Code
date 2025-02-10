li = [10,20,30,40,50]
print(type(li),li)
iterable_object = iter(li)
print(type(iterable_object),iterable_object)

print(next(iterable_object)) # 10
print(next(iterable_object)) # 20
print(next(iterable_object)) # 30
print(next(iterable_object)) # 40
print(next(iterable_object)) # 50
# print(next(iterable_object)) --> StopIteration Error