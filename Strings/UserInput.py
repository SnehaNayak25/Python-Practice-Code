# input() will always take input as string:
num1 = input('Enter a number: ')
print('Value of num1 is: ', num1,' Data Type of num1 is: ',type(num1))

# int method is used for typecasting that is for converting string to integer
num2 = int(input('Enter a number: '))
print('Value of num1 is: ', num1,' Data Type of num1 is: ',type(num1))

# Program for addition of two numbers by taking user input
num1 = int(input('Enter a number1 : ')) # 20
num2 = int(input('Enter a number2 : ')) # 10
print(f'Addition of {num1} and {num2} is  : {num1+num2}') # 30
print(f'Subtraction of {num1} and {num2} is  : {num1-num2}') #10
print(f'Multiplication of {num1} and {num2} is  : {num1*num2}') #200
# Division result in python will always be of type float
print(f'Division of {num1} and {num2} is  : {num1/num2}')#2.0

