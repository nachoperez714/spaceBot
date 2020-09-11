import Space
import time
import os
from importlib import reload

while True:
	seguir = True
	while seguir:
		if not(os.path.exists("sigo.txt")):
			print("turno 0")
			reload(Space)#In case there were changes
			seguir = Space.main("0")
			f = open("sigo.txt","w+")
			f.write(seguir)
		else:
			f = open("sigo.txt","w+")
			turno = f.read()
			print(turno)
			if turno == "1":
				print("turno 1")
				reload(Space)#In case there were changes
				seguir = Space.main(seguir)
				f.write(seguir)
			else:
				reload(Space)#In case there were changes
				seguir = Space.main("2")
		if seguir == "0":
			os.remove("sigo.txt")
		time.sleep(60*60)

	