import json
import logger as log
from easygui import *

def load(file):
    with open(file, "r", encoding="utf-8") as fl:
        data = json.load(fl)
        log.register_logger("База сотрудников загружена")
    return data

def save(data, file): 
    try:
        with open(file, "w", encoding="utf-8") as fl:
            fl.write(json.dumps(data, ensure_ascii=False))
            log.register_logger(f'Сохранение прошло успешно в файле {file}')
    except: 
        log.error_logger('Ошибка сохранения базы')


