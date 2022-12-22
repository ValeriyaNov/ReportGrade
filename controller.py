import Identifikation
import operations
import teacher


print('Электронный табель оценок')
name_status = Identifikation.identifikation()

while True:

    if name_status[1] == 'преподаватель':
        teacher.menu_teach()
    elif name_status[1] == 'студент':
        operations.find_grade_student(name_status[0])
    print('Хотите продолжить? Если нет, то нажмите 1')
    n = input()
    if n == '1':
        break
    


    

