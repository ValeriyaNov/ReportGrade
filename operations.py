import os
os.chdir(os.path.dirname(__file__))
import csv


def read_grade():
    complet = False
    while not complet:
        print('Выберете предмет: 1 - химия, 2 - материаловедение, 3 - метрология, 4 - сертификация')
        item = input()
        if item == '1':
            item_lst = 'Химия'
            complet = True
        elif item == '2':
            item_lst = 'Материаловедение'
            complet = True
        elif item == '3':
            item_lst = 'Метрология' 
            complet = True
        elif item == '4':
            item_lst = 'Сертификация'
            complet = True
        if not complet:
            print('Введите заново')
    complet = False
    while not complet:
        print('Выберете вид работы: 1 - РГЗ, 2 - КР/КП, 3 - экзамен')
        type_work = int(input())
        if type_work == 1:
            type_work_lst = 'РГЗ'
            complet = True
        elif type_work == 2:
            type_work_lst = 'КЗ/КП'
            complet = True
        elif type_work == 3:
            type_work_lst = 'экзамен'
            complet = True
        if not complet:
            print('Введите заново')
    complet = False
    while not complet:
        print('Введите оценку 1 - не удовлетворительно, 2 - удовлетворительно, 3 - хорошо, 4 - отлично')
        grade = int(input())
        if grade == 1:
            grade_lst = 'не удовлетворительно'
            complet = True
        elif grade == 2:
            grade_lst = 'удовлетворительно'
            complet = True
        elif grade == 3:
            grade_lst = 'хорошо' 
            complet = True
        elif grade == 4:
            grade_lst = 'отлично' 
            complet = True
        if not complet:
            print('Введите заново')

    complet = False
    while not complet:
        print('Введите ФИО студента: ')
        name_student = input()
        path = 'password.csv'
        with open(path, "r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter = ";")
            user_passw = list(file_reader) 
        for n in range(len(user_passw)): 
            d = list(user_passw[n])
            if name_student == d[1] and d[4]=='студент':
                name_lst = d[1]
                complet = True
                
        if not complet:
            print('Некорректное ФИО')

    arr = [item_lst, name_lst, type_work_lst, grade_lst]
    
    lkey = ['Предмет', 'ФИО', 'Вид работы', 'Оценка']
    array = dict(zip(lkey, arr))

    return arr


def find_grade_teacher():
    comp = False
    while not comp:
        print("Выберете предмет: 1 - химия, 2- материаловедение, 3- метрология, 4- сертификация")
        item = input()

        if item == '1':
            word1 = 'Химия'
            comp = True
        elif item == '2':
            word1 = 'Материаловедение'
            comp = True
        elif item == '3':
            word1 = 'Метрология'
            comp = True
        elif item == '4':
            word1 = 'Сертификация'
            comp = True
        if not comp:
           print('Введите заново') 

    comp = False
    while not comp:
        print("Выберете вид работы: 1 - РГЗ, 2 - КЗ/КП, 3 - экзамен")
        type_work = input()
        if  type_work == '1':
            word2 = 'РГЗ'
            comp = True
        elif type_work == '2':
            word2 = 'КЗ/КП'
            comp = True
        elif type_work == '3':
            word2 = 'Экзамен'
            comp = True  
        if not comp:
           print('Введите заново')
    
    path = 'Grade.csv'
    with open(path, "r", encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter = "|")
        user_passw = list(file_reader) 
            
    r = False
    for n in range(len(user_passw)): 
        d = user_passw[n]
        d.append('n')
        d.append('m')
        if d[0] == word1 and  d[2] == word2:
            kkey = ['Предмет', 'ФИО', 'Вид работы', 'Оценка']
            ar = dict(zip(kkey, d)) 
            print(ar) 
            ar = 0
            r = True

    if not r:
        print('Оцеки по выбранному предмету или виду работы еще не выставлены!')
            

def find_grade_student(name):
    path = 'Grade.csv'
    data = []
    with open(path, "r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter = "|")
            user_passw = list(file_reader) 
            
            for n in range(len(user_passw)): 
                d = user_passw[n]
                d.append(' ')
                d.append(' ')
                
                if d[1] == name:
                    data.append(d)  

    comp = False
    while not comp:
        print("Выберете предмет: 1 - химия, 2- материаловедение, 3- метрология, 4- сертификация")
        item = input() 

        if item == '1':
            word1 = 'Химия'
            comp = True
        elif item == '2':
            word1 = 'Материаловедение'
            comp = True
        elif item == '3':
            word1 = 'Метрология'
            comp = True
        elif item == '4':
            word1 = 'Сертификация'
            comp = True
        if not comp:
            print('Введите заново') 
    ar = []
    ff = False
    for i in data:
        if i[0] == word1:
            ar.append(i[0])
            ar.append(i[1])
            ar.append(i[2])
            ar.append(i[3])
            
            kkey = ['Предмет', 'ФИО', 'Вид работы', 'Оценка']
            d = dict(zip(kkey, ar))
            print(d)
            ar = []
            ff = True
    if not ff:
            print('Оценки еще не выставлены ')
            

    






