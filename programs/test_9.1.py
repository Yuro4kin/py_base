

# 1. Дан список [-1, 0, 5, 3, 2]
# Необходимо изменить его, увеличив каждое значение на 7.2.


# Изменим элементы списка внутри цикла for - увеличим каждое значение на 7.2
digs = [-1, 0, 5, 3, 2]
for x in range(5):       # range(len(digs)):         # x будет пробегать значение от 0 до 4, функция range последовательность от 0 до 4 с шагом 1
    digs[x] += 7.2       # digs[x] = digs[x]+7.2     # далее используем x как индекс списка digs => присваиваем новое значение - увеличиваем на 7.2
print("Увеличено каждое значение на 7.2: ", digs)


