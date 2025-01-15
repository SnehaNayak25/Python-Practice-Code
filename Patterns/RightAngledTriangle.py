# Increasing Right-Angled Triangle
rows = int(input())
for i in range(rows):
    for j in range(i+1):
        print('*', end=" ")
    print()

print()
# Decreasing Right-Angled Triangle
for i in range(rows):
    for j in range(i,rows):
        print('*', end=" ")
    print()