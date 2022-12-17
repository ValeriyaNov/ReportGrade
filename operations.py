
def read_grade():
    comp = False
    
    print('Выберете предмет: 1 - химия, 2 - материаловедение, 3 - метрология, 4 - сертификация')
    item = int(input())
    while not comp:
        if item == 1 or item == 2 or item ==3 or item ==4:
            comp = True  
        else:
            print('Введите заново')

    print('Выберете вид работы: 1 - РГЗ, 2 - КР/КП, 3 - экзамен')
    type_work = int(input())
    while not comp:
        if type_work == 1 or type_work== 2 or type_work ==3:
            comp = True
        else:
            print('Введите заново')

    print('Введите оценку 1 - не удовлетворительно, 2 - удовлетворительно, 3 - хорошо, 4 - отлично')
    grade = int(input())
    while not comp:
        if grade == 1 or grade== 2 or grade == 3 or grade == 4:
            comp = True
        else:
            print('Введите заново')

    print('Выберите студента: 1 - Абаканов А.М, 2 - Власова Р.Т, 3 - Ездин Н.А., 4 - Кочкин П.П, 5 - Лашина Н.С,б - Мороз К.Т')
    name_student = int(input())
    while not comp:
        if name_student == 1 or name_student== 2 or name_student ==3 or name_student== 4 or name_student==5 or name_student==6:
            comp = True
        else:
            print('Введите заново')


    if item == 1:
        item_lst = 'Химия'
    elif item == 2:
        item_lst = 'Материаловедение'
    elif item == 3:
        item_lst = 'Метрология' 
    elif item == 4:
        item_lst = 'Сертификация' 

    if type_work == 1:
        type_work_lst = 'РГЗ'
    elif type_work == 2:
        type_work_lst = 'КЗ/КП'
    elif type_work == 3:
        type_work_lst = 'экзамен'

    if name_student == 1:
        name_lst = 'Абаканов А.М'
    elif name_student == 2:
        name_lst = 'Власова Р.Т'
    elif name_student == 3:
        name_lst = 'Ездин Н.А.' 
    elif name_student == 4:
        name_lst = 'Кочкин П.П'
    elif name_student == 5:
        name_lst = 'Лашина Н.С.' 
    elif name_student == 6:
        name_lst = 'Мороз К.Т.'

    if grade == 1:
        grade_lst = 'не удовлетворительно'
    elif grade == 2:
        grade_lst = 'удовлетворительно'
    elif grade == 3:
        grade_lst = 'хорошо' 
    elif grade == 4:
        grade_lst = 'отлично' 
    

    array = [item_lst, name_lst, type_work_lst, grade_lst]
    return array

print(read_grade()) 