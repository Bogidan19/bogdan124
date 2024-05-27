"""
sum_ = 0
input_number = int(input("Введите число:"))
while input_number !=0:
    sum_ += input_number
    input_number = int(input("Введите число:"))
    print("Ответ:", sum_)
"""

'''
a = {"Иван": 30, "Мария": 25, "Сергей": 42}
for value in a.keys():
  print(f"ключ: {value}")
'''

'''
people = {"Иван": 30, "Мария": 25, "Сергей": 42}
for age in people.values():
  print(f"Возраст: {age}")
'''

people = {"Иван": 30, "Мария": 25, "Сергей": 42}
for name, age in people.items():
  print(f"Имя: {name} возраст: {age}")
