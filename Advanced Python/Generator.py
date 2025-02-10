'''
def disp():
    return 10
    return 20
    return 30
   
print(disp()) # 10
print(disp()) # 10 
print(disp()) # 10

'''
def generator_function():
    # print('Hello')
    yield 10
    yield 20
    yield 30

# print(generator_function()) # <generator object generator_function at 0x00000110B44449E0>

ref = generator_function()
print(next(ref)) # 10
print(next(ref)) # 20
print(next(ref)) # 30
# print(next(ref)) -->StopIteration