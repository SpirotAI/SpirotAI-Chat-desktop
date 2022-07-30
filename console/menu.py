from console.consoleinit import *
from colorama import Fore, Back, Style
from rich.progress import track
from rich import print as prrint
from rich.prompt import Prompt
from tools.tree import allfile
from rich.console import Console
from rich.table import Table
import os
from engine.feedback import startfeed
console = Console()

def menu():
	v = findos()
	clearScreen(v)
	def scrape_data():
		sleep(0.01)
	
	for _ in track(range(100), description='[blue]Start all'):
		scrape_data()
	showmenu()

		
def launchprog(response):
	if response == 1:
		print("1")
	elif response == 2:
		startfeed()
		showmenu()
	elif response == 3:
		allfile()
		showmenu()
	elif response == 4:
		clearScreen(findos())
		showmenu()
	elif response == 5:
		prrint('[magenta] À bientôt Spirot AI')
		print("Press Enter to exit ...")
		input()
		os._exit(0)
	
	else:
		prrint('[red]Error programme inconnu')
		showmenu()
	
	
def showmenu():
	#prrint("[blue]=== MENU ===[/blue]\n [yellow]1:Talk with the bot[/yellow]\n [green]2:Feedback[/green]\n [magenta]3:Tree[/magenta]\n [red]4:Clear console\n 5:Stop[/red]")
	table = Table(show_header=True, header_style="bold blue")
	table.add_column("Date", style="dim", width=12)
	table.add_column("Name")
	table.add_column("Number", justify="right")
	table.add_row(
		"Jul 28, 2022", "[yellow]Talk with the bot[/yellow]", "1"
	)
	table.add_row(
		"Jul 28, 2022",
		"[green]Feedback[/green]",
		"2"
	)
	table.add_row(
		"Jul 28, 2022",
		"[magenta]Tree[/magenta]",
		"3"
	)
	table.add_row(
		"Jul 28, 2022",
		"[red]Clear console[/red]",
		"4"
	)
	table.add_row(
		"Jul 28, 2022",
		"[red]Stop[/red]",
		"5"
	)

	console.print(table)
	statue = "ok"
	while statue != "stop":
		try:
			#response = int(input('Numéro du programme à lancer --> '))
			response = int(Prompt.ask("[yellow] Numéro du programme à lancer"))
			launchprog(response)
			statue = "stop"
		except:
			prrint("[red]Veuillez renseigner un nombre")





