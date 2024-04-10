n = int(input())
dividers = [] #список для делителей
def check(a):
    dividers.clear()
    for i in range(1, a):
        if a % i == 0:
            dividers.append(i)
    if sum(dividers) == a:
        return True
    else:
        return False

print('Совершенные числа, не превышающие N:')
for i in range(2, n + 1):
    if check(i):
        print(i)