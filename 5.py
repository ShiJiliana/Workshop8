n = int(input('Введите последнее значение интервала: '))
dividers = [] #список для делителей
number_perfect = 0
def check(a):
    dividers.clear()
    for i in range(1, a):
        if a % i == 0:
            dividers.append(i)
    if sum(dividers) == a:
        return True
    else:
        return False

for i in range(2, n + 1):
    if check(i):
        number_perfect += 1

print('Кол-во совершенных чисел в интервале =', number_perfect)