'''
def disp(a,b):
    print(a/b)
 #  print(a/c) --> NameError: name 'c' is not defined
# disp(10,0) --> ZeroDivisionError: division by zero
disp(10,20)
# disp(10,'Kodnest') --> TypeError: unsupported operand type(s) for /: 'int' and 'str' 

'''

def checkage(age):
    if age < 18 :
        raise ValueError('Age must be greater than 18')
    
try:
    checkage(12)
except ValueError as e:
    print('Error Message: ' , e)


'''
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,depo_amount):
        if depo_amount <= 0:
            raise ValueError("Deposit failed. Deposit amount must be positive.")
        self.balance += depo_amount
        print(f'Deposit of {depo_amount} successful. Current balance: {self.balance}')

    def withdraw(self,with_amount):
        if with_amount < 0 and with_amount > self.balance:
            raise ValueError("Withdrawal failed. Insufficient balance.")
        else:
            self.balance -= with_amount
            print(f"Withdrawal of {with_amount} successful. Current balance: {self.balance}")

depo_amount = int(input('Deposit amount: '))
with_amount = int(input('Withdraw amount: '))

b = BankAccount()
try:
    b.deposit(depo_amount)
    b.withdraw(with_amount)
except ValueError as e:
    print('Error Message: ', e)



    


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,depo_amount):
        if depo_amount <= 0:
            raise ValueError("Deposit failed. Deposit amount must be positive.")
        self.balance += depo_amount
        print(f'Deposit of {depo_amount} successful. Current balance: {self.balance}')

    def withdraw(self,with_amount):
        if with_amount < 0 and with_amount > self.balance:
            raise ValueError("Withdrawal failed. Insufficient balance.")
        else:
            self.balance -= with_amount
            print(f"Withdrawal of {with_amount} successful. Current balance: {self.balance}")

b = BankAccount()
try:
    depo_input = input()
    depo_amount = int(deposit_input.split(":")[-1].strip())
    b.deposit(depo_amount)
except ValueError as e:
    print(f"Deposit failed: {e}")



'''