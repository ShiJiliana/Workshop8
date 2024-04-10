n = int(input('Введите последнее значение интервала: '))
dividers = [] #список для делителей
number_perfect = 0
p = 0
def check(a):
    global p
    dividers.clear()
    for i in range(1, a):
        if a % i == 0:
            dividers.append(i)
    if sum(dividers) == a:
        p = 1
    else:
        p = 0
    return p

for i in range(2, n + 1):
    if check(i) == 1:
        number_perfect += 1
    i += 1

print('Кол-во совершенных чисел в интервале =', number_perfect)