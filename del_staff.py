from easygui import *

def del_sotr(staff,key):
    if key in staff:
        del staff[key]
        msgbox(f"Запись сотрудника {key} удалена")
    else:
        msgbox("Элемент не найден")
    return staff    

# удалять поле пакетно по всему словарю можно только гл.админу
def del_key(staff, key_field):
    for k, v in staff.items():
        if key_field in v:
            del v[key_field]
        else: msgbox("Элемент не найден")   
    return staff        



