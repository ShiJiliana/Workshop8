n = int(input())
numbers = []
for i in range(2, n+1):
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
            break
    if check:
        print(i)
