# Convert

# Кортеж – это упорядоченная неизменяемая коллекция произвольных данных.
# Кортеж отличается от списка тем что он неизменяемый.

# функции tuple , list ( с списка в кортеж, с кортежа в список)
# функция tuple - создавать кортежи на основе любых упорядоченных списков
j = tuple([1, 2, 3])      # передали в качестве аргумента список
jj = tuple("Привет мир")  # передали строку, строка это КОЛЛЕКЦИЯ из символов
print(j, type(j))
print(jj, type(jj))

jone = [4, 5, 6]
jtwo = tuple(jone)
print(jone, type(jone))
print(jtwo, type(jtwo))

# обратная операция, из кортежа получим список - функция list
k = (1, 2, 3)
lstK = list(k)
print(k, type(k))
print(lstK, type(lstK))

