#!/bin/python3

import os

c=1
k=3
print("-------------------------------------------")
#Цикл проверки логина и пароля
while c<=3:
    login=input("Login ")
    password=(input("Password "))
    #Открытие файла с логинами и паролями для проверки
    passw = open("filepasswords.txt", "r")
    b = passw.read()
    passw.close()
    #Непосредственно сама првоерка ит вывод сопуствующих сообщений
    if login+":"+password in b:
        print("Access sucsessfuly")
        print("-------------------------------------------")
        break
    else:
        print("Invalid login or password\n\n\n\n\n")
        c+=1
        k-=1
        if c>3:
            print("Exceeded the number of input attempts")
            s=""
            while s != "yes" or s != "no":
                s = input("Do you want to create account?(yes/no) ")
                if s == "no":
                    break
                if s == "yes":
                    print("")os.system("./regist.py")
        else:
            print("Try again")
