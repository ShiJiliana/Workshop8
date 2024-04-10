b = []
n = -2
for i in range(500):
    while n != 0:
        n = int(input(f'Введите доход гражданина: '))
        b.append(n)
        i += 1
print('Средний доход =', sum(b) / (len(b) - 1))