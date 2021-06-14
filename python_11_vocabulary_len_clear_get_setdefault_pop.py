# Словарь - это неупорядоченная коллекция произвольных данных с доступом по ключу
# Ключ - значение {key1: value1, key2: value2, …, keyN:valueN}
A = {"house": "дом", "car": "машина", "tree": "дерево", "road": "дорога", "river":"река"}
B = {"house": "дом", "house": "дом 2", "car": "машина"} # ключ уникален, но берется последнее значение

# Определить словарь  - функция-конструктор dict - задать словарь
# ключи записываются без кавычек, после них ставится знак равно
C = dict(house = "дом", car = "машина", tree = "дерево", road = "дорога", river = "река")
# С = dict(house = "дом", 2 = "машина")  # не работают числовые значения, только для строк

# Словари создаются на основании ранее сформированных данных, списков
# Список состоит из вложенных элементов - перечислены вложенные списки с двумя элементами: ключ, значение
D = [[2, "неудовлетворительно"], [3, "удовлетворительно"], [4, "хорошо"], [5, "отлично"]]

# Преобразуем в словарь с помощью функции dict
listD = dict(D)
# {2: 'неудовлетворительно', 3: 'удовлетворительно', 4: 'хорошо', 5: 'отлично'}

# dict.fromkeys(список[, значение по умолчанию])
# формирует словарь где ключами будут элементы списка
E = dict.fromkeys(["+7", "+6", "+5", "+4"], "код страны")
# {'+7': None, '+6': None, '+5': None, '+4': None}
# {'+7': 'код страны', '+6': 'код страны', '+5': 'код страны', '+4': 'код страны'}

# Создать пустой словарь
F = {}
FF = dict()

# Любые неизменяемые типы данных можно указывать в словаре
# Присваивая словарю значение с новым ключом, оно автоматически добавляется в словарь
# Добавляем в словарь
# Если же мы существующему ключу присваиваем другое значение, то он просто поменяет свое значение в словаре
# Можем добавлять и менять значения словаря
# Словарь относится к изменяемым типам данных
F[True] = "Истина"
F[False] = "Ложь"
F[True] = 1

# если мы укажем изменяемый тип в качестве ключа 
# F[[1,2]] = 1

# ключи - используются строки или числа
# значения - произвольные данные

G = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
#   key1:val1,key2: value2,   key3:  value3, key4:value4

# удаление ключа - оператором del - по ключу
del G[True]

# Проверка существует ли ключ в словаре
checkKey = print = ("abc" in G)

# Проверка несуществования ключа в словаре
checkKey1 = print = ("abc" not in G)

# функция len - определить длину (число записей) в словаре
lenG = print=(len(G))

# Цикл for - перебор - выводит ключ и значение 
# H = {True: 1, False: "Ложь", "list": [1,2,3], 5: 4}
# for x in H:
   #  print(x)                       #  получится ключ - последний 
   # print(x, H[x])                 #  получится и ключ и значение - последнее

# Очистить все записи из словаря
# H.clear()

# Создание копий словаря
I = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
J = I.copy()

# Проверка по id - разные словари
id(I)                   # Переменные ссылаются на разные объекты
id(J)                   # Переменные ссылаются на разные объекты
J["list"] = [5,6,7]     # Ключу list присвоим значение [5,6,7]

# Метод get - возвращает значения по ключу словаря
getJ = J.get("list")
getJerror = J.get(3, False) # Аргумент False - если ключ неправильно указан

# dict.setdefault(key[, default]) - возвращает значение, ассоциированное с ключом key
# и если его нет, то добавляет в словарь со значением None,
# либо default – если оно указано
setJ = J.setdefault("list")
setJJ = J.setdefault(3)             # 3: None - несуществующий ключ добавляет в конец списка
del J[3]                            # удалили 3: None
setJj = J.setdefault(3, 'three')    # 3: 'three' - добавил ключ и значение

# d.pop - удаляет указанный ключ и возвращает его значение.
# Если в нем указывается несуществующий ключ, то возникает ошибка
J.pop(3)
popJ = J.pop('abc', False)          # в качестве второго аргумента указать значение, возвращаемое при отсутствии ключа
popTrue = J.pop(True)               # ключ присутствует, то возвращается его значение 1

# d.popitem() - удаление произвольной записи из словаря
# Если словарь пуст, то возникает ошибка
K = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
K.popitem()

# метод d.keys() возвращает коллекцию ключей
# По умолчанию цикл for обходит именно эту коллекцию, при указании словаря:
L = {True: 2, False: "Ложь", "list": [4,5,6], 6: 6}
#1 for x in L.items():
#2 for key, value in L.items():  
  #1  print(x)
  #1  print(x[0], x[1])               # Ключ - значение
  #2  print(key, value)  
