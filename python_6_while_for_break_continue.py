# while <условие>: заголовок
# оператор 1 - тело цикла
# оператор 2 - тело цикла
# Итерация - однократное выполнение тела цикла

# Задаем переменную S = 0, в переменной S будем хранить значение суммы
# обозначаем счетчик i = 1
# записываем оператор тела цикла while и говорим что он будет работать до тех пор,
# пока счетчик i <= 1000
# внутри цикла два оператора, значение S суммы 1/i
# на каждой итерации i будет меняться, мы будем добавлять нужное слогаемое
# i увеличиваем на 1. i сначала = 1, потом 2, потом 3
# слогаемые суммируем и выводим в консоль
# цикл while работает до тех пор, пока истина i <=1000 , условие ложно, цикл завершил свою работу
S = 0; i=1
while i <= 1000:
    S += 1/i
    i += 1
print(S)

P = 0; j=1
while j <= 1000 and P < 5: # цикл завершится, когда сумма превысит значение 5
    P += 1/j
    j += 1
print(P)

# вечный цикл
# S = 0; i = 1
# while 1 : S += 1      // 1 это true 
# print(S)

# Любой оператор цикла можно прервать оператором break в теле цикла (досрочное прерывание) => управление переходит к следующим операторам
# break  - досрочное завершение цикла (любого)
# Если else стоит после  while блока операторов
# Считаем сумму ряда 1/q -> делаем вначале проверку if q == 0: break ->
# -> если q=0, на ноль делить нельзя и мы прерываем работу цикла -> в этом случае выводим значение получившейся суммы ->
# -> сообщение print("Сумма вычислена корректно") не появится в консоле -> else если возникнет break не выполнится

Sum = 0; q = -10
while q < 100 :
    if q == 0: break
    Sum += 1/q
    q = q + 1
else:
    print("Сумма вычислена корректно")
print(Sum)

# continue - пропуск последующих операторов тела цикла и переход к следующей итерации
# Предположим мы хотим перебрать все целые числа от -4 до +4 (кроме 0)
Sum1 = 0; r = -5
while r < 4 :
    r = r + 1
    if r == 0: continue     # проверка, если r = 0, вызывается continue
    print(r)                # данные операторы пропускаются
    Sum1 += 1/r             # данные операторы пропускаются
print(Sum1)

# for - оператор цикла
# перемеенная y последовательно будет принимать значение чисел, и затем в консоль будем выводить значение этих чисел в **2
for y in 1, 5, 2, 4:
    print(y**2)

# range - перебрать значение по поряду (начальное значение, шаг, конечное значение)
# range - генератор последовательности range (start, stop, step) _ шаг 1 - defoult

for z in range (1,5,1): # [1; 5) - от 1 до 5 (последнее значение = 4) (-1 шаг_конечное значение 5 не может быть достигнуто, возвратится пустая последовательность)
    print(z)

# если нам нужна последовательность от 5 до 1
# поставим начальное значение 5, 0 - 0 не будет входить в диапазон и последнее значение 1

for m in range (5,0,-1): # [1; 5) - от 5 до 1 (последнее значение = 4)
    print(m)

for v in range (5):   # выводит от 0 до 4
    print(v)

# Запишем программу подсчета суммы ряда с помощью цикла for
# Переменная Sum2 ее начальное значение 0, далле цикл for, у него счетчик с
# счетчик с меняется от 1 до 1000, шаг 1, подсчитываем сумму ряда и выводим ее в консоль

Sum2 = 0
for c in range(1, 1001, 1):
    Sum2 += 1/c
print (Sum2)

# Выведем в консоль значение линейной функции y=f(x)=kx+b, будут меняться x = 0;0.1;0.2;...;0.5
# Для перебора значений счетчика x, можно использовать списки сформированные ранее в программе
# Задали значение k и b
# Задали значение x списку

k = 0.5; b = 2
lst = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
for x in lst:                       # Переменная x в цикле for будет принимать эти значения
    print(x*k+b)                    # Вычисляется значение линейной функции и выводится в консоль

# Есть строка - переберем символы строки определенным образом
# Строка выступает как список, перебрали каждый символ этой строки

msg = "Hello World!"
for x in msg:
    print(x)

# Вложенные циклы - перебор элементов матрицы

# while условие
#    операторы 1...M 
#       while условие :
#           операторы 1...N
#     операторы M+1...N

# Рассмотрим двумерный массив со значениеми 1 2 3 и 4 5 6 (3 столбца и 2 строчки)
# Задаем две переменные N = 2; M = 3
# Перебираем элементы этого массива range - переменная ii будет пробегать значение от 0 до 1 ->
# N=2 2-не будет входить в диапазон - переменная jj будет пробегать значение от 0 до 2 ->
# с помощью функции print (A[ii] [jj]) выводим элементы этой матрицы 
A = [ [1, 2, 3], [4, 5, 6] ]
N = 2; M = 3
for ii in range (N) :
    for jj in range (M) :
        print (A[ii] [jj], end='')          # для цикла for вложенного end='' - именованый параметр для вывода значений в виде матрицы
    print()                                 # для цикла for

# Посчитать суммму двойного ряда
# Вспомогательные переменные, два цикла один вложен в другой -> считаем сумму -> выводим в консоль
# N=5 (N+1) 1+2+3+4+5 = 15
# M=10 (M+1) 1+2+3+4+5+6+7+8+9+10 = 55 
# 15 * 55 = 825 

SS = 0; MM = 10; NN = 5
for iii in range(1, NN + 1):
    for jjj in range(1, MM + 1):
        SS +=iii *jjj
print(SS)




## c_o_n_s_o_l_e ##

#  7.485470860550343
#  5.002068272680166
#  -2.9289682539682538
#  -4
#  -3
#  -2
#  -1
#   1
#   2
#   3
#   4
#   2.7755575615628914e-16
#   1
#   25
#   4
#   16
#   1
#   2
#   3
#   4
#   5
#   4
#   3
#   2
#   1
#   0
#   1
#   2
#   3
#   4
#   7.485470860550343
#   2.0
#   2.05
#   2.1
#   2.15
#   2.2
#   2.25
#   H
#   e
#   l
#   l
#   o
 
#   W
#   o
#   r
#   l
#   d
#   !
#   123
#   456
#   825

