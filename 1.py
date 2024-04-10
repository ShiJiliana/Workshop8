b = []
b_new = []
n = 0
for i in range(500):
    while n != -1:
        n = int(input(f'Введите результат игрока № {i+1}: '))
        b.append(n)
        i += 1

for j in range(len(b) - 1):
    if b[j] < b[j+1]:
        b_new.insert(0, b[j+1])

print('Лучший результат игры:', b_new[0])
