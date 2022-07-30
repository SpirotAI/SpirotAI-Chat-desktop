from console.consoleinit import *
from rpc.manage import startrpc
from console.menu import *
from core.core import checker
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

if __name__ == '__main__':
	init()
	checker()
	startrpc()
	menu()
	
