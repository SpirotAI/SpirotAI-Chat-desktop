from configparser import ConfigParser
from rich import print as prrint
import sys
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def checker():
	config = ConfigParser()
	config.readfp(open(r'core.conf'))
	path1 = config.get('CONFIG', 'token')
	path2 = config.get('CONFIG', 'username')
	if path1 == "VOTRE_TOKEN_ICI" or path2 == "username" :
		prrint("[red]Veuillez remplacer les valeurs indiqué dans core.conf[/red]")
		sys.exc_info()[0]
		print("Press Enter to exit ...")
		input()
		os._exit(0)
		
def getvalueconf(configfile,title,variable):
	configv = ConfigParser()
	configv.readfp(open(fr'{configfile}'))
	pathd1 = configv.get(f'{title}', f'{variable}')
	return pathd1


