#!/usr/bin/python
#
# Diretory Find
# Coded By Twi John


import httplib
import sys, string, itertools,re
 	


banner = """

 _____  _               _                     ______ _           _ 
|  __ \(_)             | |                   |  ____(_)         | |
| |  | |_ _ __ ___  ___| |_ ___  _ __ _   _  | |__   _ _ __   __| |
| |  | | | '__/ _ \/ __| __/ _ \| '__| | | | |  __| | | '_ \ / _` |
| |__| | | | |  __/ (__| || (_) | |  | |_| | | |    | | | | | (_| |
|_____/|_|_|  \___|\___|\__\___/|_|   \__, | |_|    |_|_| |_|\__,_|
                                       __/ |                       
        Coded By Twi John             |___/                         

   
                               
"""

print banner

if len(sys.argv) !=5:
	print("Usage: "+ sys.argv[0] + " <host> <dir> <extension> <max caracters>\r\n")
        print("Ex: "+ sys.argv[0] + " www.exemple.com /home/ .php 7")
        
	sys.exit(1)

host = sys.argv[1]
chars = "abcdefghijklmnopqrstuvxwyz1234567890"
diretory = sys.argv[2]
exten = sys.argv[3]


x = False
erro = ""


conn = httplib.HTTPConnection(host)
while x != True:
	MAX_CHARS = int(sys.argv[4])
	for nletters in range(MAX_CHARS):
		for word in itertools.product(chars, repeat=nletters + 1):
		     try: 
     					
			print(''.join(word))
			dir1 = (''.join(word))
			diretory += dir1+exten 
			conn.request("HEAD",diretory)
                        r1 = conn.getresponse()
			erro = str(r1.status)
			if not re.search(erro ,"404"):
 				x = True	
				print("Dir :"+ str(diretory))
				f = open("dirs.txt","a+")
				f.write(host+diretory+"\n")
                                f.close()
		     except httplib.error:
			conn.close()
			
