#!/bin/python3
import os
import os.path

print("-------------------------------------------")
c=0
while c!=1:
	log = input("Enter login for registration ")
#Открытие файла для считывания уже существующих логинов
	a = open("filepasswords.txt" , "r")
	q = a.read()
	a.close()
#Если логина в файле нет - продолжается регистрация
	if log not in q:
		passw = input("Enter password for registration ")
		print("Registration complete")
		print("-------------------------------------------\n\n\n\n\n")
		passwords = open("filepasswords.txt", "a")
		passwords.write(f"{log}:{passw}\n")
		passwords.close()
		os.system("./autor.py")
		break
#В противном случае прдоставляется выбор на вход в существующий аккаунт или повторная регистрация
	else:
		print("Username already exists")
		b=""
		while b!="yes" or b!="no":
			b=input("Do you want registration again?(yes/no)")
			if b=="yes" or b=="y":
				break
			if b=="no" or b=="n":
				c=1
				print("-------------------------------------------")
				break
		
