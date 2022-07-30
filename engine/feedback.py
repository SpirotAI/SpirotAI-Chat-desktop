from rich import print as prrint
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from rich.prompt import Prompt
from rich.console import Console
import socket
from core.core import getvalueconf
console = Console()


def startfeed():
	name = Prompt.ask("[yellow] Votre username ")
	title = Prompt.ask("[yellow] Titre / courte description")
	stars = Prompt.ask("[red]Nombre d'étoile sur 5 (note mettre x si vous ne voulez pas noter)")
	comment = Prompt.ask("[magenta]Votre commentaire")
	discordid = Prompt.ask("[blue]Votre discord id pour vous contacter si besoin")
	response = Prompt.ask("[red]:warning:Votre ip sera envoyé au serveur pour préserver le spam pour annuler mettre n")
	if response != "n":
		hostname = socket.gethostname()
		ip_address = socket.gethostbyname(hostname)
		ip = str(hostname)+str(ip_address)
		tokensend = getvalueconf("../core.conf.","CONFIG","token"):
		url = 'https://api.spirotai.tk/desktop/feedback'
		post_fields = {'name': name,
		'title':title,
		'stars':stars,
		'commentary': comment,
		'discordid': response,
		'ip': ip,
		'token':tokensend}
		request = Request(url, urlencode(post_fields).encode())
		json = urlopen(request).read()
		prrint('[blue]'+str(json))
	
