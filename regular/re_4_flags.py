import re

# проверки и flags
# The Income Tax Department NEVER asks for your PIN numbers,
# passwords or similar access information for credit cards,
# banks or other financial accounts 

# недостаток re - они способны находить соответствия там, где это не предполагалось
# выражение найдет подстроку «income» в слове «incomes».
text = "incomes tax"
match = re.findall(r"profit|acquisition|income", text)
print(match)



# Нам нужно находить слово income как самостоятельное, а не как часть другого слова
# Сделаем дополнительную проверку, границу слова
text_1 = "incomes tax, income"
match_1 = re.findall(r"profit|acquisition|\bincome\b", text_1)
print(match_1)
# \b - найдет слово как самостоятельный элемент в этом предложении

# Вот пример простейшей проверки. Если нужно для всех трех вариантов выполнять
# такую проверку, то это можно записать так:
match_2 = re.findall(r"\bprofit\b|\btax\b|\bincome\b", text_1)
print(match_2)


# или проще, с помощью группировки вариантов:
match_3 = re.findall(r"\b(?:profit|tax|income)\b", text_1)
print(match_3)

# re - рассматривается как единая группа, к этой группе 
# выполняем проверку до соответствия границы слова.
# ?: используем несохраняющую группу
# Обратите внимание, проверки не являются частью совпадения строки по шаблону,
# они лишь проверяют определенные условия, поэтому сам по себе символ \b
# в строке text не ищется, а определяется граница слова в шаблоне, где он записан.
# \b - к шаблону не имеет отношения
# В общем случае, для регулярных выражений доступны следующие проверки:

# В общем случае, для регулярных выражений доступны следующие проверки:

# Символ                        Описание
#   ^           Начало текста (с флагом re.MULTILINE – начало строки)
#   $           Конец текста (с флагом re.MULTILINE – позиция перед символом переноса строки \n)
#   \A          Начало текста
#   \b          Граница слова (внутри символьных классов [] соответствует символу BACKSPACE)
#   \B          Граница не слова (зависим от флага re.ASCII)
#   \Z          Конец текста
# (?=exp)       Проверка на совпадение с выражением exp продолжения строки. При этом позиция поиска не смещается на выражение exp (опережающая проверка).
# (?!exp)       Проверка на несовпадение с выражением exp продолжения строки. (Также опережающая проверка).
# (?<=exp)      Проверка на совпадение с выражением exp хвоста уже обработанной (проверенной) строки. Она также называется позитивной ретроспективной проверкой.
# (?<!exp)      Проверка на несовпадение с выражением exp хвоста уже обработанной (проверенной) строки. Еще она называется негативной ретроспективной проверкой.

#Рассмотрим примеры использования этих проверок.
#Предположим, у нас имеется вот такой многострочный текст:
# И мы хотим выделить содержимое тега script. 

text_2 = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""

match_4 = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text_2, re.MULTILINE)
print(match_4)

# ^ Здесь сначала проверяется, что тег script записан вначале строки
# (флаг MULTILINE указывает, чтобы проверка ^ соответствовала началу каждой строки).
# <script проверяется запись тега script: он может быть с атрибутами type .*?,
# *? квантификатор воспринимаем как минорный, т.е.поиск минимальной последовательности длины
# ([\w\W]+) - два класса, выделяем все, что будет стоять после тега и все строчки до тех пор пока не встретим
# закрывающий тег </script> (?=</script>) - будем искать по шаблону совпадение пока не встретим </script> 
# далее встретили </script> прерываем проверку, и то что получили содержимым и есть результатом ([\w\W]+)

#["\nlet o = document.getElementById('id_div');\nconsole.log(obj);\n"]
# Получили \n - перевод строки, две строчки

# Обычная проверка - это опережающая проверка
# Проверка на совпадение с выражением </script> - захвачен шаблоном.
# Она также называется позитивной ретроспективной проверкой - это когда все уже вошло в шаблон.
match_5 = re.findall(r"^<script.*?>([\w\W]+)(?<=</script>)", text_2, re.MULTILINE)
#                                     . - точка не включает символ переноса строки
#                                       даст пустую коллекцию, т.к. символ \n встречается сразу же после тега script.
print(match_5)

# Нужно выбрать все пары ключ=значение
# Это можно сделать с помощью такого правила:
match_6 = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text_2, re.MULTILINE)
print(match_6)
# ([-\w]+) - выделяем ключ, который может состоять из символов, дефис может быть http-
# [ \t]*=[ \t] - равно, но перед ним могут быть пробелы или Tab
# ([^\"']+) - в кавычки выделяем, что будет являться содержимым нашего ключа, прописали симв. класс все символы, кроме " и '
# (?<![ \t]) - ретроспективная проверка, проверяет, если в конце выделяемых данных появляется пробел или символ Tab \t
#              то мы останавливаемся и полученное значение идет в значение атрибута



# Добавим пробел в http-equiv="Content-Type " - результат, пробел игнор благодаря ретроспективной проверке
# Error - добавляет пробел, если удалить ретроспективную проверку (?<![ \t])
# Error  шаблон
match_7 = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"'](.+?)(?<![ \t])[\"']", text_2, re.MULTILINE)
print(match_7)
# Error выделение ('http-equiv', 'Content-Type " content='), если бы пробела не было,
# поиск выражения был бы нормальным.
# Если удалить ретроспективную проверку, то в выражении будет пробел, но записано правильно.
# (?<![ \t]) - игнорируется пробел, если удалить р.п., пробел появляется
# (.+?) - выделять все произвольные данные, квантификатор в минорном режиме, выделение некорректно
# Неверный шаблон - пробел учитывается, р.п. учитывается и захватываем все значения до ближайшей "


# Определим re для выделения пар
# ключ="значение"   или   ключ=значение
# в тексте ниже есть ключ align=center, значение которого записано без кавычек
text_3 = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<p align=center>Hello World!</p>
</body>
</html>"""

# (?P<q>[\"'])   -  проверка наличия группирующего выражения,
#                   например если используем такую группу, то далее можем проверить
# (?(id|name)yes_pattern) - если группа была найдена, то выполнить этот шаблон yes_pattern
# (?(id|name)yes_pattern|no_pattern) - yes_pattern – шаблон, выполняемый при наличии группы;
#                                      no_pattern – шаблон, выполняемый при отсутствии группы

match_8 = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", text_3, re.MULTILINE)
print(match_8)
# ([-\w]+) - выделяем атрибут 
# [ \t]*=[ \t] - знак равно 
# (?P<q>[\"']) - сохраняющая группа
# ? - квантификатор говорит, что данная группа может быть не обязательной, кавычка мжет быть, а может и не быть
# (?(q) - проверяем, если наша кавычка присутствовала, то выполняем следующий шаблон
# ([^\"']+(?<![ \t])) - мы будем выделять значение атрибутов в "", а иначе |
# ([^ \t>]+)) - выделяем значение атрибута, пока не встретим пробел или Tab \t или закрыв. угл. скобку >

# Выделяются атрибуты и последний align со значением center.
# Благодаря шаблону в котором прописали условие смогли выделить align=center


#  набор флагов, которые можно назначать к регулярным выражениям:
#   Флаг                    Описание
# re.A или re.ASCII         При этом флаге проверки \b, \B, \s, \S, \w и \W
#                           действуют так, как если бы они применялись к тексту,
#                           содержащему только символы ASCII (по умолчанию используется
#                           Юникод re.U / re.UNICODE и лучше оставаться в этом режиме)

# re.I или re.IGNORECASE    Проверка без учета регистра символов

# re.M или                  Влияет на проверки ^ и $. 
# re.MULTILINE              Начало ^ считается началом строки (сразу после символа
#                           \n или начало текста). Конец $ считается в позиции
#                           перед \n (или конец строки)

# re.S или                  При установке этого флага символ. также включает символ перевода строки \n.
# re.DOTALL

# re.X или
# re.VERBOSE                Позволяет включать в регулярные выражения пробелы и комментарии

# re.DEBUG                  Включает режим отладки при компиляции регулярного выражения

# аналог предыдущей программы с флагами re.VERBOSE
match_9 = re.findall(r"""([-\w]+)             #выделяем атрибут
                   [ \t]*=[ \t]*            #далее, должно идти равно и кавычки
                   (?P<q>[\"'])?            #проверяем наличие кавычки
                   (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))     #выделяем значение атрибута
                   """, 
                   text_3, re.MULTILINE|re.VERBOSE) # | - или комбинируем несколько флагов
print(match_9)




# Флаги можно указывать и непосредственно внутри выражения, используя синтаксис:
#           (?flags)
# где flags – один или несколько флагов. Причем, их имена, следующие:
# 
# a – то же самое, что и re.ASCII;
# i – соответствует re.IGNORECASE;
# m – для re.MULTILINE;
# s – для re.DOTALL;
# x – для re.VERBOSE.

# используем два флага в одной конструкции
text_4 = "Python, python, PYTHON"
match_10 = re.findall(r"(?im)python", text_4)
print(match_10)


