#!/usr/bin/python
# coding: utf-8
from sys import argv, exit

if len(argv) != 2:
	print "Incorreto! Use: %s zine.txt" % argv[0]
	exit(0)

arqabri = argv[1]

f = open(arqabri, "r")
txt = f.read()
txt = txt.split("#--> Começo")
txt.pop(0)
for i in txt:
	code = i.split("#--> Fim <---#")
	nome = code[0].split("<--#")
	c = nome[1]
	nome = nome[0].strip()
	code = c.strip()
	fsave = open(nome, "a+")
	fsave.write(code)
	fsave.close()
	
f.close()
	
