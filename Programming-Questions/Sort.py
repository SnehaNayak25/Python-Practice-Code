# sort() - sorts the values
li = [10,5,3,20]
print(f"Before Sorting: {li}")
li.sort()
print(f"After sorting using sort() method: (Ascending order) {li}")

li1 = [10,5,3,20]
print(f"Before Sorting: {li1}")
li1.sort(reverse=True)
print(f"After sorting using sort() method: (Descending order) {li1}")

li2 = [100,30,500,10]
print(f"Before Sorting: {li2}")
sorted_li2 = sorted(li2)
print(f"After sorting using sorted() method: (Descending order) {sorted_li2}")

