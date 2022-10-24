from easygui import *
from menu import enter_item

def change_item_field(staff, field, sotr=''):
    if sotr == '':
        for k, v in staff.items():
            if field in v:
                v[field] = enter_item(f'{k} - текущее значение {v[field]} \nВведите новое значение поля {field}: ')
            else:
                msgbox(f'Поле {field} не найдено')    
    else:
        if sotr in staff:
            if field in staff[sotr]:
                staff[sotr][field] = enter_item(f'{sotr} - текущее значение {staff[sotr][field]} \nВведите новое значение поля {field}: ')   
            else:
                msgbox(f'Поле {field} не найдено')          
        else:
            msgbox(f'Сотрудник {sotr} не найден')   
    return staff        
                 


#пакетно повысить оклад на определенный процент
def indexation(staff, percent):
    for k, v in staff.items():
            if "Оклад" in v:
                v["Оклад"] = round(int(v["Оклад"])*percent/100+int(v["Оклад"]))
    return staff            
                    
