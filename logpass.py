#!/bin/python3
def function():
	c=1
	log = "reXt"
	passw="123456"
	k=3
	print("Autorization")
	while c<=3:
		login=input("Login ")
		password=(input("Password "))
		if log==login and passw==password:
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
function()