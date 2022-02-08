#!/bin/python3
import os
import os.path

log = input("Enter login for registration ")
a = open("filelogins.txt" , "r")
q = a.read()
a.close()
if log not in q:
	passw = input("Enter password for registration ")
	print("Registration complete")
	logins = open("filelogins.txt", "a")
	logins.write(f"{log}\n")
	logins.close()
	passwords = open("filepasswords.txt", "a")
	passwords.write(f"{passw}\n")
	passwords.close()
	os.system("./autor.py")
else:
	print("Username already exists")
	print("")
	print("Do you want registration again or log in?")
	print("              1                      2")
	b = input()
	if b=="1":
		log = input("Entr login for registration ")
		passw = input("Enter password for registration ")
		print("Registration complete")
		logins = open("filelogins.txt", "a")
		logins.write(f"{log}\n")
		logins.close()
		passwords = open("filepasswords.txt", "a")
		passwords.write(f"{passw}\n")
		passwords.close()
		os.system("./autor.py")
	else:
		os.system("./autor.py")

