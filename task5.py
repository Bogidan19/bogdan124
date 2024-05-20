# задача 1 проанализировать программу

empty_tuple = () # Пустой кортеж
tuple_with_one_item = (1,) # кортеж из одного элемента
tuple_ = (1, 2, "str")
print("Содержимое переменной empty_tuple:", empty_tuple,
type(empty_tuple))
print("Содержимое переменной tuple_with_one_item:",
tuple_with_one_item, type(tuple_with_one_item))
print("Содержимое переменной tuple_:", tuple_, type(tuple_))
list_ = [] # Пустой список
chars_list = ["a", "b", "c"]
print("Содержимое переменной list_:", list_, type(list_))
print("Содержимое переменной chars_list:", chars_list,
type(chars_list))
empty_string = "" # Пустая строка
str_ = "test" # Строковый тип данных
print("Содержимое переменной empty_string:", empty_string,
type(empty_string))
print("Содержимое переменной str_:", str_, type(str_))
empty_set = set() # Пустое множество
set_ = {3, 2, 1, 1} # Множество содержит в себе тольком уникальные элементы
print("Содержимое переменной empty_set:", empty_set,
type(empty_set))
print("Содержимое переменной set_:", set_, type(set_))
empty_dict = {} # Пустой словарь
dict_ = { # Словарь хранит пары ключ-значение. Ключи должны быть уникальными значениями
 "Имя": "Ваше имя",
 "Фамилия": "Ваша фамилия",
 "Возраст": 18,
 "Возраст": 20,}
print("Содержимое переменной empty_dict:", empty_dict,
type(empty_dict))
print("Содержимое переменной dict_:", dict_, type(dict_))

#Задача 2 Первый и последний участник
list_players = ["Маша", "Петя", "Саша", "Оля",
"Кирилл"]
last_player = list_players[-1]
reestr = {"Первый участник": list_players[0]}
print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

#Задача 3 Удаление дубликатов из списка
shopping_list = ["яблоко", "молоко", "хлеб", "яблоко",
"масло", "яйца", "молоко"]
unique_items = set(shopping_list)
print("Количество уникальных товаров:", len(unique_items))

#Задача 4 Словарь времен года
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
print(seasons_dict)

#Задача 5 Статистика посещений сайта
users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict_users = {"общее количество": len(users), "уникальное посещение": len(set(users))}
print(dict_users)

#Задача 6 Обработка списка уникальных чисел
list_=[1,2,3,4,2,4,5,6,5,7,8,6]





