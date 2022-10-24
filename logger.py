
from datetime import datetime as dt
from time import time
# записываем в лог вход и выход пользователя
def register_logger(data=''):
    with open('log_staff.txt', 'a',encoding="utf8") as file:
        file.write('{} Зафиксировано событие {}\n'
                    .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))
# записываем в лог вариант меню с запросом пользователя
def menu_logger(data=''):
    with open('log_staff.txt', 'a',encoding="utf8") as file:
        file.write('{} Событие меню {}\n'
                    .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))
# записываем в лог (фиксацию) ошибки с указанием даты/времени 
def error_logger(data=''):
    with open('log_staff.txt', 'a',encoding="utf8") as file:
        file.write('{} Зафиксирована ошибка {}\n' #по хорошему как-то обозначить, какая
                    .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))
# записываем в лог выдачу результата запроса
def res_logger(data=''):
    with open('log_staff.txt', 'a',encoding="utf8") as file:
        file.write('{} Получен результат запроса {}\n'
                    .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))