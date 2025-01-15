rows = int(input())
for i in range(rows):
    for j in range(i,rows):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    for l in range(i+1):
        print('*',end='')
    print()
for i in range(1,rows):
    for j in range(i+1):
        print(' ',end='')
    for k in range(i,rows):
        print('*',end='')
    for l in range(i,rows-1):
        print('*',end='')
    print()