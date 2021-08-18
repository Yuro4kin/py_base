# 2. Пусть имеется вот такая строка: "int = целое число, dict=словарь, list=список, str=строка, bool=булевый тип"
#    Требуется из нее создать словарь с ключами:  int, dict, list, str, bool и соответствующими значениями.

# 1
string = "int=целое число, dict=словарь, list=список, str=строка, bool=булевый тип"
my_dict = dict([n.replace("=", ",").split(",")  for n in string.split(", ")])
print(my_dict)

# 2
string = 'int=целое число, dict=словарь, list=список, str=строка, bool=булевый тип'
print(dict(([i.split('=') for i in string.split(',')])))

# 3
str = 'int= целое число, dict=словарь, list=список, str=строка, bool=булевый тип'
d = dict([[b.strip() for b in k] for k in [t.split('=') for t in str.split(',')]])
print(d)


#4
x = "int=целое число, dict=словарь, list=список, str=строка, bool=булевый тип"
s = x.replace(', ', '=').split('=')
d = {}
for i in range(len(s)):
    if i % 2 == 0:
        d[s[i]] = s[i + 1]
print(d)


#5
a = 'int = целое число, dict = словарь, list = список, bool = булиевый тип'
a = (a.split(","))
print(a)
for i in range(len(a)):
    a[i] = a[i].split("=")
a = dict(a)
print(a)