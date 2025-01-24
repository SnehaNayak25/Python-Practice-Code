# # isalnum() - checks whether a string has alphabets por numbers..
# s1 = 'Kodnest1234*'
# print(s1.isalnum()) # False

# s2 = 'Kodnest12' # True
# print(s2.isalnum())

# print('Kodnest12'.isalpha()) # False
# print('Kodnest'.isalpha()) # True
# print('12'.isdigit())# True

# print('apple'.islower())
# print('apple'.isupper())

# print(any((True,False,False))) # True


# ----------------- Logic-----------------------

s = input() # qA1
print(any([i.isalnum() for i in s])) # True
print(any([i.isdigit() for i in s])) #  True
print(any([i.isalpha() for i in s]))# TRue
print(any([i.isdigit() for i in s]))#True
print(any([i.islower() for i in s])) #True
print(any([i.isupper() for i in s])) #True

