# #create
# a = 'привет' # Одинарные ковычки
# b = "привет" # Двойные ковычки
# c = "я 'знаю' Python" # Комбинированные ковычки
# a = 123
# a = str(a)
# print(f'Строка {a}')
# #string
# a = 'привет'
# print(a)
# print('Иван')
# a = 'привет'
# a[0] # 'п'
# a[1] # 'р'
# a[2] # 'и'
# a[3] # 'в'
# a[4] # 'е'

a = 1, 2, 3
b = str(a)
print(b)
print(type(b))


a = int(input('Введите  число:-'))
if a % 2 == 0:
    print(f'Число {a} является число')
else:
    print(f'Число {a} является нечетным')