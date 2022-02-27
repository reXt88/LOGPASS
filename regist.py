#!/bin/python3

import os
import os.path

print("-------------------------------------------")
c=0
while c!=1:
    log = input("Enter login for registration ")
    #Открытие файла для проверки уже существующих логинов
    a = open("filepasswords.txt", "r")
    a.close()
    #Если лоигна нет в файле - продолжается регистраия
    if log not in q:
        passw = input("Enter password for registration ")
        print("Registration complete")
        print("-------------------------------------------")
        passwords = open("filepasswords", "a")
        passwords.write(f"{log}:{passw}\n")
        passwords.close()
        os.system("./autor.py")
        break
    else:
        print ("Username already exists")
        b=""
        while b!="yes" or b!="no":
            b = input("Do you want to registration again?(yes/no)")
            if b=="yes" or b=="y":
                break
            if b=="no" or b=="n":
                c=1
                print("-------------------------------------------")
                break
