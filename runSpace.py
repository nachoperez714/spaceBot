import Space
import time
import os

while True:
	seguir = True
	while seguir:
		seguir = Space.main(!os.path.exists("sigo"))
		open("sigo","w+")
		time.sleep(60*30)

	os.remove("sigo")