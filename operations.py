import os
os.chdir(os.path.dirname(__file__))
import csv

def read_grade():
    
    while True:
        print('Выберете предмет: 1 - химия, 2 - материаловедение, 3 - метрология, 4 - сертификация')
        item = input()
    
        if item == '1' or item == '2' or item == '3' or item == '4':
            break  
        else:
            print('Введите заново')

    while True:
        print('Выберете вид работы: 1 - РГЗ, 2 - КР/КП, 3 - экзамен')
        type_work = int(input())
        if type_work == 1 or type_work == 2 or type_work == 3:
            break
        else:
            print('Введите заново')
    while True:
        print('Введите оценку 1 - не удовлетворительно, 2 - удовлетворительно, 3 - хорошо, 4 - отлично')
        grade = int(input())
        if grade == 1 or grade== 2 or grade == 3 or grade == 4:
            break
        else:
            print('Введите заново')

    while True:
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
                break
            
        print('Некорректное ФИО')

    if item == '1':
        item_lst = 'Химия'
    elif item == '2':
        item_lst = 'Материаловедение'
    elif item == '3':
        item_lst = 'Метрология' 
    elif item == '4':
        item_lst = 'Сертификация' 

    if type_work == 1:
        type_work_lst = 'РГЗ'
    elif type_work == 2:
        type_work_lst = 'КЗ/КП'
    elif type_work == 3:
        type_work_lst = 'экзамен'

    if grade == 1:
        grade_lst = 'не удовлетворительно'
    elif grade == 2:
        grade_lst = 'удовлетворительно'
    elif grade == 3:
        grade_lst = 'хорошо' 
    elif grade == 4:
        grade_lst = 'отлично' 
    

    arr = [item_lst, name_lst, type_work_lst, grade_lst]
    
    lkey = ['Предмет', 'ФИО', 'Вид работы', 'Оценка']
    array = dict(zip(lkey, arr))
    print(array)
    
    return arr



#print(read_grade())

def find_grade_teacher():
    comp = False
    while not comp:
        print("Выберете предмет: 1 - химия, 2- материаловедение, 3- метрология, 4- сертификация")
        item = input()
        
        if item == '1' or item == '2' or item == '3' or item == '4':
                comp = True  

    if item == '1':
        word1 = 'Химия'
    elif item == '2':
        word1 = 'Материаоведение'
    elif item == '3':
        word1 = 'Метрология'
    elif item == '4':
        word1 = 'Сертификация'

    comp = False
    while not comp:
        print("Выберете вид работы: 1 - РГЗ, 2 - КЗ/КП, 3 - экзамен")
        type_work = input()
        if type_work == '1' or type_work == '2' or type_work == '3' :
            comp = True  
        
    if  type_work == '1':
        word2 = 'РГЗ'
    elif type_work == '2':
        word2 = 'КЗ/КП'
    elif type_work == '3':
        word2 = 'Экзамен'
    
    #data = []
    path = 'Grade.csv'
    with open(path, "r", encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter = "|")
        user_passw = list(file_reader) 
            #print(user_passw)
        r = False
    for n in range(len(user_passw)): 
        d = user_passw[n]
                #print(h, type(h))
        if d[0] == word1 and  d[2] == word2:
            kkey = ['Предмет', 'ФИО', 'Вид работы', 'Оценка']
            ar = dict(zip(kkey, d)) 
            print(ar) 
            ar = 0
            
            #data.append(ar)
            
            r = True

    if not r:
        print('Оцеки по выбранному предмету или виду работы еще не выставлены!')
            

def find_grade_student(name):
    path = 'Grade.csv'
    data = []
    with open(path, "r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter = "|")
            user_passw = list(file_reader) 
            #print(user_passw)
            for n in range(len(user_passw)): 
                d = user_passw[n]
                # print(d, type(d))
                if d[1] == name:
                    kkey = ['Предмет', 'ФИО', 'Вид работы', 'Оценка']
                    ar = dict(zip(kkey, d))   
                    data.append(ar)
#     print(data)            
# find_grade_student('Абаканов С.И.')

    comp = False
    while not comp:
        print("Выберете предмет: 1 - химия, 2- материаловедение, 3- метрология, 4- сертификация")
        item = input()
        
        if item == '1' or item == '2' or item == '3' or item == '4':
                comp = True  

    if item == '1':
        word1 = 'Химия'
    elif item == '2':
        word1 = 'Материаловедение'
    elif item == '3':
        word1 = 'Метрология'
    elif item == '4':
        word1 = 'Сертификация'
    ff = False
    for i in data:
        if i['Предмет'] == word1:
            print(i)
            ff = True
    if not ff:
            print('Оценки еще не выставлены ')
    
                














'''
with open('Grade.csv', "r", encoding='utf-8') as f:
    file_reader = csv.DictReader(f, delimiter = "|") 
    for row in file_reader:
        data.append(row)
    print(data)
    for i in range(len(data)):
        word = 'Химия'
        if word.lower() in data['Предмет']:
            print('data[i]')
        
        else: print('Нет такой записи')

    # def is_part_in_list(str_, words):
    # for word in words:
    #     if word.lower() in str_.lower():
    #         return True
    # return False

'''
