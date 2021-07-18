     #  -  Рассмотрим как модули внутри пакета могут импортировать любые данные
     #  -  Внутри модуля exp выполним импорт модуля funcs
     #  -  Error - при import funcs внутри модуля exp
     #  -  Необходимо указывать имя пакета  packrand.funcs 
import packrand.funcs

     #  -  Импорт вторым способом 
from packrand import funcs 
     #  -  если название пакета изменится в будущем, прийдется внутри модуля,
     #  -  где происходят такие импорты менять имя пакета приходят

     #  -  на помощь Относительные способы импортирования 
from . import funcs
     #  -  .  говорит о том, что мы берем модуль funcs из текущего пакета
     #  -  из того же пакета, что находится ex.py 

     #  -  Импорт вторым относительным способом
from .funcs import getRand
     #  -  .funcs модуль из которого дальше будем брать данные, конкретная ф-ция getRand кот. импортируется в данный модуль
     #  -  . благодаря . уходим от привязки пакета и можем не беспокоиться об его изменении в будущем
     #  -  Это преимущество относительного импорта


     
def randExp():
    return "Генерация экспоненциальных СВ"
