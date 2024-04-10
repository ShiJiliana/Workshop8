n = input('Введите целое число: ')
while not n.isdigit():
    n = input('Ошибка, попробуйте ещё раз: ')
if n.isdigit():
    print('Введено целое число:', n)
