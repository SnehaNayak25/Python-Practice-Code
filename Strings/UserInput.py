# input() will always take input as string:
num1 = input('Enter a number: ')
print('Value of num1 is: ', num1,' Data Type of num1 is: ',type(num1))

# int method is used for typecasting that is for converting string to integer
num2 = int(input('Enter a number: '))
print('Value of num1 is: ', num1,' Data Type of num1 is: ',type(num1))

# Program for addition of two numbers by taking user input
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
print(f'Addition of {num1} and {num2} is  : {num1+num2}')