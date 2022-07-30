from rich.console import Console
from time import sleep
import socket
from sys import platform
import requests
from os import system

def init():
	console = Console()
	tasks = [f"task {n}" for n in range(1,2)]

	with console.status("[bold green]Init prog...") as status:
		while tasks:
			task = tasks.pop(0)
			v = findos()
			a = url_checker("https://api.spirotai.tk/")
			sleep(1)
			if a == True:
				console.log(f"{task} complete")
				system("title " + "SpiortAI")
				exit
			elif a == False:
				console.log(f"{task} failed API is offline retry later")
				exit
			else:
				console.log(f"{task} Error please restart or contact admin")
				exit
				
        
def findos():
	if platform not in ('win32', 'cygwin'):
		return 'unix'
	else:
		return 'windows'
	
def is_website_online(host):
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        return False
    else:
        return True


def url_checker(url):
	try:
		get = requests.get(url)
		if get.status_code == 200:
			return True
		else:
			return False

	except requests.exceptions.RequestException as e:
		return "no"
		
def clearScreen(os):
    from subprocess import call
    if os == 'unix':
        command = 'clear'
    else:
        command = 'cls'
    call(command, shell=True)
