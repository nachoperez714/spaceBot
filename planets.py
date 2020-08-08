class Event:
	def __init__(self,name):
		self.name = name
		self.text = ""
		self.good_text = ""
		self.bad_text = ""
		self.url = ""
		self.icon = ""
		self.bad_chance = 0
		self.type = ""
		self.properties = {}

	def action(spaceship):
		if np.random.rand()>self.bad_chance:
			spaceship = self.good_action(spaceship)
			self.text = self.good_text
		else:
			spaceship = self.bad_action(spaceship)
			self.text = self.bad_text
		return spaceship, text

	def get_type(self):
		return self.type

	def get_url(self):
		return self.url

	def get_properties(self):
		self.good_text = self.properties[self.name]["good"]
		self.bad_text = self.properties[self.name]["bad"]
		self.url = self.properties[self.name]["url"]

class Planet(Event):
	def __init__(self,name):
		super().__init__(name)
		self.bad_chance = 0.4
		self.type = "Planet"
		self.icon = "Planet.png"
		self.properties = {
			"Mars":{
				"good" : "You find water in Mars, your provisions increase by 10.",
				"bad"  : "Martians rob you of 10 provisions.",
				"url"  : "wikimedia.mars.com"#not real page
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
				"good" : "You fuck a blue alien, while they're asleep you take 10 of their provisions",
				"bad"  : "You fuck a blue alien, you give them 10 provisions for the cure to space AIDS",
				"url"  : ""
				}
			}	
		self.get_properties(self.name)

	def good_action(spaceship):
		spaceship.modify_provisions(+10)
		return spacehip

	def bad_action(spaceship):
		spaceship.modify_provisions(-10)
		return spacehip

class Portal(Event):
	
	def __init__(self,name):
		super().__init__(name)
		self.bad_chance = 0.2
		self.type = "Portal"
		self.icon = "Portal.png"
		self.properties = {}
		self.get_properties(self.name)

	def good_action(spaceship):
		spaceship.move(np.random.randint(0,10),np.random.randint(0,8))
		return spacehip

	def bad_action(spaceship):
		spaceship.move(np.random.randint(0,10),np.random.randint(0,8))
		spaceship.modify_hull(-10)
		return spacehip


class Ship(Event):
	def __init__(self,name):
		super().__init__(name)
		self.bad_chance = 0.7
		self.type = "Ship"
		self.icon = "Ship.png"
		self.properties = {}
		self.get_properties(self.name)

	def good_action(spaceship):
		spaceship.modify_fuel(20)
		return spacehip

	def bad_action(spaceship):
		spaceship.modify_hull(-10)
		return spacehip

class Asteroid(Event):
	def __init__(self,name):
		super().__init__(name)
		self.bad_chance = 0.9
		self.type = "Asteroid"
		self.icon = "Asteroid.png"
		self.properties = {}
		self.bad_text = "You crash into an asteroid and lose 10 hull."
		self.good_text = "You mine an asteroid and gain 10 hull."

	def good_action(spaceship):
		spaceship.modify_fuel(20)
		return spacehip

	def bad_action(spaceship):
		spaceship.modify_hull(-10)
		return spacehip


class Spaceport(Event):
	def __init__(self,name):
		super().__init__(name)
		self.bad_chance = 0.0
		self.type = "Spaceport"
		self.icon = "Spaceport.png"
		self.properties = {}
		self.get_properties(self.name)

	def good_action(spaceship):
		spaceship.modify_fuel(100)


class Being(Event):
	def __init__(self,name):
		super().__init__(name)
		self.bad_chance = 0.5
		self.type = "Being"
		self.icon = "Being.png"
		self.properties = {}
		self.get_properties(self.name)

	def good_action(spaceship):
		spaceship.modify_fuel(100)
		spaceship.modify_hull(100)
		spaceship.modify_provisions(100)
		return spacehip

	def bad_action(spaceship):
		spaceship.modify_hull(-999)
		spaceship.modify_fuel(-999)
		spaceship.modify_provisions(-999)
		return spacehip


	#yourMom

class BlackHole(Event):
	#TODO: hacer funcion aparte para get solo url
	def __init__(self,name):
		super().__init__(name)
		self.bad_chance = 1
		self.type = "Portal"
		self.icon = "Portal.png"
		self.properties = {}
		self.bad_text = "To escape the gravitational pull you use 10 extra fuel"

	def bad_action(spaceship):
		spaceship.modify_fuel(-10)

Planets = ["Mars"]
Portals = ["Wormhole"]
Ships = ["TIE fighter","Elon Musk Car"]
Asteroids = ["The asteroid belt outside Hoth"]
Spaceports = ["Knowhere"]
Being = ["That dragon from Kill the Moon"]
BlackHoles = ["Sagittarius A"]
types = [Planets,Portals,Ships,Asteroids,Spaceports,Beings,BlackHoles]