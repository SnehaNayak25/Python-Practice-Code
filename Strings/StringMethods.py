# Different ways of declaring string:
s1 = "I'm Sneha"
s2 = 'My "age" is 23'
s3 = """"We are Learning Strings"""
s4 = '''Python is dynamically Typed Language'''
print(s1)
print(s2)
print(s3)
print(s4)

# Combining Strings
greeting = "Hello, "
name = "Python"
combined_message = greeting + name
print(combined_message)

# Accessing characters in String
word = "Python"
print(word[0]) # P
print(word[3]) # h
print(word[-1]) # n

# String Slicing
phrase = "Hello, Python"
print(phrase[0:5]) # Hello
print(phrase[:8]) # Hello, P
print(phrase[7:]) # Python

# Finding length of the string
message = "Hello, Python"
print(len(message)) # Python

# Changing the case of strings
str1 = "HeLlo, Python"
upperstr = str1.upper()
lowerstr = str1.lower()
print(upperstr) # HELLO, PYTHON
print(lowerstr) # hello, python

# Finding substrings in a string
str2 = "Welcome to Python Learning"
print(str2.find("Python")) # 11 - gives the index value
print("to" in str2) # True



