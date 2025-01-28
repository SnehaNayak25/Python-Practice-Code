class Bank:
    bank_name ='SBI'
    def __init__(self,name,age,bal):
        self.name = name
        self.age = age
        self.bal = bal

    def get_info(self):
        print(f"User Name: {self.name}, User Balance: {self.bal} for bank {Bank.bank_name}") # self.bank_name can also be used  

b1 = Bank("Sannidhi",21,500000)
print(b1.bank_name)
print(Bank.bank_name)
b1.get_info()
