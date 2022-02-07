#!/bin/python3
def function():
	c=1
	log = "reXt"
	passw="123456"
	k=3
	while c<=3:
		login=input("Login ")
		password=(input("Password "))
		if log==login and passw==password:
			print("Access sucsessfuly")
			break
		else:
			print("Invalid login or password")
		c+=1
		k-=1
		if c>3:
		        print('''Exceeded the number of input attempts
Try again later''')
		else:
			print(f"{k} attempts left")


function()
