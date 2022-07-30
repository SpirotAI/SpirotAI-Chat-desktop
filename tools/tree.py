from rich.tree import Tree
from rich import print
def allfile():
	tree = Tree("All files Spirot AI")
	data01 = tree.add("main.py")
	data02 = tree.add("core.conf")
	
	data1 = tree.add('console')
	data1.add("[red]consoleinit.py")
	data1.add("[red]menu.py")
	
	data5 = tree.add('core')
	data5.add("[green]core.py")
	
	
	data2 = tree.add('engine')
	data2.add("[blue]tchatia.py")
	data2.add("[blue]feedback.py")
	
	data3 = tree.add('rpc ([yellow]:warning: Vérifié bien qu\'il y a seulement ce fichier-là[/yellow])')
	data3.add("[red]manage.py")
	
	data4 = tree.add('tools')
	data4.add("[green]tree.py")
	
	print(tree)
