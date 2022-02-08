#!/bin/python3

c=1
k=3
print("Autorization")
while c<=3:
	login=input("Login ")
	password=(input("Password "))
	log = open("filelogins.txt" , "r")
	a = log.read()
	log.close()
	passw = open("filepasswords.txt", "r")
	b = passw.read()
	passw.close()
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

