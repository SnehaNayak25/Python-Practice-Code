# Program to print numbers from 1-10 but if number is 6 then skip printing.

for i in range(1,11):
    if(i==6):
        continue
    print(i, end =" ") 
print()

# Program to print numbers from 1-10 but if number is 5 then stop printing.
for i in range(1,11):
    if(i==5):
        break
    print(i, end = " ") 
print()

for i in range(1,4):
    if(i==2):
        pass
    else:
        print(i,end =" ")
