'''
1. Conditional: if-else, if-elif
2. Looping: for, while
3. Jumping: break, continue, pass

'''

def checkAge(age):
    if(age>18):
        print('Age is greater than 18')
    else:
        print('Age is not greater than 18')
checkAge(18)

# Program to display 'Child' if age is below 18, display 'Adult' if it is above 18 , display 'Senior Citizen' if age is above 65
age = int(input('Enter age: '))
def displayAgeCategory(age):
    if age<18 :
        print('Child')
    elif age > 18 and age < 65:
        print('Adult')
    else:
        print('Senior Citizen')
displayAgeCategory(age)
