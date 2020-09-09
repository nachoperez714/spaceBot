import Space
import time
import os
from importlib import reload

while True:
	seguir = True
	while seguir:
		if seguir==2:
			vote = 1
		else:
			vote = 0
		reload(Space)#In case there were changes
		seguir = Space.main(not(os.path.exists("sigo"))+vote)
		open("sigo","w+")
		time.sleep(60*60)

	os.remove("sigo")