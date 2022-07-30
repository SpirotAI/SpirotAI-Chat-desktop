from pypresence import Presence
import time

def startrpc():
	start = int(time.time())
	client_id = "974377110837792768"
	desc = "Spirot AI"
	detl = "Dev by Snipeur060 / 💻снайпер060⌨#1913"
	laimg = "sptest"
	latext = "Spirot AI is here"
	smimg = "talk"
	smtext = "Talk with you"
	try:
		rpc = Presence(client_id,pipe=1)
		rpc.connect()
		rpc.update(
			state=desc,
			details=detl,
			large_image=laimg,
			large_text = latext,
			small_image = smimg,
			small_text = smtext,
			start=start,
			buttons = [{"label":"Discord Spirot", "url":"https://discord.gg/sVPE5guPN5"}]
		)
	except:
		pass
	
	try:
		
		rpd = Presence(client_id,pipe=0)
		rpd.connect()
		rpd.update(
			state=desc,
			details=detl,
			large_image=laimg,
			large_text = latext,
			small_image = smimg,
			small_text = smtext,
			start=start,
			buttons = [{"label":"Discord Spirot", "url":"https://discord.gg/sVPE5guPN5"}]
		)
	except:
		pass

