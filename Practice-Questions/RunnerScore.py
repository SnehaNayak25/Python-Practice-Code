# Finding second largest number in the list
n = int(input())
li = list(map(int,input().split()))
li = list(set(li))
li.sort(reverse=True)
print(li[1])
