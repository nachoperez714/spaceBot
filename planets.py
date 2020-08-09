import numpy as np

boardlenx = 10
boardleny = 7

class Event:
	def __init__(self,name=""):
		self.name = name
		self.text = ""
		self.good_text = ""
		self.bad_text = ""
		self.url = ""
		self.icon = ""
		self.bad_chance = 0
		self.type = ""
		self.properties = {}
		self.urls = {}

	def action(self,spaceship):
		if np.random.rand()>self.bad_chance:
			spaceship = self.good_action(spaceship)
			self.text = self.good_text
		else:
			spaceship = self.bad_action(spaceship)
			self.text = self.bad_text
		return spaceship#, self.text

	def get_type(self):
		return self.type

	def get_url(self):
		return self.url

	def set_url(self):
		self.url = self.urls[self.name]

	def get_properties(self):
		self.good_text = self.properties[self.name]["good"]
		self.bad_text = self.properties[self.name]["bad"]
		self.url = self.properties[self.name]["url"]

class Start(Event):
	def __init__(self):
		super().__init__("Start")
		self.text = ""#Texto para la primer imagen
		self.icon = "Resources/Start_icon.png"

class Planet(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.4
		self.type = "Planet"
		self.icon = "Resources/Planet_icon.png"
		self.properties = {
			"Mars":{
				"good" : 'You find water in Mars,\nyour provisions increase by 10.',
				"bad"  : "Martians rob you of 10 provisions.",
				"url"  : "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg"
				},
			"Solaris":{
				"good" : "Your ex-wife's ghost helps you find food in the abandoned base, you get 10 provisions.",
				"bad"  : "Your ex-wife's ghost manipulates you into leaving her 10 provisions.",
				"url"  : "wikimedia.poeticcinema.com"
				},
			"Tatooine":{
				"good" : "You befriend an orphan that gifts you 10 provisions because you 'look like an angel'.",
				"bad"  : "Jawas steal 10 of your provisions.",
				"url"  : ""
				},
			"Trantor":{
				"good" : "Prime minister Eto Demerzel gifts you 10 provisions for your services to the Empire.",
				"bad"  : "You wind up in Billibotton and get mugged with knives. You lose 10 provision.",
				"url"  : ""
				},
			"Pandora":{
				"good" : "You fuck a blue alien, while they're asleep you take 10 of their provisions.",
				"bad"  : "You fuck a blue alien, you give them 10 provisions for the cure to space AIDS.",
				"url"  : ""
				},
			"Magrathea":{
				"good" : "Slartibartfast gifts you 10 provisions for listening to his talk about fjords.",
				"bad"  : "10 provisions are taken from you as material for a planet made of food.",
				"url"  : ""
				},
			"Gallifrey":{
				"good" : "You pick up 10 provisions from the corpse of a Gallifreyan.",
				"bad"  : "10 of your provisions are destroyed in the crossfire between Daleks and Time Lords.",
				"url"  : ""
				},
			"Roboworld":{
				"good" : "You catch 10 provisions that come flying out of a Redline's competitor's vehicle.",
				"bad"  : "10 provisions get destroyed by a blast from Funky Boy.",
				"url"  : ""
				},
			"Hoth":{
				"good" : "You scavenge 10 provisions from the still warm corpse of a Tauntaun.",
				"bad"  : "You throw 10 provisions to distract the Wampa that's chasing you.",
				"url"  : ""
				},
			"Terminus":{
				"good" : "You buy 10 provisions at the market of Terminus City.",
				"bad"  : "The Enciclopedists demand that you give them 10 provisions simply because you are dumb.",
				"url"  : ""
				},
			#Reach, Cybertron, Namek, Todos los demas de Star Wars, Vulcan, el resto de los IRL
			}	
		self.get_properties()

	def good_action(self,spaceship):
		spaceship.modify_provisions(+10)
		return spaceship

	def bad_action(self,spaceship):
		spaceship.modify_provisions(-10)
		return spaceship

class Portal(Event):
	
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.2
		self.type = "Portal"
		self.icon = "Portal.png"
		self.urls = {}
		#Wormhole, portal, warp station, improbability drive
		self.set_url()
		self.good_text = "You get transported across the universe."
		self.bad_text = "You get violently transported across the universe, losing 10 hull."

	def good_action(self,spaceship):
		spaceship.move(np.random.randint(0,boardlenx),np.random.randint(0,boardleny))
		return spaceship

	def bad_action(self,spaceship):
		spaceship.move(np.random.randint(0,boardlenx),np.random.randint(0,boardleny))
		spaceship.modify_hull(-10)
		return spaceship


class Ship(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.7
		self.type = "Ship"
		self.icon = "Ship.png"
		self.properties = {}
		self.get_properties(self.name)

	def good_action(self,spaceship):
		spaceship.modify_fuel(20)
		return spaceship

	def bad_action(self,spaceship):
		spaceship.modify_hull(-10)
		return spaceship

class Asteroid(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.9
		self.type = "Asteroid"
		self.icon = "Asteroid.png"
		self.urls = {
			"Solar system asteroid belt" : "",
			"Kuiper belt" : "",
			"Asteroid belt outside Hoth" : "",
			"Asteroid belt from Asteroids" : "",
			"Stuff" : "Other stuff"
			}
		self.bad_text = "You crash into an asteroid and lose 10 hull."
		self.good_text = "You mine an asteroid and gain 10 hull."
		self.set_url

	def good_action(self,spaceship):
		spaceship.modify_fuel(20)
		return spaceship

	def bad_action(self,spaceship):
		spaceship.modify_hull(-10)
		return spaceship


class Spaceport(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.0
		self.type = "Spaceport"
		self.icon = "Spaceport.png"
		self.urls = {
			"Knowhere" : "",
			"Death Star" : "",
			"International Space Station" : "",
			"Babylon 5" : "",
			"The Citadel" : "",#la de mass effect
			"The Bunker" : "",#la de Nier
			"Death Egg" : "",
			"The Halo arrays" : "",
			"Space colony ARK" : "",
			"ISPV 7": "",
		}
		self.set_url()

	def good_action(self,spaceship):
		spaceship.modify_fuel(100)
	
class Being(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.5
		self.type = "Being"
		self.icon = "Being.png"
		self.properties = {
			"Your Mom" : {
				"good" : "Your mom is ver kind and loving. All resources maxed up.",
				"bad"  : "The weight of your mom destroys the ship.",
				"url"  : ""
				},
			"Cthulhu" : {
				"good" : "Your tininess amuses the cosmic entity. All resources maxed up.",
				"bad"  : "Why is Cthulhu in space? Who cares, he killed you.",
				"url"  : ""
				},
			"Reaper" : {
				"good" : "You get the green ending. All resources maxed up.",#Mass Effect
				"bad"  : "You get the red ending (that means you died).",
				"url"  : ""
				},
			"Marker" : {
				"good" : "You are tasked with taking monolites to planets. All resources maxed up.",#Dead Space
				"bad"  : "What do you and Nicole Brennan have in common? That's right.",
				"url"  : ""
				},
			"Galactus" : {
				"good" : "You are the new herald of Galactus. All resources maxed up.",
				"bad"  : "Galactus accidentally swallows your ship whole. Permanently.",
				"url"  : ""
				},
			"That dragon from Kill the Moon" : {
				"good" : "Moffat maxes up your resources so that you don't ever talk about this.",
				"bad"  : "Your ship gets destroyed by the moonquakes the dragon causes.",
				"url"  : ""
				}
		}
		self.get_properties()

	def good_action(self,spaceship):
		spaceship.modify_fuel(100)
		spaceship.modify_hull(100)
		spaceship.modify_provisions(100)
		return spaceship

	def bad_action(self,spaceship):
		spaceship.modify_hull(-999)
		spaceship.modify_fuel(-999)
		spaceship.modify_provisions(-999)
		return spaceship


	#yourMom

class BlackHole(Event):
	#TODO: hacer funcion aparte para get solo url
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 1
		self.type = "Portal"
		self.icon = "Portal.png"
		self.urls = {
			"Sagittarius A":"",
			"M87" : "",
			"Gargantua" : "",
		}
		self.bad_text = "To escape the gravitational pull you use 10 extra fuel"
		self.set_url()

	def bad_action(self,spaceship):
		spaceship.modify_fuel(-10)

#Planets = ["Mars","Solaris","Tatooine","Trantor","Pandora","Magrathea","Gallifrey",
#	"Roboworld","Hoth","Terminus"]
#Portals = ["Wormhole"]
#Ships = ["TIE fighter","Elon Musk Car"]
#Asteroids = ["Solar system asteroid belt","Kuiper belt","Asteroid belt outside Hoth",
#	"Asteroid belt from Asteroids"]
#Spaceports = ["Knowhere","Death Star","International Space Station","Babylon 5",
#	"The Citadel","The Bunker","Death Egg","The Halo arrays","Space colony ARK",
#	"ISPV 7"]
#Beings = ["Your Mom","Cthulhu","Reaper","Marker","Galactus","That dragon from Kill the Moon"]
#BlackHoles = ["Sagittarius A","M87","Gargantua"]
#types = [Planets,Portals,Ships,Asteroids,Spaceports,Beings,BlackHoles]