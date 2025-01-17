#  iterable_pbject.reverse() - reverse the original objects
li = [10,5,20,7,40]
print(f"Before reverse() method: {li}")
li.reverse()
print(f"After reverse() method: {li}")

print("---------------------------------------")

# reversed(iterable_object) - return iterable object so it needs to be converted to list, tuple or any other.
li1 = [11, 6, 8, 22]
print(f"Before reversed() method: {li1}")
reverse_li1 = list(reversed(li1))
print(f"After reversed() method: {reverse_li1}")

print("---------------------------------------")

li2 = [1,5,2,9]
print(f"Before reverse() method: {li2}")
li2.reverse()
print(f"After reverse() method: {li2}")

print("---------------------------------------")

li3 =[1,5,2,9]
print(f"Before reversed() method: {li3}")
reverse_li3 = list(reversed(li3))  # Creating new reverse list and storing it in reference variable.
print(f"After reversed() method: {reverse_li3}")