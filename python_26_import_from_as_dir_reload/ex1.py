# Создание и подключение модулей в Python
# Подключим модуль mymath.py к нашей программе
import mymath                       # _1_
from mymath import sum              # _2_
# from mymath import sum, PI        # _2_   - для импорта нескольких элементов
# from mymath import *              # _2_   - импорт всех элементов(ф-ций, переменные) из нашего модуля подключатся к программе
                                    # _2_   - * недостаток в конфликте имен уже существующих переменных и ф-ций
from mymath import sum as my_sum    # _3_   - Если мы хотим сделать так, чтоб стандартная ф-ция sum продолжала работать 
                                    # _3_   - После ключевого слова as указать alias - my_sum (псевдоним импортируемого элемента)
                                    # _3_   - Теперь ф-ция sum будет доступна по имени sum
from mymath import PI, sum as my_sum       # _4_   - Если импортируем сразу несколько элементов                                
from lib.mymath import PI, sum as my_summy # _5_   - Подключение модуля из подкаталога lib  
import lib.mymath                   # _6_   - При таком импорте создается пространство имен с именем  lib.mymath

import mymath                       # _7_   - Особенности операций импорта, импортируем наш модуль mymath
mymath.PI = 3                       # _7_   - меняем значение переменной PI на 3 
# import mymath       запишем       # _7_   - Снова импортируем наш модуль mymath                       
#                     ниже          # _7_   - Python  целях оптимизации импортирует каждый отдельный модуль только один раз и затем не меняет
#                     вместо        # _7_   - При необходимости модуль можно перезагрузить используя вспомогательный модуль
                                    # _7_   - Начиная с версии Python 3.4+ - этот модуль назыв. importlib
from importlib import reload        # _7_   - Импортимруем из модуля importlib ф-цию reload = Перезагрузка модуля
reload(mymath)                      # _7_   - Используя эту ф-цию перезагрузим этот модуль  = Перезагрузка модуля
# или
import importlib                    # _7_   - Перезагрузка модуля - обычный импорт 
importlib.reload(mymath)            # _7_   - Перезагрузка модуля - используя пространство имен вызовем ф-цию reload

from mymath import PI               # _8_   - когда мы импортируем из нашего модуля mymath переменную PI, (происходит создание новой переменной в нашей глобальной области видимости 
                                    # _8_   - то эта переменная буквально копируется в глобальную область видимости нашей програамы ex1.py
                                    # _8_   - идет создание новой переменной PI с соответствующим значением  
import mymath                       # _8_   - импортируем этот модуль еще раз и изменим значение PI на 3 
PI = 3                              # _8_   - изменим значение PI на 3

                                    # _9_   - Список
from mymath import ar               # _9_   - импортируем из нашего модуля mymath переменную ar = [1,2,3,4] - это СПИСОК 
import mymath                       # _9_   - выполним импорт всего модуля, то переменные ar и ar.mymath будут ссылаться на один и тот же список
ar[1] = 100                         # _9_   - изменим второй элемент из переменной ar на значение 100, то оба списка изменят значение на 100
                                    # _9_   - это говорит о том, что переменные ar и ar.mymath ссылаются на один и тот же список
                                    # _9_   - изменяемые типы данных не копируются, не дублируются. Как были созданы один раз так и остаются

                                    # _10_   - Кортеж
                                    # _10_   - изменяемые типы данных не копируются, не дублируются. Как были созданы один раз так и остаются
from mymath import cort             # _10_   - импортируем из нашего модуля mymath переменную cort = (1,2,3,4) - это КОРТЕЖ                              
import mymath                       # _10_   - выполним импорт всего модуля, то переменные cort и cort.mymath будут ссылаться на один и тот же кортеж
cort += (10, )                      # _10_   - добавим еще один элемент в наш кортеж, изменения коснуться переменной mymath.cort

                                    # _11_   - в Python имеется полезная функция  dir(<модуль>) -возвращает имена всех данных, которые импортируются с указанным модулем
import mymath                       # _11_   - импортируем модуль mymath и вызовем функцию dir - print( dir(mymath) )


                                    
# Если же мы не хотим создавать нового пространства имен,
# то можно импортировать элементы модуля по следующему правилу
# пишем ключевое слово from, указываем имя модуля, после слова import, говорим, что
# будем брать из этого модуля, в данном случае ф-цию sum, далее ф-ция sum будет
# находиться в глобальном пространстве имен, и mymath писать не нужно перед ф-цией



# _1_
# вызовем из модуля mymath функцию sum, которая была в нем там определена
# m = sum(1,2,3)         - Error - по умолчанию ф-ция sum в Python берет на вход список, а не набор аргументов

# Если мы уберем mymath. - Error - по умолчанию ф-ция sum в Python берет на вход список, а не набор аргументов 
m = mymath.sum(1,2,3)   # По умолчанию разделяем ф-цию sum пространством имен mymath
# название модуля mymath.название ф-ции sum

print(m)


# выведем значение переменной которая там была определена в модуле 
print(mymath .PI)


# _2_
m1 = sum(1,2,5)
print(m1)
# "from mymath import sum: ",

# mm = sum([1,2,4])       # - укажем список [] - все работает ДЛЯ МОДУЛЯ _1_ import mymath
#print(mm)

# mymath - это пространство имен, которое автоматически создается при подключении соотв. модуля
# пространство имен чтоб избежать конфликта с другими подобными ф-ми
# в Python уже существует функция sum, но наш вариант из модуля mymath никак не повлияет на ее работоспособность

# _3_
m2 = my_sum(1,2,7)
print(m2)
# Если написать стандартную ф-цию Error, т.к. задан alias

# _4_
m3 = my_sum(1,2,8)
print(m3)
print(PI)


# Во всех наших примерах модуль mymath находился в том же каталоге, что и файл ex1.py.
# Когда мы что-либо импортируем, то файл ищется следующим образом:
#  - в текущей директории программы (в данном случае ex1.py);
#  - в директориях, указанных в переменной окружения PYTHONPATH;
#  - в директориях стандартных библиотек;
#  - в дополнительных путях, прописанные в .pth-файлах и пакетах сторонних разработчиков.


# _5_                   - Подключение модуля из подкаталога lib
m4 = my_summy(1,2,9)
print(m4)
print(PI)

# _6_                   - Подключение модуля из подкаталога lib, так указывается пространство имен
m5 = lib.mymath.sum(1,2,10)
print(m5)
print(lib.mymath.PI)

# _7_  
print("Измененное значение PI: ", mymath.PI)

# _8_  
print("Измененное значение PI из модуля mymath: ", PI)
print("Значение PI из модуля mymath: ", mymath.PI)

# _9_  
print("Переменная ar из модуля mymath: ", ar)
print("Переменная mymath.ar из модуля mymath: ", mymath.ar)
print(ar, mymath.ar, sep="\n")

# _10_  
print("Переменная cort из модуля mymath: ", cort)               # К первому кортежу добавился элемент, а другой остался неизменным
print("Переменная mymath.cort из модуля mymath: ", mymath.cort) # К первому кортежу добавился элемент, а другой остался неизменным
print(cort, mymath.cort, sep="\n")                              # К первому кортежу добавился элемент, а другой остался неизменным
# Когда такие переменные ссылаются на неизменяемый тип данных,
# то при cort += (10, ) - создается новый объект с новым содержимым
# переменная cort ссылается уже на другой объект, а когда работали со списком ar, то
# переменная ar продолжала ссылаться на тот же объект

# _11_  
print("Функция  dir(<модуль>) -возвращает имена всех данных, которые импортируются с указанным модулем: ", dir(mymath) )
