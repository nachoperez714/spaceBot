import Space
import time
import os
from importlib import reload

while True:
	seguir = True
	while seguir:
		reload(Space)#In case there were changes
		seguir = Space.main(not(os.path.exists("sigo")))
		open("sigo","w+")
		time.sleep(60*60)

	os.remove("sigo")