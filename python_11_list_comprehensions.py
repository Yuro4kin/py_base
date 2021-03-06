
# List comprehensions - иногда это переводят как «генераторы списков»
# Списки: срезы и методы
# List comprehensions - это инструмент

# Рассмотрим пример:
# Нам нужно создать список, состоящий из квадратов чисел, определенных от 0 до N-1
list = []                       # создали пустой список
N = 10                          # задали N = 10
for x in range(N):              # цикл - х меняется от 0 до N-1
     list.append(x**2)          # добавили последний элемент списка x**2
print(list)


# А теперь этот же алгоритм с использованием list comprehensions.
# Формируем список x**2, сам x будет меняться в диапазоне N-1
# сначала указываем, что будем возводить некое значение x**2
# переменная x существует только внутри этого списка и пропадает после его создания
Nn = 10
list1 = [x**2 for x in range(Nn)]
print(list1)
# Работать будет быстрее предыдущей программы, т.к. Python оптимизирует работу таких конструкций



# Создадим список из квадратов четных чисел
list2 = []                       # создали пустой список
Np = 10                          # задали N = 10
for x in range(Np):              # цикл - х меняется от 0 до N-1
    if x%2 == 0:                 # если x нацело делится на 2, значит x четное число
        list2.append(x**2)       # добавили последний элемент списка x**2
print(list2)



# После цикла можем записывать любые условия
# условие истина - формируется новый элемент списка
# вместо возведения в степень можно писать любой функционал
list3 = []                                      # создали пустой список
Nq = 10                                         # задали N = 10
list3 = [x**2 for x in range(Nq)if x%2 == 0]    # добавим условие: если остаток от деления 
print(list3)                                    # то будем добавлять в список x**2, добавляем квадраты только четных чисел




print("/n")
# вместо возведения в степень можно писать любой функционал или записать просто x:
# получим последовательность четных чисел
list4 = []                                      # создали пустой список
Nb = 10                                         # задали N = 10
list4 = [x for x in range(Nb)if x%2 == 0]    # добавим условие: если остаток от деления 
print(list4)                                    # то будем добавлять в список x четных чисел   




# Формула вычисления значений линейной функции:
list5 = []                                      # создали пустой список
Nd = 10                                         # задали N = 10
list5 = [0.5*x+1 for x in range(Nd)]            # значения просто линейной функции 
print(list5)




# Также можно оперировать не только числами, но и другими типами данных, например, строками.
# List comprehensions - со строками - генерирование, формирование новых списков
cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]     # список в виде строк
list6 = [city for city in cities if len(city) < 7]                  # формируем новый список, который будет состоять из тех названий городов, длины которых меньше 7
print(list6)



# Алгоритм - разбиваем целое положительное число по цифрам

# Есть число 432, нужно выделить каждую цифру этого числа ->
# вычисляем остаток от деления, деленное на 10, получаем последнюю цифру 2
# запоминаем 2 ->  отбрасываем число 2
# 432 % 10 = 2      
# ->  отбрасываем число 2
#
# выполняем целочисленное деление на 10, остаток 43
# 432 // 10 = 43
#
# остаток от деления 3
# 43 % 10 = 3
#- >  отбрасываем число 3
#
# выполняем целочисленное деление на 10, остаток 4
# 43 // 10 = 4
#
# остаток от деления 4
# 4 % 10 = 4
#- >  отбрасываем число 4
#
# выполняем целочисленное деление на 10, остаток 0
# 4 // 10 = 0

# Шаг 1: 432 % 10  = 2
#        432 // 10 = 43

# Шаг 2: 43 % 10   = 3
#        43 // 10  = 4

# Шаг 3: 4 % 10    = 4
#        4 // 10   = 0


# Алгоритм обработки элементов списка.
# Алгоритм - разбиваем целого положительного числа по цифрам.
xx = int(input("Введите целое положительное число: "))     # вводим некое целое число с клавиатуры
digs = []                                                  # формируем список который будет содержать эти цифры
while xx:                                                  # цикл while от x - будет работать до тех пор, пока x неравен 0 (0 - ложь, не ноль - это истина)
    digs.append(xx % 10)                                   # добавляем последнюю цифру нашего числа x, шаг 1 - выполняется первая операция,   
    xx = xx//10                                            # идет целочисленное деление на 10, отбрасываем последнюю цифру числа - и цикл повторяется переходим к шагу 3, пока не получим значение 0
print(digs)                                                # 4567 - [7, 6, 5, 4] - выделили последнюю цифру 7 и дошли до первой 4





# Алгоритм - разбиваем целое положительное число по цифрам - сортировка по порядку следования
xxx = int(input("Введите целое положительное число: "))   # вводим некое целое число с клавиатуры
digs1 = []                                                 # формируем список который будет содержать эти цифры
while xxx:
    #digs.append(xxx%10)   Берем последнюю цифру числа
    digs1 = [ xxx % 10 ] + digs1    # Чтобы цифры шли по порядку: слева-направо, мы их будем добавлять в начало списка
    xxx = xxx // 10               # отбрасываем последнюю цифру числа
print(digs1)


# НЕ ЗАПУСКАЕТСЯ РАБОТАЕТ АВАРИЙНО -- ЗАПУСКАТЬ В ОТДЕЛЬНОЙ ПРОГРАММЕ
# Алгоритм - программа, меняющая порядок следования элементов в списке
# 1, 2, 3, 4, 5, 6, 7  - необходимо вывести в обратном порядке
# Программа - reverse

#N = 11                                     # число элементов в этом списке
#A = list(range(N))                         # формируем список из целых чисел от 0 до Nn-1(функция list с диапазоном от 0...N-1)
#print(A)                                   # выводим список в консоль

#for i in range(N//2):                      # цикл, переменная i определяет положение индексов
#    A[i], A[N-i-1] = A[N-i-1], A[i]   # цикл, доходим до середины списка -> обмен данными между соответствующими элементами
#print(A)




# Алгоритм - сортировка методом выбора по росту
# программа - сортировка методом выбора по росту

H = [2,2,-1,-5,55,34,0,10]                  # Список из чисел
N = len(H)                                  # Определили длину этого списка
for z in range(N-1):                        # Цикл отвечает за положение индекса 1
    for j in range(z+1, N):                 # Цикл отвечает за положение индекса 3 - сравниваемого
       if H[z] > H[j]:                      # Внутри вложеного цикла проверили, рост индекса 1 больше индекса 4 -> если это так, они меняются местами
          H[z],H[j] = H[j],H[z]
print(H)



# Алгоритм Евклида (поиск наибольшего общего делителя двух чисел)
# Теория. Пусть даны два натуральных числа a и b, для которых требуется найти НОД. Далее, такой алгоритм:
# пока a не равно b
#        находим большее среди a и b
#        уменьшаем большее на величину меньшего
# выводим полученное равное значение преобразованных величин a и b
# Например, пусть у нас два числа: a=18 и b=24 и далее по алгоритму:
# Реализуем этот алгоритм на Python:
a = int(input("Введите 1-е натуральное число: "))
b = int(input("Введите 2-е натуральное число: "))
sa = a;
sb = b
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print("НОД(%d, %d) = %d" % (sa, sb, a))






# Быстрый алгоритм Евклида
# Но у этого алгоритма есть один существенный недостаток: если мы введем два вот таких числа:
# 100000000 и 2
# то этот алгоритм начнет довольно долго работать и понятно почему, здесь мы получим большое количество вычитаний 2. Эти вычитания будут происходить до тех пор, пока двойка укладывается в оставшееся число. И мы здесь без всяких вычитаний сразу можем сказать, что на последнем шаге будет вот такая операция:
# 4-2 = 2
# После чего оба числа станут равными и НОД будет равен двум. Так вот, чтобы без лишних операций сразу определить на сколько будут отличаться два числа после серии вычитаний, достаточно взять целый остаток от деления. Например:
# 100000000 % 2 = 0
# Это значит, что большее число можно полностью составить из суммы двоек. Следовательно, они оба делятся на два нацело и их НОД равен 2. Хорошо, а если вместо 2 взять 3. В этом случае имеем:
# 100000000 % 3 = 1
# и далее уже можно рассматривать два числа: 3 и 1. Причем, для них также можно выполнить такую же операцию:
# 3 % 1 = 1
# 1 % 1 = 0
# Все, получили НОД, равный 1. И смотрите, здесь на каждой итерации большее число делится на меньшее. Поэтому быстрый алгоритм Евклида можно записать так:
# пока меньшее число больше 0
#        большему числу присваиваем остаток от деления на меньшее число
# выводим большее число
# Реализуем этот алгоритм. И договоримся, что большее число будем хранить в a, меньшее – в b.
a1 = int(input("Введите 1-е натуральное число: "))
b1 = int(input("Введите 2-е натуральное число: "))
sa = a1
sb = b1
b1 = min(sa, sb)
a1 = max(sa, sb)
while b1:
    a1, b1 = b1, a1 % b1

print("НОД(%d, %d) = %d" % (sa, sb, a1))