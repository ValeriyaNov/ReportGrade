# import time
complete = False
teach_passw = [["username","password", "name"],["username2","password2","name2"]]
student_passw = [["username3","password3"],["username4","password4"]]

while not complete:
    username = input("Введите логин   ")
    password = input("Введите пароль   ")
    if username[0] == 'p':
        for n in len(teach_passw): 
            if username == teach_passw[n][0][0] and password == teach_passw[0][n][0]:
                print("Пароль верный!") 
                print(f"Добро пожаловать, преподаватель {teach_passw[0][0][n]}!")
                complete = True
            else:
                break
    elif username[0] == 's':
        for n in len(student_passw): 
            if username == student_passw[n][0] and password == student_passw[0][n]:
                print("Пароль верный! Добро пожаловать, студент") 
                complete = True
            else:
                break       
    elif not complete:
        print("Введие пароль заново!")