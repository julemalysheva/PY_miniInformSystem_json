from easygui import msgbox
from menu import enter_item, integer_item

def add_worker(staff, sotr, fields_sotr,all_fields):
    staff[sotr] = {}
    for i in range(len(all_fields)):
        staff[sotr][all_fields[i]] = fields_sotr[i]
        
    return staff    


# # добавляем ключ - новое поле карточки
def add_field(staff, field):
    msgbox('\nВводите значения нового поля для каждого сотрудника\nили пропускайте ввод, нажимая Enter\n')
    for k, v in staff.items():
        v[field] = enter_item(f'Сотрудник {k} - введите значение поля {field}: ') 
   
    return staff     


