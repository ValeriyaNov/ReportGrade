# import time
import os
os.chdir(os.path.dirname(__file__))
import csv


def identifikation(): 
    complete = False
    path = 'password.csv'
    with open(path, "r", encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter = ";")
        user_passw = list(file_reader)   

    while not complete:
        username = input("Введите логин   ")
        password = input("Введите пароль   ")
        for n in range(len(user_passw)): 
            d = list(user_passw[n])
        
            if username == d[2] and password == d[3]:
                    print("Пароль верный!") 
                    print(f"Добро пожаловать, {d[4]} {d[1]}!")
                    name = d[1]
                    status = d[4]
                    complete = True 
        
            
        if not complete:
            print("Введие пароль заново!")
        
    arrr = []
    arrr.append(name)
    arrr.append(status)
    return arrr
    
