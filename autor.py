#!/bin/python3

c=1
k=3
print("Autorization")
#Цикл проверки логина и пароля
while c<=3:
	login=input("Login ")
	password=(input("Password "))
#Открытие файла с логинами для проверки
	log = open("filelogins.txt" , "r")
	a = log.read()
	log.close()
#Открытие файла с паролями для проверки
	passw = open("filepasswords.txt", "r")
	b = passw.read()
	passw.close()
#Непосредственно сама проверка и вывод сопутсвующих сообщений
	if login in a and password in b:
		print("Access sucsessfuly")
		break
	else:
		print("Invalid login or password")
		print("")
		c+=1
		k-=1
		if c>3:
			print("Exceeded the number of input attempts")
		else:
			print("Try again")

