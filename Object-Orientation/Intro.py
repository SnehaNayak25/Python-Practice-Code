class Student:
    def learn(self):
        print('Inside learn method')
    def play():
        print('Inside play ,method')
s1 = Student()
# s1.play() # Student.play() takes 0 positional arguments but 1 was given
s1.name = "Sona"
print("Name is ",s1.name)
s1.learn()
