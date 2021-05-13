import Space
import time
import os
from importlib import reload
from types import ModuleType

def rreload(module):
    reload(module)
    for attribute_name in dir(module):
        attribute = getattr(module,attribute_name)
        if type(attribute) is ModuleType and attribute_name=="planets" or attribute_name=="canvas":
            rreload(attribute)

while True:
	seguir = True
	while seguir:
		rreload(Space)#In case there were changes
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
