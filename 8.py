number = '1'
r = (int(number)*8) + 1
print(number, '* 8 +', 1, '=', r)
for i in range(2, 10):
    j = str(i)
    number = number + j
    new_number = int(number)
    result = (new_number * 8) + i
    print(number, '* 8 +', j, '=', result)
    i += 1

number1 = '1'
r2 = (int(number1)*9) + 2
print(number1, '* 9 +', 2, '=', r2)
for i in range(2, 10):
    j = str(i)
    number1 = number1 + j
    print(number1, '* 9 +', i+1, '=', '1'*(i+1))
    i += 1

number2 = '1'
for i in range(1, 10):
    result2 = int((number2 * i))**2
    print(f'{number2*i} * {number2*i} = {result2}')
    i += 1