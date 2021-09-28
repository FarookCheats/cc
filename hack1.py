import requests,json,time,threading,os,sys
import urllib.request, os, threading, time, random, sys
import colorama
from colorama import Fore, Style, init
#from requests_futures.sessions import FuturesSession
#from requests_futures import sessions
print (Fore.RED + "บิ้วก่อนนะครับ(ไม่บิ้วไม่ติด)")
print (Fore.GREEN + "[1] OK")
print ("[2] NO")

verfly = input("Numbers :")
if verfly == '1':
	os.system("python main.py")
	
if verfly == '2':
	 os.system("clear")
