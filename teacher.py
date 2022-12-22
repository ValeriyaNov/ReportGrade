import csv
import os
os.chdir(os.path.dirname(__file__))

import operations

def menu_teach():  
    #complete = False
    print('Выберете действия: 1 - поставить оценку; 2 - посмотреть оценки')
    choic = input()
    if choic == '1':
        score = operations.read_grade()
        complet = False
        while not complet:
            print('Если хотите записать данные, то нажмите 1, если не, то -2')
            answer = int(input())
        
            if answer == 1:
                with open('Grade.csv', 'a', encoding='UTF-8') as f:
                    f_writ = csv.writer(f, delimiter = "|", lineterminator="\n" )
                    #f_writ.writerow(' ')
                    f_writ.writerow(score)
                    f_writ.writerow(' ')
                    
                complet = True   
            elif answer == 2:
                complet = True
            else:
                print('Некорректный ввод, попробуйте заново!')
            
    elif choic == '2':
        operations.find_grade_teacher()
    else:
        print('Некорректный ввод')
    

        
    



# import os
# print (os.listdir(os.getcwd()))

