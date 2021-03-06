# if(<условное выражение>): оператор
# if<условное выражение>: оператор

# Записываем число -> преобразовываем его к вещественному типу -> далее делаем проверку -> если это число отрицательное -> меняем знак этого числа - > выводим модуль числа в консоль
x = float(input())
if(x < 0) : x = -x
print(x)

# a > b  Истинно, если a > b
# a < b  Истинно, если a < b
# a >= b Истинно, если а > или равно b
# a <= b Истинно, если а < или равно b
# a == b Истинно, если a равно b ( для сравнения используется двойной знак равенства)
# a != b Истинно, если а не равно b
# a = b  Это присваивание (Один знак равенства)

print(2 > 1)
print(2 == 1)
print(2 != 1)

# Булевое значение принимает Result
result = 7 > 5
print(result)

# Сравнение строк
print ('T' > 'R')
print ('C' > 'B') 
print ('Sunny' > 'Sun')

# IF - определяем знак введенного числа
# Вводим некое значение с клавиатуры
f = int(input())
if f < 0 : print("x отрицательное число")
if f >= 0 : print("x неотрицательное число")

# Если истина выполняется if g < 0, если условие ложно выполнится другой оператор 
g = int(input())
if g < 0 :
    print("g отрицательное число")
else:
    print("g неотрицательное число")

# elif (else if - вторая проверка) - все условия взаимоисключающие
# t > 0 , t < 0, t == 0 
# if - elif - elif - elif ... - elif - else 
t = int(input())
if t < 0 :
    print("t отрицательное число")
elif x > 0:
    print("t положительное число")
else:
    print("t равен 0")

# Операторы внутри некоторого условия
# Определяем не просто знак числа
# В переменной sgn сохранить -1 для отрицательных чисел, 1 для положительных
# По условию можем выполнять несколько операторов
r = int(input())
sgn = 0
if r < 0 :
    sgn = -1
    print("r отрицательное число", sgn)
elif r > 0:
    sgn = +1
    print("r положительное число", sgn)
else:
    print("r равен 0", sgn)

# Тернарный условный оператор result = значение if <условие> else значение 2
# Некоторому условию result присваивается значение 1, если <условие> истина , иначе присваивается значение 2
age = 15
accessAllowed = True if age >=18 else False
print(accessAllowed)

age1 = 18
accessAllowed1 =  age1 >=18 
print(accessAllowed1)

# Проверка попадания переменной x в диапазон [2 ; 7]
# Условие истино когда x в этом диапазоне чисел
# Две проверки x >= 2 и x <= 7
# Если истина d >=2 and d <= 7 - то истина все условие, если ложно хоть одно условие, ложно все условие
d = 4
if d >=2 and d <= 7 : print("x не попаает в [2 ; 7]")
else: print ("x попаает в [2 ; 7]")

# Проверка, что x не принадлежит этому диапазону - проверка на непопадание в диапазон
d1 = 40
if (d1 >=2 or d1 <= 7) : print("x не попаает в [2 ; 7]")
else: print ("x попаает в [2 ; 7]")

# x >=2 and x<=7 - истинно, если истина каждое подусловие x >=2 and x<=7. Ложно - ложно хотя бы одно
# x < 2 or x > 7 - истинно, если истина хотя бы одно подусловие x < 2 or x > 7. Ложно - когда оба ложны

# Комбинирование проверок в любом сочетании
# Если б не было круглых скобок это было бы уже другое условие

u = 4; i = -2
if u>=2 and i <= 7 and (i < 0 or i > 5):
    print("u попадает в [2; 7], i не попадает в [0; 5]")

# Внутри условия можем прописывать одиночные выражения
# Если qq , или если не 0, или если строка "0", или не пустая строка "", или ww , или не z
# Все эти выражения истина -> любое число неравное 0 - Истина
# Число 0 дает ложь, и мы сделали противоположную проверку, что это будет не 0, в итоге not 0 превратился в истину
# Не пустая строка if("0") с числом 0 это будет истина
# Пустая строка дает ложь, но мы поставили (not "") - поэтому даст истину
# ww = "True" - поэтому истина
# ee = "False" - делаем обратную проверку if(not ee) - поэтому истина

qq = 4; ww = True; ee = False
if (qq): print ("qq= ", qq, " дает true")
if(not 0): print("0 дает false")
if("0"): print("строка 0 дает true")
if(not ""):print("пустая строка дает false")
if(ww): print("y = true дает true")
if(not ee): print("ee = false дает false")

# 1. Любое число отличное от 0, дает True. Число 0 преобразуется в False
# 2. Пустая строка - это False. Любая другая строка с символом - это True
# 3. С помощью оператора not можно менять условие на противоположное ( False превращать True)
#     Приоритеты: 1- not 2 -and 3 - or 



## c_o_n_s_o_l_e ##

#  -5
#   5.0
#   True
#   False
#   True
#   True
#   True
#   True
#   True
#   6
#   x неотрицательное число
#   0
#   g неотрицательное число
#   -7
#   t отрицательное число
#   0
#   r равен 0 0
#   False
#   True
#   x не попаает в [2 ; 7]
#   x не попаает в [2 ; 7]
#   u попадает в [2; 7], i не попадает в [0; 5]
#   qq=  4  дает true
#   0 дает false
#   строка 0 дает true
#   пустая строка дает false
#   y = true дает true
#   ee = false дает false
