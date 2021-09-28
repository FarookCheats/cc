import requests,json,time,threading,os,sys
import urllib.request, os, threading, time, random, sys
import colorama
print ("บิ้วก่อน..")
time.sleep(3)
os.system("clear")
print ("[1] Build")

verfly = input("Numbers : ")
if verfly == '1':
	os.system("pip install requests")
	os.system("pip install colorama")
	
print ("Build เสร็จแล้ว")
time.sleep(2)
print ("[66] ต่อไป")
print ("[99] ยกเลิก")

verfly = input("Numbers : ")
if verfly == '66':
	os.system("python verfly.py")
	
if verfly =='99':
	os.system("clear")