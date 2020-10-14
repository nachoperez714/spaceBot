import Space
import time
import os
from importlib import reload

while True:
	seguir = True
	while seguir:
		reload(Space)#In case there were changes
		if not(os.path.exists("sigo.txt")):
			seguir = Space.main(0,vote=True)
			f = open("sigo.txt","w+")
			f.write("1")
			f.close()
		else:
			f = open("sigo.txt")
			turno = int(f.read())
			seguir = Space.main(turno,vote=True)
			f = open("sigo.txt","w+")
			f.write(str(turno+1))
			f.close()
		time.sleep(60*60)
	os.remove("sigo.txt")	
