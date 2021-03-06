# Локальная переменная, глобальная переменная  - global, nonlocal

# Глобальная переменная – это переменная доступная в любом месте программы.
a = 5
N = (100, )                     # кортеж, с одним значением 
WIDTH, HEIGHT = (1000, 500)     # задай две переменные и присвой им значение
                                # плохой стиль программирования
# допускается использовать глобальные константы, доступные во всей программе
# имена констант записывать заглавными буквами (WIDTH, HEIGHT - чтобы отличать их от обычных не глобальных, локальных переменных)

# Локальные переменные – это переменные, объявленные (ДОСТУПНЫ внутри любого ЭТОГО блока программы)

def myFunc(b):                  # задали функцию myFunc, с одним аргументом b, будет пробегать некоторое значение
    # a = 10                    # error
    global a                    # если нужно работать с глобальной переменной, эта строчка говорит, что дальше будем работать с переменной a как с глобальной переменной, а не создавать новую внутри функции
                                # использовать - global a - если отсутствует соответствующая локальная переменная 
    a = 10                      # создали новую локальную переменную с именем глобальной a
    for x in range (b):         # в диапазоне от 0 до b-1
        n = x+1                 # нутри цикла for создаем переменную n со значением x+1  
        print(n, end =" ")      # выводим ее в консоль

#print(x)                       # error - доступны только внутри функции myFunc и не существуют за ее пределами
    print(x)                    # внутри функции переменная x существует
    print(n)                    # переменная n существует за пределами цикла
myFunc(6)                       # функция это отдельный блок программы, поэтому переменные b, x, n - это все локальные переменные   // вызов функции
                                # все эти локальные переменные b, x, n - доступны внутри функции  myFunc

print("\n\n%d - global var "%(a)) # после вызова функции выведем значение a, изначально было = 5, внутри функции поменяли на 10
                                  # повлияет ли эта операция на значение глобальной переменной? Ответ: не повлияла, т.к. создали новую локальную переменную с именем глобальной a 

# Все переменные объявленные веутри цикла for, while - доступны и за пределами этого цикла
# Операторы цикла не образуют свои области видимости
# Как работать с глобальной переменной внутри этой функции

name = "Tom"                    # глобальная переменная
 
def say_hi():                   # задали ф-цию
    print("Hello", name)        # вызываем print "Hello" с переменной name, которая будет ссылаться на глобальную переменную name (взяла переменную из глобальной области видимости)
 
def say_bye():                  # задали ф-цию
    name = "Bob"                # создаем локальную переменную с именем name
    print("Good bye", name)     # вызываем print "Hello" с локальной переменной name, которая будет ссылаться на локальную переменную name (ф-ция взяла переменную из локальной области видимости)
 
say_hi()
say_bye()

# Алгоритм поиска переменной - сначала переменная name ищется внутри функции, если не находится, то переходим на уровень выше в глобальную область и ищем переменную. Если нашли внутри функции локальную переменную, то поиск дальше не продолжается.

# Режим работы с локальными переменными с использованием ключевого слова - nonlocal -

# nonlocal

x = 0                           # глобальная переменная x
def outer():
  # global x                    # если нам нужно работать с глобальной переменной, значение переменной x изменится
  # nonlocal x                  # error - нельзя работать так с глобальной переменной
    x = 1                       # локальная переменная x внутри функции outer()
    def inner():
        nonlocal x              # будем работать с переменной x объявленной уровнем выше
        x = 2                   # локальная переменная x внутри вложенной функции inner()
        print("inner:", x)
 
    inner()
    print("outer:", x)
 
outer()
print("global:", x)             # каждая ф-ция взяла свою переменную внутри своей области видимости
