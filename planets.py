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
		self.pretext = ""
		self.path = ""

	def action(self,spaceship):
		if np.random.rand()>self.bad_chance:
			spaceship = self.good_action(spaceship)
			self.text = self.good_text
		else:
			spaceship = self.bad_action(spaceship)
			self.text = self.bad_text
		return spaceship, self.pretext+". "+self.text

	def get_type(self):
		return self.type

	def get_path(self):
		return self.path

	def set_path(self):
		self.path += self.urls[self.name]+".png"

	def get_properties(self):
		self.good_text = self.properties[self.name]["good"]
		self.bad_text = self.properties[self.name]["bad"]
		self.path += self.properties[self.name]["url"]+".png"

class Start(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.icon = "Resources/Start_icon.png"
		self.type = "Start"
		self.bad_chance = 0
		self.good_text = "You're back where you started you silly space-goose"
		self.urls = {
			"Start" : "start"
		}
		self.path = "Pictures/Start/"
		if name:
			self.set_path()

	def good_action(self,spaceship):
		return spaceship

class Goal(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.icon = "Resources/Goal_icon.png"
		self.type = "Goal"
		self.bad_chance = 0
		self.good_text = "You've reached your destination: {}.".format(self.name)
		self.path = "Pictures/Goals/"
		self.urls = {
			"Earth" : "earth",
			"Treasure Planet" : "trasure_planet",
			"The Restaurant at the end of the Universe" : "the_restaurant_at_the_end_of_the_universe",
			"Continuum Transfunctioner" : "continuum_transfunctioner",
			"Earth 2" : "earth_2",
			"Iscandar" : "iscandar",
			"Spice" : "spice",
			"Atomsk" : "atomsk",
			"The secret to life the universe and everything" : "the_secret_to_life_the_universe_and_everything",
			"Planet Ohio" : "planet_ohio",
			"The edge of the universe" : "the_edge_of_the_universe",
			"Boobies Brestaurant" : "boobies_restaurant",
			"Venom" : "venom",
			"What its based on" : "what_its_based_on",
			"A plant" : "a_plant",
			"SPB5000" : "spb5000"
		}
		if name:
			self.set_path()

	def good_action(self,spaceship):
		spaceship.isHome = True
		return spaceship

class Planet(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.4
		self.drop_rate=1
		self.type = "Planet"
		self.icon = "Resources/Planet_icon.png"
		self.pretext = "You've reached planet {}".format(self.name)
		self.path = "Pictures/Planets/"
		self.properties = {
			"Mars":{
				"good" : 'You find water in Mars, your provisions increase by 10.',
				"bad"  : "Martians rob you of 10 provisions.",
				"url"  : "mars"
				},
			"Solaris":{
				"good" : "Your ex-wife's ghost helps you find food in the abandoned base, you get 10 provisions.",
				"bad"  : "Your ex-wife's ghost manipulates you into leaving her 10 provisions.",
				"url"  : "solaris"
				},
			"Tatooine":{
				"good" : "You befriend an orphan that gifts you 10 provisions because you 'look like an angel'.",
				"bad"  : "Jawas steal 10 of your provisions.",
				"url"  : "tatooine"
				},
			"Trantor":{
				"good" : "Prime minister Eto Demerzel gifts you 10 provisions for your services to the Empire.",
				"bad"  : "You wind up in Billibotton and get mugged with knives. You lose 10 provision.",
				"url"  : "trantor"
				},
			"Pandora":{
				"good" : "You fuck a blue alien, while they're asleep you take 10 of their provisions.",
				"bad"  : "You fuck a blue alien, you give them 10 provisions for the cure to space AIDS.",
				"url"  : "pandora"
				},
			"Magrathea":{
				"good" : "Slartibartfast gifts you 10 provisions for listening to his talk about fjords.",
				"bad"  : "10 provisions are taken from you as material for a planet made of food.",
				"url"  : "magrathea"
				},
			"Gallifrey":{
				"good" : "You pick up 10 provisions from the corpse of a Gallifreyan.",
				"bad"  : "10 of your provisions are destroyed in the crossfire between Daleks and Time Lords.",
				"url"  : "gallifrey"
				},
			"Roboworld":{
				"good" : "You catch 10 provisions that come flying out of a Redline's competitor's vehicle.",
				"bad"  : "10 provisions get destroyed by a blast from Funky Boy.",
                                "url"  : "roboworld"
				},
			"Hoth":{
				"good" : "You scavenge 10 provisions from the still warm corpse of a Tauntaun.",
				"bad"  : "You throw 10 provisions to distract the Wampa that's chasing you.",
				"url"  : "hoth"
				},
			"Terminus":{
				"good" : "You buy 10 provisions at the market of Terminus City.",
				"bad"  : "The Enciclopedists demand that you give them 10 provisions simply because you are dumb.",
				"url"  : "terminus"
				},
			"Naboo":{
				"good" : "You land in Naboo and befriend the locals. They gift you 10 provisions",
				"bad"  : "You fall in love with the princess but cant have sex with her. In impotence you lose 10 provisions",
				"url"  : "naboo"
				},
			"Thanos farm":{
				"good" : "Thanos farm. You get 10 provisions",
				"bad"  : "Thanos farm. You lose 10 provisions",
				"url"  : "thanos_farm"
				},
			"Krypton":{
				"good" : "Marlon Brando teaches you good morals. You get 10 provisions",
				"bad"  : "Just as you are arriving you see a baby fly by and the planet explodes. You lose 10 provisions",
				"url"  : "krypton"
				},
			"Arrakis":{
				"good" : "You become a Messiah-like figure and lead the sand people on a Jihad. You get 10 Spice",
				"bad"  : "You barely escape the jaws of a sandworm. You lose 10 provisions",
				"url"  : "arrakis"
				},
			"Fezzan":{
				"good" : "You entered mutually benefitial business agreements. You got 10 provisions.",
				"bad"  : "You violated the NAP, Fezzan funds terrorists against you. You lose 10 provisions",
				"url"  : "fezzan"
				},
			"Orous":{
				"good" : "You inherit Earth. It comes with 10 provisions",
				"bad"  : "You spend a week doing space bureaucracy. You eat 10 provisions in the process",
				"url"  : "orous"
				},
			"Mars Colony":{
				"good" : "You restore Mars' atmosphere and make out with a hot chick. You get 10 provisions",
				"bad"  : "You may or may not be a secret double/triple agent whose memory was wiped intentionally or unintentionally once or twice. In the confusion you lose 10 provisions",
				"url"  : "mars_colony"
				},
			"Namek":{
				"good" : "You achieve SUPERSAIYAN. You get 10 provisions",
				"bad"  : "You arrive just as a midget and a monkey destroy the planet. You lose 10 provisions",
                                "url"  : "namek"
				},
			"Kaiosama's Planet":{
				"good" : "Kaiosama trains you to get stronger. You get 10 provisions",
				"bad"  : "You arrive just as Goku teleports with an exploding Cell. Pretty dick move. You lose 10 provisions",
				"url"  : "kaiosamas_planet"
				},
			"Planet Vegeta":{
				"good" : "You have somewhat returned to monke. You get 10 provisions",
				"bad"  : "You are attacked by monkeys. You lose 10 provisions",
				"url"  : "planet_vegeta"
				},
			"Broly Culo":{
				"good" : "You landed on his Culo. You get 10 provisions",
				"bad"  : "The Culo sucks you up. You lose 10 provisions",
				"url"  : "broly_culo"
				},
			"Omicron persei 8":{
				"good" : "You get some delicious Popplers. You get 10 provisions",
				"bad"  : "Lrrr tries to eat you. You lose 10 provisions",
				"url"  : "omicron_persei_8"
				},
			"Neutral Planet":{
				"good" : "Nothing good nor bad happens. You get 10 provisions",
				"bad"  : "Nothing good nor bad happens. You lose 10 provisions",
				"url"  : "neutral_planet"
				},
			"Planet of the Apes":{
				"good" : "You have successfully returned to Monke. You get 10 provisions",
				"bad"  : "You watch some statue and cry a bit. You lose 10 provisions",
				"url"  : "planet_of_the_apes"
				},
			"Forbidden Planet":{
				"good" : "You steal a hot naive girl from her father. She cooks you a sandwich. You get 10 provisions",
				"bad"  : "You are not a fan of psychoanalisis and misogyny. You lose 10 provisions",
				"url"  : "forbidden_planet"
				},
			"Cybertron":{
				"good" : "Optimus Prime gives you an inspirational speech and 10 provisions",
				"bad"  : "Starscream betrays you. You lose 10 provisions",
				"url"  : "cybertron"
				},
			"Unicron":{
				"good" : "Unicron shares with you some of Paul Masson's French champagne and you get 10 provisions",
				"bad"  : "Unicron was set up to be in the next movie but the series was rebooted. You lose 10 provsions",
				"url"  : "unicron"
				},
			"Zebes":{
				"good" : "A metroid mistakes you for his mom and gifts you 10 provisions",
				"bad"  : "You get attacked by space pirates and lose 10 provisions",
				"url"  : "zebes"
				},
			"Uranus":{
				"good" : "Hehe. You get 10 provisions",
				"bad"  : "Hehe. You lose 10 provisions",
				"url"  : "uranus"
				},
			"Galvan Prime":{
				"good" : "Momento Galvano. You get 10 provisions",
				"bad"  : "Momento Galvano. You lose 10 provisions",
				"url"  : "galvan_prime"
				},
			"Capitan del espacio":{
				"good" : "Best Alfajor of the south area. You get 10 provisions",
				"bad"  : "You dont understand what an Alfajor is. You lose 10 provisions",
				"url"  : "capitan_del_espacio"
				},
			"Pluto":{
				"good" : "This isnt a planet but you get 10 provisions",
				"bad"  : "You were sued for copyright by Disney. You lose 10 provisions",
				"url"  : "pluto"
				},
			"SCP-3003":{
				"good" : "The inhabitants gift you some weird beetles, you guess they're safe to eat. You win 10 provisions",
				"bad" : "You are weirded by everyone's lumps so you run away while dropping 10 provisions",
				"url" : "scp-3003"
				},
			"The Moon":{
				"good" : "A tear falls for the moon, a Deku scrub trades you 10 provisions for it",
				"bad" : "Oh shit, oh fuck. You lose 10 provisions",
				"url" : "the_moon"
				},
			"Macragge":{
				"good" : "The chapter master pays you for your services with 10 provisions",
				"bad"  : "Just as you arrive the Tyranid Hive Fleet Behemoth invade. You lose 10 provisions",
				"url"  : "macragge"
				},
			"Coruscant":{
				"good" : "You got some death sticks. You got 10 provisions",
				"bad"  : "You witness the collapse of democracy. You lose 10 provisions",
				"url"  : "coruscant"
				},
			"Mustafar":{
				"good" : "You have the high ground. You got 10 provisions",
				"bad"  : "You dont have the high ground. You lose 10 provisions",
				"url"  : "mustafar"
				},
			"Ego":{
				"good" : "Your Planet-Dad gives you 10 provisions",
				"bad"  : "Your Planet-Dad steals 10 provisions from you and gives your mom cancer",
				"url"  : "ego"
				},
			"Space Ghost Coast to Coast":{
				"good" : "You are a guest in the show. You get 10 provisions",
				"bad"  : "Zorak attacks you. You lose 10 provisions",
				"url"  : "space_ghost_coast_to_coast"
				},
			"Space Colony Neo-Mexico":{
				"good" : "Orale wey, you buy a Taco. You get 10 provisions",
				"bad"  : "You get shot crossing the border. You lose 10 provisions",
				"url"  : "space_colony_neo-mexico"
				},
			"Yugopotamia":{
				"good" : "Yugopotamians try to poison you with chocolate. You get 10 provisions",
				"bad"  : "Yugopotamians try to share their food with you but its shit. You lose 10 provisions",
				"url"  : "yugopotamia"
				},
			"Lifeforce Spaceship":{
				"good" : "You make out with naked space vampires. You get 10 provisions",
				"bad"  : "You get the blood suck out of your body by space vampires. You lose 10 provisions",
				"url"  : "lifeforce_spaceship"
				},
			"Brexit means Brexit":{
				"good" : "You find whats left of the british empire. You buy fish and chips. You get 10 provisions",
				"bad"  : "British 'people' try to colonize your ship. You lose 10 provisions",
				"url"  : "brexit_means_brexit"
				},
			"Skaro":{
				"good" : " Thankfully, the Daleks don't seem to notice you, and you manage to scavenge some provisions from a nearby piece of wreckage. You get 10 provisions",
				"bad"  : " Despite your best efforts, you are noticed by the Daleks, who order you to surrender or be exterminated. After begging for your life, they agree to let you go in exchange for some provisions. You lose 10 provisions",
				"url"  : "skaro"
				},
			"Dark Star (Kirby)":{
				"good" : "You get a crystal shard. You get 10 provisions",
				"bad"  : " You fight 02. You lose 10 provisions",
				"url"  : "dark_star_kirby"
				},
			"Decapod 10":{
				"good" : "You hook up with a crab waifu. You get 10 provisions",
				"bad"  : "You get operated by Zoidberg. You lose 10 provisions",
				"url"  : "decapod_10"
				},
			"Hyperion":{
				"good" : "Shrike shares some impaled bodies with you. You gain 10 provisions.",
				"bad"  : "Your daughter is cursed with reverse aging and you must sacrifice her at the Time Tombs. You lose 10 provisions.",
				"url"  : "hyperion"
				},
			"Hourglass Twins":{
				"good" : "You arrive into Chert's Camp, he offers you marshmallows and plays some music for you, you get 10 provisions",
				"bad"  : "The big sand waterfall pulls you into Ember twin, you drop 10 provisions while you escape",
				"url"  : "hourglass_twins"
				},
			"Klendathu":{
				"good" : "The humans see you're a human, you get 10 provisions",
				"bad"  : "The humans think you're an insect, you drop 10 provisions while you escape",
				"url"  : "klendathu"
				},
			"Cortex Vortex":{
				"good" : "You break some boxes and get Wumpa fruits, you get 10 provisions",
				"bad"  : "Cortex fires a laser at you, you lose 10 provisions",
				"url"  : "cortex_vortex"
				},
			"Planet 51":{
				"good" : "You raid area 51 and get 10 provisions",
				"bad"  : "You just remembered this movie exists, you lose 10 provisions",
				"url"  : "planet_51"
				},
			"Death Ball":{
				"good" : "Flippsie does a cool flip and amuses you. You get 10 provisions",
				"bad"  : "Dark laser uses his dark powers against you, you lose 10 provisions",
				"url"  : "death_ball"
				},
			"Borg Cube":{
				"good" : "You kick the space communists' asses. You get 10 provisions",
				"bad"  : "The borg try to assimilate you, you lose 10 provisions",
				"url"  : "borg_cube"
				},
			"Globetrotter Homeworld":{
				"good" : "The Harlem Globetrotters astound you with their superior intellect. You get 10 provisions",
				"bad"  : "You lose an humiliating match against the Harlem Globetrotters. You lose 10 provisions",
				"url"  : "globetrotter_homeworld"
				},
			"God of basketball":{
				"good" : "God of Basketball teaches you how to play. You get 10 provisions",
				"bad"  : "You lose an humiliating match against the God of basketball. You lose 10 provisions",
				"url"  : "god_of_basketball"
				},
			"Neptune":{
				"good" : "Robot Santa gifts you 10 provisions for being a good Zoidberg",
				"bad"  : "Robot Santa tries to kill you. You lose 10 provisions",
				"url"  : "neptune"
				},
			"Endor":{
				"good" : "Teddy bears think you are their god and gift you 10 provisions",
				"bad"  : "Teddy bears taking on a professional, technologically superior military reminds you of Nam. You lose 10 provisions",
				"url"  : "endor"
				},
			"Kashyyyk":{
				"good" : "What about the droid attack on the wookies? Chewbacca is your friend and gifts you 10 provisions",
				"bad"  : "What about the droid attack on the wookies? You barely manage to escape. You lose 10 provisions",
				"url"  : "kashyyyk"
				},
			"Vulcan":{
				"good" : "The hand gesture. You know the one. You get 10 provisions",
				"bad"  : "Just as you arrive the planet explodes. You lose 10 provisions",
				"url"  : "vulcan"
				},
			"Reach":{
				"good" : "You save Cortana. You get 10 provisions",
				"bad"  : "You hold out in a last stand of a suicide mission. You lose 10 provisions",
				"url"  : "reach"
				},
			"Sezius-RFF8 Refinery Colony ":{
				"good" : "It's abandoned... after cutting through the overgrowth you find a warehouse with 10 provisions",
				"bad" : "it's abandoned... automated defenses kick online and you drop 10 provisions",
				"url" : "sezius-rff8_refinery_colony"
				},
			"Petrichor V":{
				"good" : "You and three friends have a great time killing all the wildlife on the planet. Win 10 provisions",
				"bad" : "You and three friends have a terrible time killing only half of the wildlife on the planet. In the end you lose 10 provisions",
				"url" : "petrichor_v"
				},
			"Aiur" :{
				"good" : "Raynor's Raiders and his protoss allies will help you. You get 10 provisions",
				"bad" : "Oh oh, there are a lot of renegade zergs around the planet. You lose 10 provisions",
				"url" : "aiur"
				},
			"Peronia" : {
				"good" : "Your ship run into a Del Caño strike. They are cooking choris. You get 10 provisions",
				"bad" : "Your money has been devalued and now you can’t eat. You lose 10 provisions",
				"url" : "peronia"
				},
			"Prospero" : {
				"good" : "Amidst the ashes, you hear wolves howling in the distance. You find 10 provisions",
				"bad" : "Amidst the ashes, you hear wolves howling in the distance. You lose 10 provisions",
				"url" : "prospero"
				},
			"Moon Kingdom" : {
				"good" : "You've landed on the Moon and discover the ruins of the Moon Kingdom. A hologram of a white-haired woman shows you what it used to look like and gives you good advice. Gain 10 provisions",
				"bad" : "You've landed on the Moon and discover the ruins of the Moon Kingdom. A hologram of a white-haired woman tells you the story of what happened to this place. You drop 10 provisions while she was telling you the story",
				"url" : "moon_kingdom"
				},
			"Parum" : {
				"good" : "You land on Parum and drink some Koltova Juice at the West Café. +10 provisions",
				"bad" : "You land on Parum and get on a racial argument with a CAST. You escape dropping 10 provisions",
				"url" : "parum"
				},
			"Ersion" : {
				"good" : "The plants and fruits in the planet are edible. You get 10 provisions",
				"bad" : "Somehow this reminds you the early version of No Man's Sky. Lose 10 provisions",
				"url" : "ersion"
				},
			"Insanus" : {
				"good" : "You sold a bit of coolant to purchase 10 provisions for your ship",
				"bad" : "Your ship was attacked by violent robots. Lose 10 provisions",
				"url" : "insanus"
				},
			"Nirn" : {
				"good" : "The dwemers give you aetherium in exchange of your technology and you sell it for 10 food",
				"bad" : "You fight off a horde of cliff racers and you drop 10 provisions",
				"url" : "nirn"
				},
			"Auraxis" : {
				"good" : "You landed near an abandoned base and harvested some Cortium nearby, granting you 10 provisions",
				"bad" : "You got yourself in the middle of a never ending war between purple spandex cultists, red autoritharian crybabies and blue capitalist pigs, and your ship was hit by some rockets, losing 10 provisions",
				"url" : "auraxis"
				},
			#Todos los demas de Star Wars, el resto de los IRL
			}
		if name:
			self.get_properties()

	def good_action(self,spaceship):
		if np.random.rand()<self.drop_rate:
			if not(spaceship.item):
				#TODO get_random_item
				spaceship.item=get_random_item()
				self.text = self.text+". You found an item! You found a {}".format(spaceship.item.text)
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
		self.icon = "Resources/Portal_icon.png"
		self.pretext = "You find a {}".format(self.name)
		self.path = "Pictures/Portals/"
		self.urls = {
			"Wormhole" : "wormhole",
			"Wormhole (marvel)" : "wormhole_marvel",
			"Mass Relay" : "mass_relay",
			"Infinite improbability Drive" : "infinite_improbability_drive",
			"Warp Station" : "warp_station",
			"Portal" : "portal",
			"Bifrost" : "bifrost",
			"Florpus Hole" : "florpus_hole",
			"Portal (R&M)" : "portal_rm",
			"Time hole" : "time_hole",
			"Time vortex" : "time_vortex",
			"Stargate" : "stargate",
			"Warp Star" : "warp_star",
		}
		#Wormhole, portal, warp station, improbability drive
		if name:
			self.set_path()
		self.good_text = "You get transported across the universe."
		self.bad_text = "You get violently transported across the universe, losing 10 hull."

	def good_action(self,spaceship):
		#spaceship.move(np.random.randint(0,boardlenx),np.random.randint(0,boardleny))
		return spaceship

	def bad_action(self,spaceship):
		#spaceship.move(np.random.randint(0,boardlenx),np.random.randint(0,boardleny))
		spaceship.modify_hull(-10)
		return spaceship


class Ship(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.7
		self.type = "Ship"
		self.icon = "Resources/Ship_icon.png"
		self.pretext = "You've run into the {}".format(self.name)
		self.path = "Pictures/Ships/"
		self.properties = {
			"Millenium Falcon":{
				"good" : "You entered a dogfight with it. You managed to steal 20 fuel from Disney",
				"bad"  : "You entered a dogfight with it. You received damage by 10 hull",
				"url"  : "millenium_falcon"
				},
			"Swordfish":{
				"good" : "You encounter bounty hunters. They gift you 20 fuel",
				"bad"  : "You entered a dogfight with the swordfish. You received damage by 10 hull",
				"url"  : "swordfish"
				},
			"The Bebop":{
				"good" : "You encounter bounty hunters. They gift you 20 fuel",
				"bad"  : "You entered a dogfight with the Bebop. You received damage by 10 hull",
				"url"  : "the_bebop"
				},
			"Arwing":{
				"good" : "You destroyed Slippy. You got 20 fuel",
				"bad"  : "You entered a dogfight with Starfox. You tried and failed to do a barrel roll receiving damage by 10 hull",
				"url"  : "arwing"
				},
			"Aloha Oe":{
				"good" : "You seduced Dandy and got 20 fuel out of him",
				"bad"  : "Dandy caused some apocalyptic shit in your vicinity. You received damage by 10 hull",
				"url"  : "aloha_oe"
				},
			"TIE fighter":{
				"good" : "You won a dogfight with a TIE fighter. You got 20 fuel",
				"bad"  : "You entered a dogfight with a TIE fighter. Spinning wasnt that good a trick. You received damage by 10 hull",
				"url"  : "tie_fighter"
				},
			"Elon Musk Car":{
				"good" : "You encounter Elon Musk's Car. It encourages you to invest in Bitcoin. You got 20 fuel",
				"bad"  : "You crash into Elon Musk's Car. You received damage by 10 hull",
				"url"  : "elon_musk_car"
				},
			"Diamond Ship":{
				"good" : "Diamonds try to enlave you but you hug it out and forget your differences. You got 20 fuel",
				"bad"  : "Diamonds colonize your ship. You received damage by 10 hull",
				"url"  : "diamond_ship"
				},
			"Tardis":{
				"good" : "The Doctor gives some speech and leaves a british girl behind. She comes with 20 fuel",
				"bad"  : "The TARDIS appears inside your ship and it reminds you of your Tumblr phase. You received damage by 10 hull",
				"url"  : "tardis"
				},
			"Heart of Gold":{
				"good" : "The infinite improbability drive somehow sneaks 20 fuel into your ship",
				"bad"  : "A potted plant materializes and hits your ship. You received damage by 10 hull",
				"url"  : "heart_of_gold"
				},
			"Iserlohn Fortress":{
				"good" : "You discuss the benefits of democracy. You got 20 fuel",
				"bad"  : "You barely escape its cannon. You received damage by 10 hull",
				"url"  : "iserlohn_fortress"
				},
			"Normandy":{
				"good" : "You seduce Shepard with your blue ass. You got 20 fuel out of him",
				"bad"  : "Shepard tries to enlist you for a suicide mission. You refuse and a dogfight ensues. You received damage by 10 hull",
				"url"  : "normandy"
				},
			"The Enterprise":{
				"good" : "You seduce Kirk with your blue ass. You got 20 fuel out of him",
				"bad"  : "You entered a dogfight with The Enterprise. You received damage by 10 hull",
				"url"  : "the_enterprise"
				},
			"Talos 1":{
				"good" : "You get sick powers from the Typhons. You got 20 fuel",
				"bad"  : "Black gooey things damage your hull by 10",
				"url"  : "talos_1"
				},
			"The USCSS Prometheus":{
				"good" : "You board a ship only to discover an Alien. After defeating it you get a newfound love for motherhood. You got 20 fuel",
				"bad"  : "You board a ship only to discover an Alien. You manage to escape but only after an alien popping out of your cook and discovering your best friend is a robot made of milk. Your hull is damaged by 10",
				"url"  : "the_uscss_prometheus"
				},
			"The Park":{
				"good" : "You get a hat that says 'IM EGGSCELENT'. You got 20 fuel",
				"bad"  : "Someone makes a joke about their mom. You dont get it. Your hull is damaged by 10",
				"url"  : "the_park"
				},
			"Gunbuster":{
				"good" : "You get sent 12000 years into the future but there's someone waiting for you with 20 fuel",
				"bad"  : "You get sent 12000 years into the future. Your hull is damaged by 10",
				"url"  : "gunbuster"
				},
			"Cathedral Terra":{
				"good" : "You discover that your unconquerable human spirit moves foward like a drill and pierces through the heavens. Spiral power materializes 20 fuel in your ship",
				"bad"  : "You are a bitch ass utilitarian and dont understand spirals. Your hull is damaged by 10",
				"url"  : "cathedral_terra"
				},
			"Yolkian Ship":{
				"good" : "You defeat the eggs trying to kidnap your parents. You get 20 fuel",
				"bad"  : "Eggs kidnap your parents. Your hull is damaged by 10",
				"url"  : "yolkian_ship"
				},
			"Event Horizon":{
				"good" : "You spend some quality time with Sam Neil before being sent to hell. You get 20 fuel",
				"bad"  : "Oops, you are in hell. Your hull is damaged by 10",
				"url"  : "event_horizon"
				},
			"Kang and Kodos' Ship":{
				"good" : "They feed you and teach you how to cook for forty humans. You get 20 fuel",
				"bad"  : "You voted for Kodos. He still impregnates your wife. Your hull is damaged by 10",
				"url"  : "kang_and_kodos_ship"
				},
			"Firefly":{
				"good" : "You get renewed for a second season. You get 20 fuel",
				"bad"  : "You get cancelled on the first season. Your hull is damaged by 10",
				"url"  : "firefly"
				},
			"Space Godzilla":{
				"good" : "You defeat Space Godzilla. You get 20 fuel",
				"bad"  : "Space Godzilla attacks you. Your hull is damaged by 10",
				"url"  : "space_godzilla"
				},
			"Comet Observatory":{
				"good" : "Rosalina gifts you 20 fuel",
				"bad"  : "Rosalina performs CBT on you. Your hull is damaged by 10",
                                "url"  : "comet_observatory"
				},
			"Barrilete Cosmico":{
				"good" : "Maradona shares a line of coke with you. You get 20 fuel",
				"bad"  : "Maradona made you a terrible dribble. Your hull is damaged by 10",
				"url"  : "barrilete_cosmico"
				},
			"Capitan Beto":{
				"good" : "His ring makes you immune to danger. You get 20 fuel",
				"bad"  : "Not even a sad shadow is left. Your hull is damaged by 10",
				"url"  : "capitan_beto"
				},
			"Von Braun":{
				"good" : "You embark on the first manned mission to Jupiter. You get 20 fuel",
				"bad"  : "You are boarded by space terrorists trying to make you feel bad about space exploration. Your hull is damaged by 10",
				"url"  : "von_braun"
				},
			"Dalek Fleet":{
				"good" : "You wave a sonic screwdriver a bit and they explode. You get 20 fuel",
				"bad"  : "EXTERMINATE. You lose 10 hull",
				"url"  : "dalek_fleet"
				},
			"Vengeful Spirit":{
				"good" : "Glory to the emperor of mankind. You get 20 fuel",
				"bad"  : "Sanguinus is dead. You lose 10 hull",
				"url"  : "vengeful_spirit"
				},
			"Voyager 1":{
				"good" : "You steal 20 fuel from the probe",
				"bad" : "The probe's security measures damage your ship. You lose 10 hull",
				"url" : "voyager_1"
				},
			"Remote-controlled solid gold death star":{
				"good" : "You get a code to travel through time. You steal 20 fuel from your past self",
				"bad"  : "Nudist scammers damage your hull by 10",
				"url"  : "remote-controlled_solid_gold_death_star"
				},
			"Fortress of doom":{
				"good" : "You manage to run doom on a facebook bot. You get 20 fuel",
				"bad"  : "The Doom Slayer stares at your ship and damages it by 10 hull",
				"url"  : "fortress_of_doom"
				},
			" ARSAT":{
				"good" : "You manage to get from Cordoba to Japan in only 2 hours. You get 20 fuel",
				"bad"  : "A general strike by the CGT damages your ship by 10",
				"url"  : "arsat"
				},
			"Duck Dodgers' ship":{
				"good" : "Duck saves you from martians and gives you 20 fuel",
				"bad"  : "ACME explosives go off and you lose 10 hull",
				"url"  : "duck_dodgers_ship"
				},
			"Jumba's ship":{
				"good" : "You spend a vacation in hawaii and get 20 fuel",
				"bad"  : "One of his experiments does damage to your ship by 10 hull",
				"url"  : "jumbas_ship"
				},
			"Axiom":{
				"good" : "You get fat in an automated consumerist society and get 20 fuel",
				"bad"  : "The Ship's Autopilot detects a plant on your ship and attacks you. You lose 10 hull",
				"url"  : "axiom"
				},
			"Captain Planet":{
				"good" : "You get 20 clean energy fuel",
				"bad"  : "Indivual Enviromental responsability is a spook. You lose 10 hull",
				"url"  : "captain_planet"
				},
			"Buzz LightYear's Star Cruiser":{
				"good" : "To infinity... and beyond! You get 20 fuel",
				"bad"  : "You are a sad, strange little man. You lose 10 hull",
				"url"  : "buzz_lightyears_star_cruiser"
				},
			"Space chimps":{
				"good" : "Return to monke...IN SPACE. You get 20 fuel",
				"bad"  : "Crackhouse vibes. You lose 10 hull",
				"url"  : "space_chimps"
				},
			"Ships from Chicken Little":{
				"good" : "You bond with your chicken father. You get 20 fuel",
				"bad"  : "Sky falls on your head. You lose 10 hull",
				"url"  : "ships_from_chicken_little"
				},
			"Great Thing":{
				"good" : "You hunt the whale. You get 20 fuel",
				"bad"  : "You barely survived the whale's bullet hell. You lose 10 hull",
				"url"  : "great_thing"
				},
			"Space Battleship Yamato":{
				"good" : "They give your ship a resupply before going back on their merry way. You get 20 fuel",
				"bad"  : "They don't seem to like the cut of your jib, so they blast you with the Wave Motion Gun. You lose 10 hull",
				"url"  : "space_battleship_yamato"
				},
			"Red Dwarf":{
				"good" : "They trade you 20 fuel in exchange for some curry and lager.",
				"bad"  : "You crash into Red Dwarf. Seems the crew were distracted by the Cat's snazzy outfit. Your hull is damaged by 10 points.",
				"url"  : "red_dwarf"
				},
			"Tylor's Landeel":{
				"good" : "You exchange A-Photon reactors with Tylor for fuel. You get 20 fuel",
				"bad"  : "Tylor and his crew try to rob your ship, but you barely escape. -10 hull.",
				"url"  : "tylors_landeel"
				},
			"Imperial fleet":{
				"good" : "Dock with the main star destroyer. You get 20 fuel",
				"bad"  : "Get locked by the tractor beam. You lose 10 hull",
				"url"  : "imperial_fleet"
				},
			"Ebon Hawk":{
				"good" : "The Ebon Hawk crew decides to help you, You get 20 fuel",
				"bad"  : "You come across with the Ebon Hawk being chased by the Leviathan. You lose 10 hull",
				"url"  : "ebon_hawk"
				},
			"Jason Bright's flock":{
				"good" : "Jason Bright thanked you for dealing with the 'demons'. You received 20 fuel.",
				"bad"  : "Jason Bright noticed you attacked a ghoul and did not like it. Your hull is damaged by 10",
				"url"  : "jason_brights_flock"
				},
			"Arcadia":{
				"good" : "You steal 20 fuel from the space pirates",
				"bad"  : "The Arcadia fires at you. Your hull is damaged by 10",
				"url"  : "arcadia"
				},
			"Alien Ship (Metal Slug)":{
				"good" : "You use your HEAVY MACHINEGUN against it. It drops 20 fuel",
				"bad"  : "It fires a laser at you. Your hull is damaged by 10",
				"url"  : "alien_ship_metal_slug"
				},
			"Starman Jr":{
				"good" : "Buzz Buzz protects you and you defeat the Starman. It drops 20 fuel",
				"bad"  : "The Starman uses PSI Fire against you. Your hull is damaged by 10",
				"url"  : "starman_jr"
				},
			"Major Tom":{
				"good" : "Everybody likes David Bowie, you get 20 fuel",
				"bad"  : "There's no reply. Your hull is damaged by 10",
				"url"  : "major_tom"
				},
			"SEEDS":{
				"good" : "Lets find a new beginning for humanity, you get 20 fuel",
				"bad"  : "The ship crashes due to an immortal blondie. Your hull is damaged by 10",
				"url"  : "seeds"
				},
			"RMS Titanic":{
				"good" : "You meet a hot blonde and she gifts you 20 fuel",
				"bad"  : "The Titanic sinks. IN SPACE. Your hull is damaged by 10",
				"url"  : "rms_titanic"
				},
			"Chimerian Hammer":{
				"good" : "You get the Omnitrix, it comes with 20 fuel",
				"bad"  : "Vilgax crashes your ship because he thinks you have the Omnitrix. Your hull is damaged by 10",
				"url"  : "chimerian_hammer"
				},
			"White Base":{
				"good" : "You boarded at White Base's hangar. Captain Bright and his crews restock your ship with 20 fuel",
				"bad"  : "The White Base crews misinformed you as a zeon ship so they open fire at you. Your hull is damaged by 10",
				"url"  : "white_base"
				},
			"Spaceball One":{
				"good" : "You escape on Ludicrous speed and manage to snatch 20 fuel",
				"bad"  : "It vacuums your ship. Your hull is damaged by 10",
				"url"  : "spaceball_one"
				},
			"Gary":{
				"good" : "Gary gifts you 20 fuel",
				"bad"  : "You didnt complete your ritual youth dance. Your hull is damaged by 10",
				"url"  : "gary"
				},
			"Freighter":{
				"good" : "The freighter refills you 20 fuel",
				"bad"  : "No man's sky wasnt playable on release. Your hull is damaged by 10",
				"url"  : "freighter"
				},
			"Tiangong-1":{
				"good" : "邓小平没做错什么。你得到20加油",
				"bad"  : "4th june, 1989. Nothing happens in Tiananmen Square. Your hull is damaged by 10",
				"url"  : "tiangong-1"
				},
			"Freeza's ship":{
				"good" : "You watch Bardock be obliterated in a final stand, he drops 20 fuel",
				"bad"  : "An alien midget that isnt even in it's final form shoots you. Your hull is damaged by 10",
				"url"  : "freezas_ship"
				},
			"Don John Roland":{
				"good" : "The Don John Roland is a party ship and gives you 20 fuel",
				"bad" : "This is actually the ship's twin, the meat eating ship, the John Ron Donald, which eats 10 of hull",
				"url" : "don_john_roland"
				},
			"Space Amish":{
				"good" : "The Amish gift you 20 fuel because they're nice",
				"bad" : "Amish believe your ship is heretical and attack you with a horse, -10 hull",
				"url" : "space_amish"
				},
			"UES Contact Light":{
				"good" : "You have a delivery! You get 20 fuel",
				"bad" : "You get attacked by a very angry guy with a sword who damages your hull by 10",
				"url" : "ues_contact_light"
				},
			"USS Ishimura":{
				"good" : "You manage to board the ship and stomp some crates. You get 20 fuel",
				"bad" : "You fight hordes of necromorphs as you realize your girlfriend is dead. Lose 10 hull",
				"url" : "uss_ishimura"
				},
			"Joji's Ship":{
				"good" : "The captain sings a song. you get 20 fuel",
				"bad" : "The crewmate of the captain betrays then you get hit from the fight. you lose 10 hull",
				"url" : "jojis_ship"
				},
			"Grancypher" : {
				"good" : "You get 20 fuel for not questioning what's an airship doing in space",
				"bad" : "Rackam accidentally hits you and you lose 10 hull",
				"url" : "grancypher"
				},
			"Grox Ship" : {
				"good" : "You run into a Grox ship. You somehow convince them to not blow up your ship and get 20 fuel from them",
				"bad" : "You run into a Grox ship. They see you as a threat and damage your hull by 10",
				"url" : "grox_ship"
				},
			"Federal Security Forces" : {
				"good" : "They let you pass through the resource extraction site. You gain 20 fuel",
				"bad" : "They see smuggled items in your hold. They attempt an arrest but you supercruise out. Hull damaged by 10",
				"url" : "federal_security_forces"
				},
			"Grineer Galleon" : {
				"good" : "You sabotage the ship and gain 20 fuel",
				"bad" : "You get targeted by a Grineer Navar cannon and lose 10 hull",
				"url" : "grineer_galleon"
				},
			"Derelict Alien Spaceship" : {
				"good" : "You managed to scavenge for resources and found 20 fuel through the wreckage",
				"bad" : "Your ship's presence activated old security drones that attacked you, causing 10 damage in your hull",
				"url" : "derelict_alien_spaceship"
				},
			"Musai Class Cruiser" : {
				"good" : "The crew provides 20 fuel for your journey",
				"bad" : "The crew believe you're part of the V Project and attack, you lose 10 hull",
				"url" : "musai_class_cruiser"
				},
			"Clan Wolf Dropship" : {
				"good" : "You win a trial of possession despite not owning any 'Mechs. Gain 20 fuel",
				"bad" : "They fire their C-ER-PPC's at you, damaging your hull by 10",
				"url" : "clan_wolf_dropship"
				},
			}
		if name:
			self.get_properties()

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
		self.icon = "Resources/Asteroid_icon.png"
		self.pretext = "You find yourself in the vicinity of {}".format(self.name)
		self.path = "Pictures/Debris/"
		self.urls = {
			"Solar system asteroid belt" : "solar_system_asteroid_belt",
			"Fox's Satelite" : "foxs_satellite",
			"ARSAT" : "arsat",
			"Balloon Priest" : "balloon_priest",
			"Grob gob glob grod" : "grob_gob_glob_grod",
			"Bender" : "bender",
			"Hoshimachi Suisei" : "hoshimachi_suisei",
			"Laika" : "laika",
			"Attack ball" : "attack_ball",
			"A Baoa Qu" : "a_baoa_qu",
			"Mansion room" : "mansion_room",
			"Kuiper belt" : "kuiper_belt",
			"Asteroid belt outside Hoth" : "asteroid_belt_outside_hoth",
			"Asteroid belt from Asteroids" : "asteroid_belt_from_asteroids",
			"Halley's Comet" : "halleys_comet",
			"Space trash" : "space_trash",
			"Kars" : "kars",
			"Wheatley" : "wheatley",
			"Baseball Asteroid" : "baseball_asteroid",
			"Master Chief" : "master_chief",
			"Rocket Man" : "rocket_man",
			"Deoxys" : "deoxys",
			"Space Anomaly" : "space_anomaly",
			"Sputnik" : "sputnik",
			"Higuain's penalty" : "higuains_penalty",
			"Poochy on his way to his home planet" : "poochy_on_his_way_to_his_home_planet",
			"Garbage Ball" : "garbage_ball",
			"Phantom Zone" : "phantom_zone",
			"Asteroid from Armageddon" : "asteroid_from_armageddon",
			"Wall-e and EVE" : "wall-e_and_eve",
			"Meateroid" : "meateroid",
			"Space Hulk" : "space_hulk",
			"Space Mafalda" : "space_mafalda",
			"The Little Prince's planet" : "the_little_princes_planet",
			"Juice" : "juice",
			"Monument of B-R5RB" : "monument_of_b-r5rb",
			"Moon Bears" : "moon_bears",
			}
		self.bad_text = "You crash into an object and lose 10 hull."
		self.good_text = "You set up a mining station and gain 10 hull."
		if name:
			self.set_path()

	def good_action(self,spaceship):
		spaceship.modify_hull(10)
		return spaceship

	def bad_action(self,spaceship):
		spaceship.modify_hull(-10)
		return spaceship


class Spaceport(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.0
		self.type = "Spaceport"
		self.icon = "Resources/Spaceport_icon.png"
		self.pretext = "You dock your ship at {}".format(self.name)
		self.path = "Pictures/Spaceports/"
		self.urls = {
			"Knowhere" : "knowhere",
			"Death Star" : "death_star",
			"International Space Station" : "international_space_station",
			"Babylon 5" : "babylon_5",
			"The Citadel" : "the_citadel",
			"The Citadel (R&M)" : "the_citadel_rm",
			"The Bunker" : "the_bunker",
			"Death Egg" : "death_egg",
			"The Halo arrays" : "the_halo_arrays",
			"Space colony ARK" : "space_colony_ark",
			"ISPV 7": "ispv_7",
			"Space Tree Station": "space_tree_station",
			"Terra Venture": "terra_venture",
			"Dr Willy's Space Station": "dr_willys_space_station",
			"Space Colony Neo Mexico": "space_colony_neo_mexico",
			"Jameson Memorial": "jameson_memorial",
			"Axis": "axis",
			"Star Forge": "star_forge",
			"La Vie en Rose": "la_vie_en_rose",
			"Hydroponics Station": "hydroponics_station",
			"GUARDIANS Colony" : "guardians_colony",
			"The Beyond" : "the_beyond",
			"Salyut 6" : "salyut_6",
			"United Nations in Exile" : "united_nations_in_exile",
			"Solar Station" : "solar_station",
			"Everus Harbor" : "everus_harbor",
			"KND Moonbase" : "knd_moonbase",
			"Ghost Station" : "ghost_station",
			}
		self.good_text = "You get 50 of your lowest resource."
		if name:
			self.set_path()

	def good_action(self,spaceship):
		fuel = spaceship.fuel
		food = spaceship.provisions
		hull = spaceship.hull
		if fuel<=food and fuel<=hull:
			spaceship.modify_fuel(50)
		elif food<=hull:
			spaceship.modify_provisions(50)
		else:
			spaceship.modify_hull(50)
		return spaceship

class Being(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.5
		self.type = "Being"
		self.icon = "Resources/Being_icon.png"
		self.pretext = "You find a cosmic entity: {}".format(self.name)
		self.path = "Pictures/Beings/"
		self.properties = {
			"Your Mom" : {
				"good" : "Your mom is very kind and loving. All resources +100.",
				"bad"  : "The weight of your mom destroys the ship.",
				"url"  : "your_mom"
				},
			"Cthulhu" : {
				"good" : "Your tininess amuses the cosmic entity. All resources +100.",
				"bad"  : "Why is Cthulhu in space? Who cares, he killed you.",
				"url"  : "cthulhu"
				},
			"Reaper" : {
				"good" : "You get the green ending. All resources +100.",#Mass Effect
				"bad"  : "You get the red ending (that means you died).",
				"url"  : "reaper"
				},
			"Marker" : {
				"good" : "You are tasked with taking monolites to planets. All resources +100.",#Dead Space
				"bad"  : "What do you and Nicole Brennan have in common? That's right.",
				"url"  : "marker"
				},
			"Galactus" : {
				"good" : "You are the new herald of Galactus. All resources +100.",
				"bad"  : "Galactus accidentally swallows your ship whole. Permanently.",
				"url"  : "galactus"
				},
			"Space baby" : {
				"good" : "Benevolent Space baby wants to help you evolve. All resources +100.",
				"bad"  : "The Space baby is in stage of evolution you cant comprehend. You lose the game",
				"url"  : "space_baby"
				},
			"That dragon from Kill the Moon" : {
				"good" : "Moffat maxes up your resources so that you don't ever talk about this.",
				"bad"  : "Your ship gets destroyed by the moonquakes the dragon causes.",
				"url"  : "that_dragon_from_kill_the_moon"
				},
			"God" : {
				"good" : "God did things right, you arent sure if he did anything at all. Your resources rise by 100.",
				"bad"  : "God does nothing. You died in space",
				"url"  : "god"
				},
			"AntiSpiral" : {
				"good" : "You pierce the heavens with your spirit. Your resources rise by 100.",
				"bad"  : "Your spiral power wasnt enough. You were destroyed to stave off the spiral nemesis.",
				"url"  : "antispiral"
				},
			"Zucc" : {
				"good" : "You encounter a strange android entity calling itself The Zucc. You sacrifice an asian woman to please him. Your resources increase by 100.",
				"bad"  : "u have been zucced goodbye",
				"url"  : "zucc"
				},
			"Page Admin" : {
				"good" : "You run into the admin of this page. Because he is a kind and benevolent admin, he gives you 100 of each resource.",
				"bad"  : "You run into the admin of this page. Unfortunately, you haven't been reacting enough to their posts and so they decide to permaban you... with extreme prejudice.",
				"url"  : "page_admin"
				},
			"Monolith" : {
				"good" : "You encounter an alien monolith. As a reward for making it out here, the aliens grant you supreme knowledge to transcend your physical humanity, and even give you 100 of each resource as a bonus.",
				"bad"  : "You encounter an alien monolith. Unfortunately, the aliens take one look at your primitive ship and de-evolve the crew back into apes. Game over.",
				"url"  : "monolith"
				},
			"Flying Spaghetti Monster" : {
				"good" : "You run into the Flying Spaghetti Monster. Seeing that your crew are dedicated believers, it gives you 100 of all resources.",
				"bad"  : "You run into the Flying Spaghetti Monster. Unfortunately, nobody on your crew is a believer, and so as a divine punishment, it sends you to the infinite spaghetti dimension, where you are doomed to roam for all eternity. At least you'll never run out of food.",
				"url"  : "flying_spaghetti_monster"
				},
			"Alien X" : {
				"good" : "Alien X warps reality to get 100 of each resource.",
				"bad"  : "Alien X obliterates you.",
				"url"  : "alien_x"
				},
			"Aurelion Sol" : {
				"good" : "The Star Forger is amused with your puny ship. +100 to all resources.",
				"bad"  : "The Star Forger sees your small existence, and promptly sends a beam of light to end you. ",
				"url"  : "aurelion_sol"
				},
			"Moon Lord" : {
				"good" : "Moon Lord gifts you some luminite to build 100 of every resource.",
				"bad"  : "Your ship is struck by Moon Lord's Phantasmal Laser. You die",
				"url"  : "moon_lord"
				},
			"Silver surfer" : {
				"good" : "Silver surfer gives you 100 of every resource to help you defeat Galactus.",
				"bad"  : "Galactus was gonna kill you anyway so Silver surfer does it quicker.",
				"url"  : "silver_surfer"
				},
			"GOLB" : {
				"good" : "The entity of chaos watches you fly by and gives you 100 of every resource",
				"bad"  : "GOLB is a mysterious entity who embodies chaos. You die",
				"url"  : "golb"
				},
			"Dr. Manhattan " : {
				"good" : "You find Dr. Manhattan, he discusses the potential of human life. He maxes out your resources",
				"bad"  : "You find Dr. Manhattan, he's in the middle of a depressing monologue about the meaning of time. You die",
				"url"  : "dr_manhattan"
				},
			"The Beast with a Billion Backs" : {
				"good" : "The Beast repents for its foul actions and leaves you in peace. +100 to all stats.",
				"bad"  : "The Beast rapes you with its enormous tentacles. A moment of bliss is followed by your painful death.",
				"url"  : "the_beast_with_a_million_backs"
				},
			"02" : {
				"good" : "You win Kirby. +100 to all stats.",
				"bad"  : "You are not Kirby. It kills you.",
				"url"  : "02"
				},
			"Leviathan" : {
				"good" : "You have grown fat from strength. +100 to all stats.",
				"bad"  : "Your light fades.",
				"url"  : "leviathan"
				},	
			"Hellstar Remina" : {
				"good" : "Junji Ito is a fine fellow. +100 to all stats.",
				"bad"  : "The lovecraftian planet licks your ship. It kills you.",
				"url"  : "hellstar_remina"
				},
			"Anti-Pops" : {
				"good" : "Anti-Pops is friendly with you for some reason. +100 to all stats.",
				"bad"  : "You sacrifice yourself to stop Anti-Pops from destroying the universe.",
				"url"  : "anti-pops"
				},
			"Stock Photo Alien" : {
				"good" : "No royalties necessary. Resources +100.",
				"bad" : "Dreamtime is furious, and kills you immediately, not before your photobucket account.",
				"url" : "stock_photo_alien"
				},
			"Lavos" : {
				"good" : "Lavos is still in hibernation, you collect a lot of resources and leave.",
				"bad" : "You get there as Lavos wakes up, killing you.",
				"url" : "lavos"
				},
			"Giygas" : {
				"good" : "You pray for your friends and you defeat Giygas, +100 to all resources",
				"bad" : "You cannot grasp the true form of Giygas's attack!",
				"url" : "giygas"
				},
			"Turn A" : {
				"good" : "The Gundam didn't have enough power to use Moonlight Butterfly, instead you get +100 to everything",
				"bad" : "The Moomlight Butterfly turns your ship and all other technology to sand",
				"url" : "turn_a"
				},

			}
		if name:
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
		self.type = "Black Hole"
		self.icon = "Resources/BlackHole_icon.png"
		self.pretext = "Oh no! It's the black hole {}".format(self.name)
		self.path = "Pictures/BlackHoles/"
		self.urls = {
			"Sagittarius A*":"sagittarius_a",
			"Messier 87" : "messier_87",
			"Gargantua" : "gargantua",
			"Black Hole Sun" : "black_hole_sun",
			"Supermassive Black Hole" : "supermassive_black_hole",
			"Hugh Janus" : "hugh_janus",
			"Black Hole (Zathura)" : "black_hole_zathura",
			"Black Hole (Futurama)" : "black_hole_futurama",
			"Dark Hole" : "dark_hole",
			"Your mom's ass" : "your_moms_ass",
			"Mario Galaxy Black Hole" : "mario_galaxy_black_hole",
		}
		self.bad_text = "To escape the gravitational pull you use 10 extra fuel"
		if name:
			self.set_path()

	def bad_action(self,spaceship):
		spaceship.modify_fuel(-10)
		return spaceship

class Player:
	def __init__(self,name=""):
		self.name = name
		self.url = ""
		self.fuel = 100
		self.provisions = 100
		self.hull = 100
		self.path = "Pictures/Player/"
		self.properties = {
			"Planet Express" : {
				"url"  : "planet_express",
				"fuel" : 100,
				"provisions"  : 100,
				"hull"  : 100,
				},
			"Rick's ship" : {
				"url"  : "ricks_ship",
				"fuel" : 110,
				"provisions"  : 110,
				"hull"  : 80,
				},
			"X-Wing" : {
				"url"  : "x-wing",
				"fuel" : 130,
				"provisions"  : 100,
				"hull"  : 70,
				},
			"Gradius" : {
				"url"  : "gradius",
				"fuel" : 100,
				"provisions"  : 90,
				"hull"  : 110,
				},
			"Great Fox" : {
				"url"  : "great_fox",
				"fuel" : 60,
				"provisions"  : 120,
				"hull"  : 120,
				},
			"Samus' Ship" : {
				"url"  : "samus_ship",
				"fuel" : 90,
				"provisions"  : 140,
				"hull"  : 70,
				},
			"Naboo Royal Starship" : {
				"url"  : "naboo_royal_starship",
				"fuel" : 140,
				"provisions"  : 80,
				"hull"  : 80,
				},
			"Capsule Corp" : {
				"url"  : "capsule_corp",
				"fuel" : 100,
				"provisions"  : 110,
				"hull"  : 90,
				},
			"Dark Star" : {
				"url"  : "dark_star",
				"fuel" : 110,
				"provisions"  : 90,
				"hull"  : 100,
				},
			"No Man's Sky LEGO" : {
				"url"  : "no_mans_sky_lego",
				"fuel" : 150,
				"provisions"  : 60,
				"hull"  : 90,
				},
			"Galaga" : {
				"url"  : "galaga",
				"fuel" : 80,
				"provisions"  : 110,
				"hull"  : 110,
				},
			"NASA Space Shuttle" : {
				"url"  : "nasa_space_shuttle",
				"fuel" : 70,
				"provisions"  : 110,
				"hull"  : 120,
				},
			"Jimmy Neutron" : {
				"url"  : "jimmy_neutron",
				"fuel" : 120,
				"provisions"  : 110,
				"hull"  : 70,
				},
			"Astro Slug" : {
				"url"  : "astro_slug",
				"fuel" : 120,
				"provisions"  : 90,
				"hull"  : 90,
				},
			"Bentenmaru" : {
				"url" : "bentenmaru",
				"fuel" : 80,
				"provisions" : 80,
				"hull" : 140,
				},
			"Wallace & Gromit Rocket" : {
				"url" : "wallace_gromit_rocket",
				"fuel" : 130,
				"provisions" : 100,
				"hull" : 70
				},
			"Railjack" : {
				"url" : "railjack",
				"fuel" : 60,
				"provisions" : 90,
				"hull" : 150
				},
			"Core Fighter" : {
				"url" : "core_fighter",
				"fuel" : 90,
				"provisions" : 150,
				"hull" : 60,
				},
			"Mystery Ship" : {
				"url" : "mystery_ship",
				"fuel" : "random",
				"provisions" : "random",
				"hull" : "random"
				},

			}
		if name:
			self.get_properties()

	def get_properties(self):
		self.path += self.properties[self.name]["url"]+".png"
		if self.name=="Mystery Ship":
			self.fuel = np.random.randint(1,150)
			self.provisions = np.random.randint(1,150)
			self.hull = np.random.randint(1,150)
		else:
			self.fuel = self.properties[self.name]["fuel"]
			self.provisions = self.properties[self.name]["provisions"]
			self.hull = self.properties[self.name]["hull"]

class Item:
	def __init__(self,name=""):
		self.name = name
		self.text = ""
		self.url = ""
		self.type = ""
		#self.urls = {}
		self.properties = {}
		self.pretext = ""
		self.icon = "resources/borger.jpg"
		self.description = ''

	def action(self,spaceship):
	        return spaceship

	def get_type(self):
		return self.type

	def get_url(self):
		return self.url

	def set_url(self):
		self.url = self.properties[self.name]["url"]


class Consumable(Item):
	def __init__(self,name=""):
		super().__init__(name)
		self.type = "Consumable"
		self.pretext = "You used the item {}".format(self.name)
		self.properties = {
			"Self Destruct Button": {
				"url": "https://t1.rbxcdn.com/9f5dc5b3eb9c8b9be20eabdde350f429",
				"use": self.destruct,
                "description":'Blow up the ship',
				"text": "Your ship has been destroyed"
			}
		}
		if name:
			self.set_url()
		self.get_properties()

	def use(self,spaceship):
	        self.properties[self.name]["use"](spaceship)
	        #spaceship.item=None
	        return spaceship,self.pretext+". "+self.text

	def get_properties(self):
		self.description = self.properties[self.name]["description"]
		self.text = self.properties[self.name]["text"]
		#self.bad_text = self.properties[self.name]["bad"]
		self.url = self.properties[self.name]["url"]

	def destruct(self,spaceship):
		spaceship.modify_fuel(-spaceship.fuel)
		spaceship.modify_provisions(-spaceship.provisions)
		spaceship.modify_hull(-spaceship.hull)
		return spaceship

#class SelfDestructButton(Consumable)
#	def __init__(self,name=""):
#			super().__init__(name)
#			self.text = "Your ship Self Destructs."
#			self.urls = {
#			"Self Destruct Button": "https://t1.rbxcdn.com/9f5dc5b3eb9c8b9be20eabdde350f429"
#			}

#	def use(self,spaceship):
#		spaceship.modify_fuel(-spaceship.fuel)
#		spaceship.modify_provisions(-spaceship.provisions)
#		spaceship.modify_hull(-spaceship.hull)
#		spaceship.item=""
#		return spaceship


class Equipment(Item):
    pass
