import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Мой номер: 415-555-4242.')
print('Найденный номер телефона: ' + mo.group())
