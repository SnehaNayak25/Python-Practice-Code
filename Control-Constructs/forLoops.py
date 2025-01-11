'''

for control_variable in iterable_object:

'''
for i in 'Kodnest':
    print(i)

for j in [10,20,30]:
    print(j+5)

# Range comes upto 11-1 till 10
for num in range(1,11):
    print(num)

# Parameters of range are start, end, steps
# range(start,end,step)
# Default value of start is zero
# Default value of step is one

for num in range(11,21,2):
    print(num, end = " ")
print()

# Program to print all even numbers from 1-10
for num in range(2,11,2):
    print(num, end = " ")
print()

# or 
for num in range(1,11):
    if num%2 == 0:
        print(num, end = " ")

