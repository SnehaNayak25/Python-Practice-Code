class Employee:
    company_name = "Code"  # Class based variable - that is common for all the employees
    def __init__(self, name, age, desg):    # Constructor
        self.name = name
        self.age = age
        self.desg = desg

    def login(self,time):
        print(f"{self.name} logged in at {time}")
    
    def logout(self,time):
        print(f"{self.name} logged out at {time}")

    def work(self, hours):
        print(f"{self.name} worked for {hours} hours")

    def getDetails(self):
        print(f"Employee name: {self.name}")
        print(f"Employee age: {self.age}")
        print(f"Employee designation: {self.desg}")
        # print(f"Company name: {company_name}") 
        
# Creating Objects
e1 = Employee('Sona',23,'Developer')
e2 = Employee('Sanvith', 24, 'Manager')
e3 = Employee('Dhanvi',22,'SDE')

e1.login(9)
e1.logout(6)
e1.work(9)
e1.getDetails()
print("----------------------")
e2.login(10)
e2.logout(8)
e2.work(9)
e2.getDetails()
print("----------------------")
e3.login(10)
e3.logout(8)
e3.work(9)
e3.getDetails()

