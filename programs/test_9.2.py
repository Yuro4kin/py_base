

# 2. Пользователь вводит с клавиатуры N значений (строки или числа)
# На их основе сформировать список, состоящий из продублированных элементов
# (Например, из значений 1, 5, "abc" формируется список [1, 1, 5, 5, "abc", "abc"])


digs1 = [0]*100            # ЗАДАВАТЬ
N = 0; x = 0
while x >= 0:
   x = int(input("Введите целое число: "))
   digs1[N] = [x]*2        # ИЗМЕНЯТЬ   
   if x >= 0: N += 1       # Число должно соответствовать числу введенных чисел
                           # Если х > 0, то N нужно увеличить на 1
   print("Сформированный список из значений: ", digs1)



a = input('Введи значение: ').split()
b = []
for i in a:
    b.append(i), b.append(i)
print(b)


B = input('Введите значения:  ').split(',')
A = []
for i in B:
    A += [i]*2
print(A)
