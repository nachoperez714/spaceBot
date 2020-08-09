boardlenx = 10
boardleny = 7

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
		self.urls = {}

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

	def set_url(self):
		self.url = self.urls[self.name]

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
			"Naboo":{
				"good" : "You land in Naboo and befriend the locals. They gift you 10 provisions",
				"bad"  : "You fall in love with the princess but cant have sex with her. In impotence you lose 10 provisions",
				"url"  : ""
				},
			"Thanos farm":{
				"good" : "Thanos farm. You get you 10 provisions",
				"bad"  : "Thanos farm. You lose 10 provisions",
				"url"  : ""
				},
			"Krypton":{
				"good" : "Marlon Brando teaches you good morals. You get you 10 provisions",
				"bad"  : "Just as you are arriving you see a baby fly by and the planet explodes. You lose 10 provisions",
				"url"  : ""
				},
			"Arrakis":{
				"good" : "You become a Messiah-like figure and lead the sand people on a Jihad. You get 10 Spice",
				"bad"  : "JYou barely escape the jaws of a sandworm. You lose 10 provisions",
				"url"  : ""
				},
			"Fezzan":{
				"good" : "You entered mutually benefitial business agreements. You got 10 provisions.",
				"bad"  : "You violated the NAP, Fezzan funds terrorists against you. You lose 10 provisions",
				"url"  : "https://gineipaedia.com/w/images/thumb/d/db/Phezzan.jpg/300px-Phezzan.jpg"
				},
			"Mars Colony":{
				"good" : "You restore Mars' atmosphere and make up with a hot chick. You get 10 provisions",
				"bad"  : "You may or may not be a secret double/triple agent whose memory was wiped intentionally or unintentionally once or twice. In the confusion you lose 10 provisions",
				"url"  : "https://cms-assets.theasc.com/Total-Recall-Walk-copy.jpg?mtime=20200303055022"
				},
			"Namek":{
				"good" : "You achieve SUPERSAYIAN. You get 10 provisions",
				"bad"  : "You arrive just as a midget and a monkey destroy the planet. You lose 10 provisions",
				"url"  : "https://cms-assets.theasc.com/Total-Recall-Walk-copy.jpg?mtime=20200303055022"
				},
			"Omicron persei 8":{
				"good" : "You get some delicious Popplers. You get 10 provisions",
				"bad"  : "Lrrr tries to eat you. You lose 10 provisions",
				"url"  : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTIXHPKAZNvcU1dlbTCE9j_6yJ6wGRO26adWQ&usqp=CAU"
				},
			"Neutral Planet":{
				"good" : "Nothing good nor bad happens. You get 10 provisions",
				"bad"  : "Nothing good nor bad happens. You lose 10 provisions",
				"url"  : "https://i.ytimg.com/vi/ussCHoQttyQ/hqdefault.jpg"
				},
			"Planet of the Apes":{
				"good" : "You have successfully returned to Monke. You get 10 provisions",
				"bad"  : "You watch some statue and cry a bit. You lose 10 provisions",
				"url"  : "https://i.pinimg.com/600x315/ce/97/89/ce97891afdba546053e466ce784ea8e6.jpg"
				},
			"Forbidden Planet":{
				"good" : "You steal a hot naive girl from her father. She cooks you a sandwich. You get 10 provisions",
				"bad"  : "You are not a fan of psychoanalisis and misogyny. You lose 10 provisions",
				"url"  : "data:image/jpeg;base64,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"
				},
			#Reach, Cybertron, Todos los demas de Star Wars, Vulcan, el resto de los IRL
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
		self.urls = {}
		#Wormhole, portal, warp station, improbability drive
		self.set_url()
		self.good_text = "You get transported across the universe."
		self.bad_text = "You get violently transported across the universe, losing 10 hull."

	def good_action(spaceship):
		spaceship.move(np.random.randint(0,boardlenx),np.random.randint(0,boardleny))
		return spacehip

	def bad_action(spaceship):
		spaceship.move(np.random.randint(0,boardlenx),np.random.randint(0,boardleny))
		spaceship.modify_hull(-10)
		return spacehip


class Ship(Event):
	def __init__(self,name):
		super().__init__(name)
		self.bad_chance = 0.7
		self.type = "Ship"
		self.icon = "Ship.png"
				self.properties = {
			"Millenium Falcon":{
				"good" : "You entered a dogfight with the Millenium Falcon. You managed to steal 20 fuel from Disney",
				"bad"  : "You entered a dogfight with the Millenium Falcon. You received damage by 10 hull",
				"url"  : "https://toppng.com/uploads/preview/star-wars-millennium-falcon-11562863034ii1e8arwof.png"
				},
			"Swordfish":{
				"good" : "You encounter bounty hunters. They gift you 20 fuel",
				"bad"  : "You entered a dogfight with the The bebop. You received damage by 10 hull",
				"url"  : "https://i.pinimg.com/originals/df/06/f0/df06f0e92ff45d482ceba427a5c5a2cf.gif"
				},
			"Arwing":{
				"good" : "You destroyed Slippy. You got 20 fuel",
				"bad"  : "You entered a dogfight with Starfox. You tried and failed to do a barrel roll receiving damage by 10 hull",
				"url"  : "https://www.starfox-online.net/uploads/monthly_2015_10/large.screenshot14.jpg.d219ba347c99d595aacf4546134f7a67.jpg"
				},
			"Aloha Oe":{
				"good" : "You seduced Dandy and got 20 fuel out of him",
				"bad"  : "Dandy caused some apocalyptic shit in yout vicinity. You received damage by 10 hull",
				"url"  : "https://external-preview.redd.it/jhJR_-Cq-MdDWR4DyVFr2XyX9rupVUz8tfrGaM4zh0g.png?auto=webp&s=a8d685052176f5ae50ddfd29c88566c4765e888f"
				},
			"TIE fighter":{
				"good" : "You won a dogfight with a TIE fighter. You got 20 fuel",
				"bad"  : "You entered a dogfight with a TIE fighter. Spinning wasnt that good a trick. You received damage by 10 hull",
				"url"  : "https://images1.sw-cdn.net/product/picture/710x528_30152724_16118795_1577610881.jpg"
				},
			"Elon Musk Car":{
				"good" : "You encounter Elon Musk's Car. It encourages you to invest in Bitcoin. You got 20 fuel",
				"bad"  : "You crash into Elon Musk's Car. You received damage by 10 hull",
				"url"  : "https://i.insider.com/5a8a1f91d030721b008b47bd?width=1100&format=jpeg&auto=webp"
				},
			"Diamond Ship":{
				"good" : "Diamonds try to enlave you but you hug it out and forget your differences. You got 20 fuel",
				"bad"  : "Diamonds colonize your ship. You received damage by 10 hull",
				"url"  : "https://i.pinimg.com/originals/31/5e/cb/315ecb9ea5542fdcbe55361120a19672.jpg"
				},
			"Tardis":{
				"good" : "The Doctor gives some speech and leaves a british girl behind. She comes with 20 fuel",
				"bad"  : "The TARDIS appears inside your ship and it reminds you of your Tumblr phase. You received damage by 10 hull",
				"url"  : "https://www.popsci.com/resizer/hCYeBX0O6EtI85AKCdafilEcvrM=/760x428/arc-anglerfish-arc2-prod-bonnier.s3.amazonaws.com/public/YILFTO56CQWE7ODNC4DTVVDYLU.jpg"
				},
			"Heart of Gold":{
				"good" : "The infinite improbability drive somehow sneaks 20 fuel into your ship",
				"bad"  : "A potted plant materializes and hits your ship. You received damage by 10 hull",
				"url"  : "https://i.ytimg.com/vi/We2-lXpdG3o/maxresdefault.jpg"
				},
			"Iserlohn Fortress":{
				"good" : "You discuss the benefits of democracy. You got 20 fuel",
				"bad"  : "You barely escape it's cannon. You received damage by 10 hull",
				"url"  : "https://cdn-us.anidb.net/images/main/230347.jpg"
				},
			"Normandy":{
				"good" : "You seduce Shepard with your blue ass. You got 20 fuel out of him",
				"bad"  : "Shepard tries to enlist you for a suicide mission. You refuse and a dogfight ensues. You received damage by 10 hull",
				"url"  : "https://i.pinimg.com/originals/6f/58/cc/6f58ccda0c5049917349005a63912ae8.jpg"
				},
			"The Enterprise":{
				"good" : "You seduce Kirk with your blue ass. You got 20 fuel out of him",
				"bad"  : "You entered a dogfight with The Enterprise. You received damage by 10 hull",
				"url"  : "https://intl.startrek.com/sites/default/files/images/2019-09/startrekenterprise15322smithsonianh.jpg"
				},
			"Talos 1":{
				"good" : "You get sick powers from the Typhons. You got 20 fuel",
				"bad"  : "Black gooey things damage your hull by 10",
				"url"  : "https://vignette.wikia.nocookie.net/prey/images/6/60/Ptall1.jpg/revision/latest/scale-to-width-down/340?cb=20161024072748"
				},
			"The USCSS Prometheus":{
				"good" : "You board a ship only to discover an Alien. After defeating it you get a newfound love for motherhood. You got 20 fuel",
				"bad"  : "You board a ship only to discover an Alien. You manage to espace but only after an alien popping out of your cook and discovering your best friend is a robot made of milk. Your hull is damaged by 10",
				"url"  : "https://i.pinimg.com/originals/8a/95/1e/8a951e67505f5d041628181a09cf3a53.jpg"
				},
			"The Park":{
				"good" : "You get a hat that says 'IM EGGSCELENT'. You got 20 fuel",
				"bad"  : "Someone makes a joke about their mom. You dont get it. Your hull is damaged by 10",
				"url"  : ""
				},
			"Gunbuster":{
				"good" : "You get sent 12000 years into the future but there's someone waiting for you with 20 fuel",
				"bad"  : "You get sent 12000 years into the future. Your hull is damaged by 10",
				"url"  : ""
				},
			"Cathedral Terra":{
				"good" : "You discover that your unconquerable human spirit moves foward like a drill and pierces through the heavens. Spiral power materializes 20 fuel in your ship",
				"bad"  : "You are a bitch ass utilitarian and dont understand spirals. Your hull is damaged by 10",
				"url"  : ""
				},
			"Yolkian Ship":{
				"good" : "You defeat the eggs trying to kidnap your parents. You get 20 fuel",
				"bad"  : "Eggs kidnap your parents. Your hull is damaged by 10",
				"url"  : ""
				},
			"Event Horizon":{
				"good" : "You spend some quality time with Sam Neil before being sent to hell. You get 20 fuel",
				"bad"  : "Oops, you are in hell. Your hull is damaged by 10",
				"url"  : ""
				},
			"Kang and Kodos' Ship":{
				"good" : "They feed you and teach you how to cook for forty humans. You get 20 fuel",
				"bad"  : "You voted for Kodos. He still impregnates your wife. Your hull is damaged by 10",
				"url"  : ""
				},
			}			
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
		self.urls = {
			"Solar system asteroid belt" : "",
			"Kuiper belt" : "",
			"Asteroid belt outside Hoth" : "",
			"Asteroid belt from Asteroids" : "",
			"Halley's Comet" : "",
			"Stuff" : "Other stuff"
			}
		self.bad_text = "You crash into an asteroid and lose 10 hull."
		self.good_text = "You mine an asteroid and gain 10 hull."
		self.set_url

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
			"Space Tree Station": "",
		}
		self.set_url()

	def good_action(spaceship):
		spaceship.modify_fuel(100)
	
class Being(Event):
	def __init__(self,name):
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
		self.urls = {
			"Sagittarius A":"",
			"M87" : "",
			"Gargantua" : "",
		}
		self.bad_text = "To escape the gravitational pull you use 10 extra fuel"
		self.set_url()

	def bad_action(spaceship):
		spaceship.modify_fuel(-10)

Planets = ["Mars","Solaris","Tatooine","Trantor","Pandora","Magrathea","Gallifrey",
	"Roboworld","Hoth","Terminus"]
Portals = ["Wormhole"]
Ships = ["TIE fighter","Elon Musk Car"]
Asteroids = ["Solar system asteroid belt","Kuiper belt","Asteroid belt outside Hoth",
	"Asteroid belt from Asteroids"]
Spaceports = ["Knowhere","Death Star","International Space Station","Babylon 5",
	"The Citadel","The Bunker","Death Egg","The Halo arrays","Space colony ARK",
	"ISPV 7"]
Beings = ["Your Mom","Cthulhu","Reaper","Marker","Galactus","That dragon from Kill the Moon"]
BlackHoles = ["Sagittarius A","M87","Gargantua"]
types = [Planets,Portals,Ships,Asteroids,Spaceports,Beings,BlackHoles]