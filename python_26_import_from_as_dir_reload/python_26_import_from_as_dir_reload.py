# Модуль – это набор конструкций языка Python, например, набор часто используемых функций
# import <модуль1>, <модуль2>, …, <модульN>
# import math                     - математический модуль
# import random                   - для подключения генератора псевдослучайных чисел
# import time

import math, random, time    #    - подключение модулей через запятую

# В программе чтоб вызвать функцию мы пишем: 
res = math.cos(0.7)
# название модуля - math. вызываемую ф-цию cos(значение аргумента 0.7)
print(res)
# значение cos при угле 0.7 rad

# Модули используются на проектах для декомпозиция большой задачи
# на множество более мелких, которые, как правило, можно реализовать независимо друг от друга

# 1. создать программу по распознаванию лиц
# 2. разработчики решили для этого использовать нейронную сеть
# 3. представим программу следующими модулями:
# 4.    - модуль нейронной сети
# 5.    - алгоритм обучения нейронной сети
# 6.    - модуль отвечающий за обучающую выборку и подачи ее на вход нейронной сети
# 7.    - модуль с тестовой выборкой
# 8.    - каждый из модулей может подключать еще дополнительно модули

# Полный  набор модулей
# https://docs.python.org/3/library/
# Поиск сторонних модулей
# https://pypi.org

# Как подключаются и создаются собственные модули
# Создадим свой собственный модуль в каталоге
# Для этого создадим файл в том же каталоге, что и файл ex1.py и назовем его mymath.py
# Переходим в файл mymath.py
