for value in collection:
# Начало блока кода с телом цикла


# конец блока кода с телом цикла
# код, который будет выполняться после цикла
a = {1:'x', 2: 'y', 3: 'z'}
for index, value in items():
    print (f'"Позиция:{index}-> Значение: {value}"')
    #список list
    for value in [1,2,3,4,5]:
        print(value)
        # кортеж tuple
        for value in (1,2,3,4,5):
            print(value)
            # множество set
            for value in {1, 2, 3, 4, 5}:
                print(value)
            range(10)
            # Генерация последовательности чисел от 0 до 9
            range(1, 11)
            # Генерация последовательности чисел от 1 до 10
            range(1, 11, 2)
            # Генерация последовательности чисел от 1 до 10 с шагом 2
            range(10, 0, -1)
            # Генерация последовательности чисел от 10 до 1 с шагом -1
print(range(10)) # объект типа range
print(list(range(10))) # список целых чисел от 0 до 9
включительно
print(tuple(range(1, 11))) # кортеж целых чисел от 1 до 10
включительно
print(list(range(1, 11, 2))) # список целых нечетных чисел от
1 до 9 включительно
print(tuple(range(10, 0, -1))) # range так же поддерживает
отрицательный шаг

for _ in range(5):
# Просто выполнить цикл 5 раз
print("Hello World!")

numbers = [10,20,30,40,50] # объявление списка чисел
total = 0 # TODO заменить использование индексов на перебор значений чисел
for i in range (len(numbers)):
    total += numbers[i]
    print ("сумма чисел:", total) #сумма чисел: 150

    for tuple_ in enumerate(["а", "б", "в"]):
        print(tuple_)
    В данном примере функция enumerate используется для перебора элементов списка ["а", "б", "в"].\
        На каждой итерации цикла, переменная tuple_ будет хранить кортеж, состоящий из индекса и соответствующего значения. Результат вывода будет следующим:
(0, 'а’)
(1, 'б’)
(2, ‘в’)

for pos, value in enumerate ("абв", start=1) # start можно указать любым целым числом
    print ("позиция:", pos, "->", "Значение:", value)
while условие
    #начало блока кода с телом цикла. Один отступ вправо от уровня объявления цикла

# конец блока кода с телом цикла
# код который будет выполняться после цикла. Один отступ влево, чтобы закончить объявление цикла
count = 0
while count < 5:
    print ("Значение count:", count)
    count += 1

    sum_ = 0
    input_number = int(input("Введите число:"))
    while input_number != 0:
        sum_ += input_number
        input_number = int(input("Введите число:"))
        print("Ответ:", sum_)