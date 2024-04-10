b = []
n = 0
for i in range(500):
    while n != -1:
        n = int(input(f'Введите результат игрока № {i+1}: '))
        b.append(n)
        i += 1
print('Количество друзей:', len(b)-1)
