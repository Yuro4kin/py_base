# Строки многострочные

str1 = "Hello1 Hello1  Hello1"
print (str1)

str2 = """Hello1 Hello1
Hello1"""
print (str2)

str3 = '''Hello1 Hello1  Hello1 
Hello2 Hello2 Hello2 Hello2'''
print (str3)

'''Hello1 Hello1  Hello1 
World World'''
print ("Hello1Hello1Hello1\nWorldWorld")

# \n - символ переноса строки 
str4 = "Hello1 Hello1  Hello\nWorld Hello2 Hello2 Hello2"
print (str4)

# Задаем пустую строку - строка не будет содержать ни одного символа
# str0 будет ссылкой на пустую строку
# Переменная в Python - это ссылка на соответствующие объекты
str0 = ""
str5 = "message"  # - Определена строка и мы хотим скопировать эту строку в другую строку
str6 = str5       # - Будут ссылаться на одну строку
                  # Получили две ссылки которые ссылаются на одну и ту же строку

id(str5)          # - id будут одинаковые
id(str6)
#    str1 --> У нас есть объект "message"  <-- str2    , на который ссылается две переменные
#    строки не копируются

# Операторы и функции строк
# Оператор соединения двух строк
#wrd1 = "Hello "
#wrd2 = "world !" 
#print(wrd1 + wrd2)

str7 = "Hello"+"world"
print (str7)
str8 = "Hello"+" "+"world"
print (str8)

dig = 5         # - строки не можем соединять с каким-то типом данных
#str9 = "число = "+dig          конкатенация, соединение только СТРОК 

# Функция str преобразовывает аргумент в строку - на выходе не число, а строка 5
str(dig)     # '5'
str(5)       # '5'
str9 = "число = " + str(dig)        # str(dig) - функция
print (str9)

# Преобразовываем в строки любые типы данных - например в булевый тип
# str(True) преобразовывает любые данные в строковые переменные 
# Булевый True в строку True

str10= str(True)
print (str10)

# Размножить строки
one = 'hey '
one*10
msg1 = one*10
print (msg1)

# Дублирование строки, есть строка и мы хотим ее размножить несколько раз
# Определение длины строки

lengthMsg1 = len(msg1)
print (lengthMsg1)

NN = len(one*2)
print (NN)

PP = "Hello World!"
PP = len(PP)
print (PP)

# Оператор in проверяет, содержится ли подстрока в нашей строке
# <подстрока> in <строка>
s = "abcdefg0123"
stringS = "abc" in s         # True
print (stringS)
string0 = "0" in s           # True

# Сравнение строк между собой
strComp1 = "abc" == 'abc'
strComp2 = "ABC" == 'abc'
strComp3 = "ABC" != 'abc'    # Проверка на неравенство двух строк, возвратит True - строки неравны
strComp4 = "abc" != 'abc'    # False - строки на самом деле равны
print (strComp1)
print (strComp2)
print (strComp3)
print (strComp4)

# Условный оператор if, while - пример для сравнения строк
# У пользователя запрашивается пароль, если введет pass - Вход в систему разрешен
# Если введет другое, цикл while продолжит свою работу и попросит ввести пароль еще раз

psw="pass"
in_psw = ""
while psw != in_psw:
      in_psw = input("Введите пароль: ")
      print("Вход в систему разрешен")

str11 = "Кот" > "Код"     # Лексикографический порядок? каждому символу поставлено число, в соответствии с кодовой таблицей
# str12 = "Код"
# str13 = str11 > str12
print (str11)
# Функция ord узнать это число
numOrd1 = ord("т")
numOrd2 = ord("д")
print (numOrd1)
print (numOrd2)

# Индексы и срезы 
# Python - строка - это упорядоченная коллекция символов, у каждого элемента свой index
msg3 = "Hello World!"
print (msg3[0])

# Формула длины строки
msg4 = msg3[len(msg3)-1]        # '!'
print (msg4)
# или
msg5 = msg3[-1]
print (msg5)

# Можно работать и со строковыми литералами
str12 = "abcd"[1]
str13 = "abcd"[-1]
print (str12)
print (str13)

# Выберем сразу несколько символов - срезы
# Есть строка, выделим из этой строки слово World
str14 = msg3[6:11]    # Последний рабочий индекс исключается из интервала, последний рабочий индекс 10
str15 = msg3[2:5]
str16 = msg3[:5]      # Краткая запись до 5 индекса
str17 = msg3[6:]      # Краткая запись после 6 индекса
str18 = msg3[:]       # Вся строка

print (str14)
print (str15)
print (str16)
print (str17)
print (str18)

copy = msg3[:]                  # Создается копия данной строки - Python видит, что если такая же строка, то возвращает тот же самый объект (копию не делает)
copy1 = id(copy), id(msg3)      # Эти id одинаковые, Python видит, что если такая же строка, то возвращает тот же самый объект
print (copy1)

# Если строка меняется, срез меняет строку, то создается новый объект
copy = msg3[6:]                  # Создается копия данной строки, возвращается новый объект 
copy2 = id(copy), id(msg3)       # Эти id разные - получаем новый объект
print (copy2)

# Срез - шаг следования - получим строку, но через символ
str19 = msg3[::2]
print (str19)
# Срез - шаг следования - граничные значения
str19 = msg3[:5:2]      #  берем срез от 0 до 5, внутри среза делается шаг равный 2
print (str19)
str20 = msg3[6::2]      #  берем срез от 6 до конца строки, с шагом 2
print (str20)
str21 = msg3[1:6:2]     #  берем срез от 1 до 6, с шагом 2
print (str21)
str22 = msg3[::-1]     #  берем срез - все буквы наоборот записываются
print (str22)

# Замена строк , букв - создается новая строка с нужным содержимым
# Преобразование строки W -> w , l - delate
myStr = msg3[:6]+"w"+msg3[7:9]+msg3[10:]
print (myStr)






## c_o_n_s_o_l_e ##

#  Hello1 Hello1  Hello1
#  Hello1 Hello1
#  Hello1
#  Hello1 Hello1  Hello1 
#  Hello2 Hello2 Hello2 Hello2
#  Hello1Hello1Hello1
#  WorldWorld
#  Hello1 Hello1  Hello
#  World Hello2 Hello2 Hello2
#  Helloworld
#  Hello world
#  число = 5
#  True
#  hey hey hey hey hey hey hey hey hey hey 
#  40
#  8
#  12
#  True
#  True
#  False
#  True
#  False
#  Введите пароль: pass
#  Вход в систему разрешен
#  True
#  1090
#  1076
#  H
#  !
#  !
#  b
#  d
#  World
#  llo
#  Hello
#  World!
#  Hello World!
#  (2685077101360, 2685077101360)
#  (2685077100848, 2685077101360)
#  HloWrd
#  Hlo
#  Wrd
#  el 
#  !dlroW olleH
#  Hello word!
