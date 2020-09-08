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

	def get_url(self):
		return self.url

	def set_url(self):
		self.url = self.urls[self.name]

	def get_properties(self):
		self.good_text = self.properties[self.name]["good"]
		self.bad_text = self.properties[self.name]["bad"]
		self.url = self.properties[self.name]["url"]

class Start(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.icon = "Resources/Start_icon.png"
		self.type = "Start"
		self.bad_chance = 0
		self.good_text = "You're back where you started you silly space-goose"
		self.urls = {
			"Start" : "https://b.rgbimg.com/users/x/xy/xymonau/600/mVExAYa.jpg"
		}
		if name:
			self.set_url()

	def good_action(self,spaceship):
		return spaceship

class Goal(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.icon = "Resources/Goal_icon.png"
		self.type = "Goal"
		self.bad_chance = 0
		self.good_text = "You've reached your destination: {}.".format(self.name)
		self.urls = {
			"Earth" : "https://media.npr.org/assets/img/2013/03/06/bluemarble3k-smaller-nasa_custom-644f0b7082d6d0f6814a9e82908569c07ea55ccb-s800-c85.jpg",
			"Treasure Planet" : "https://vignette.wikia.nocookie.net/disney/images/2/2d/Treasure-planet-disneyscreencaps.com-233.jpg/revision/latest?cb=20130403024637",
			"The Restaurant at the end of the Universe" : "https://i.pinimg.com/originals/f7/f7/ff/f7f7ffa4375050aa74c360b9ea65a0ef.jpg",
			"Continuum Transfunctioner" : "https://wiki.godvillegame.com/images/0/03/ContinuumTransfunctioner.jpg",
			"Earth 2" : "data:image/jpeg;base64,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",
			"Iscandar" : "https://pbs.twimg.com/media/DhHHnUPWAAAA481.jpg",
			"Atomsk" : "https://external-preview.redd.it/OKCV2DA85ahjhviQ_mABxubFXz-dYY_P5N288vyiWO4.jpg?auto=webp&s=70b011a9e0a4aa8c700d13152da4cde14eb99f42",
			"The secret to life the universe and everything" : "https://i.pinimg.com/originals/95/c9/7b/95c97bfb99926952c1d9af2c68d6f5b1.png",
			"Planet Ohio" : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSjsEYb9SwkLJXaBSkdF9FJJL8tRKjJYNv5Kw&usqp=CAU",
			"The edge of the universe" : "https://specials-images.forbesimg.com/imageserve/5f1774a1558c7c0006dd7785/960x0.jpg?fit=scale",
			"Boobies Brestaurant" : "https://space-dandy.fandom.com/wiki/BooBies",
			"Venom" : "https://vignette.wikia.nocookie.net/starfox/images/2/2d/VenomDeserted.png/revision/latest?cb=20130407161739",
			"What its based on" : "https://pbs.twimg.com/profile_images/1248509273/39198_1571854573776_1157872547_31663366_5779158_n.jpg",
			"A plant" : "data:image/jpeg;base64,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",
		}
		if name:
			self.set_url()

	def good_action(self,spaceship):
		spaceship.isHome = True 
		return spaceship

class Planet(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.5
		self.type = "Planet"
		self.icon = "Resources/Planet_icon.png"
		self.pretext = "You've reached planet {}".format(self.name)
		self.properties = {
			"Mars":{
				"good" : 'You find water in Mars, your provisions increase by 10.',
				"bad"  : "Martians rob you of 10 provisions.",
				"url"  : "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg"
				},
			"Solaris":{
				"good" : "Your ex-wife's ghost helps you find food in the abandoned base, you get 10 provisions.",
				"bad"  : "Your ex-wife's ghost manipulates you into leaving her 10 provisions.",
				"url"  : "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Solaris.jpg/400px-Solaris.jpg"
				},
			"Tatooine":{
				"good" : "You befriend an orphan that gifts you 10 provisions because you 'look like an angel'.",
				"bad"  : "Jawas steal 10 of your provisions.",
				"url"  : "https://vignette.wikia.nocookie.net/starwars/images/b/b0/Tatooine_TPM.png/revision/latest/top-crop/width/720/height/900?cb=20131019121937"
				},
			"Trantor":{
				"good" : "Prime minister Eto Demerzel gifts you 10 provisions for your services to the Empire.",
				"bad"  : "You wind up in Billibotton and get mugged with knives. You lose 10 provision.",
				"url"  : "https://i.pinimg.com/originals/71/eb/53/71eb5317dd4b68f1df54e4eab5ce8fc7.jpg"
				},
			"Pandora":{
				"good" : "You fuck a blue alien, while they're asleep you take 10 of their provisions.",
				"bad"  : "You fuck a blue alien, you give them 10 provisions for the cure to space AIDS.",
				"url"  : "https://vignette.wikia.nocookie.net/james-camerons-avatar/images/8/89/Luna_Pandora.png/revision/latest?cb=20150307030147&path-prefix=es"
				},
			"Magrathea":{
				"good" : "Slartibartfast gifts you 10 provisions for listening to his talk about fjords.",
				"bad"  : "10 provisions are taken from you as material for a planet made of food.",
				"url"  : "https://www.42magrathea.com/images/magwel.jpg"
				},
			"Gallifrey":{
				"good" : "You pick up 10 provisions from the corpse of a Gallifreyan.",
				"bad"  : "10 of your provisions are destroyed in the crossfire between Daleks and Time Lords.",
				"url"  : "https://vignette.wikia.nocookie.net/doctorwho/images/a/a3/250px-Gallifrey_modern.png/revision/latest?cb=20120122132630&path-prefix=es"
				},
			"Roboworld":{
				"good" : "You catch 10 provisions that come flying out of a Redline's competitor's vehicle.",
				"bad"  : "10 provisions get destroyed by a blast from Funky Boy.",
				"url"  : "https://vignette.wikia.nocookie.net/topstrongest/images/8/89/Funky_Boy.jpg/revision/latest/scale-to-width-down/340?cb=20160913005120"
				},
			"Hoth":{
				"good" : "You scavenge 10 provisions from the still warm corpse of a Tauntaun.",
				"bad"  : "You throw 10 provisions to distract the Wampa that's chasing you.",
				"url"  : "https://upload.wikimedia.org/wikipedia/en/d/d2/Hothplanetsurface.jpg"
				},
			"Terminus":{
				"good" : "You buy 10 provisions at the market of Terminus City.",
				"bad"  : "The Enciclopedists demand that you give them 10 provisions simply because you are dumb.",
				"url"  : "https://vignette.wikia.nocookie.net/asimov/images/c/cf/Terminus-0.jpg/revision/latest/scale-to-width-down/340?cb=20150119102940"
				},
			"Naboo":{
				"good" : "You land in Naboo and befriend the locals. They gift you 10 provisions",
				"bad"  : "You fall in love with the princess but cant have sex with her. In impotence you lose 10 provisions",
				"url"  : "https://uncyclopedia.ca/w/images/3/3c/Naboo.png"
				},
			"Thanos farm":{
				"good" : "Thanos farm. You get 10 provisions",
				"bad"  : "Thanos farm. You lose 10 provisions",
				"url"  : "https://mcucosmic.com/wp-content/uploads/2018/07/0408_titan_ext_titan_50s0z.jpg"
				},
			"Krypton":{
				"good" : "Marlon Brando teaches you good morals. You get 10 provisions",
				"bad"  : "Just as you are arriving you see a baby fly by and the planet explodes. You lose 10 provisions",
				"url"  : "https://upload.wikimedia.org/wikipedia/en/0/0a/Krypton_%28DC_Comics_planet_-_circa_2018%29.jpg"
				},
			"Arrakis":{
				"good" : "You become a Messiah-like figure and lead the sand people on a Jihad. You get 10 Spice",
				"bad"  : "You barely escape the jaws of a sandworm. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/dune/images/a/af/Arrakis_planet.jpg/revision/latest/scale-to-width-down/340?cb=20190804030356"
				},
			"Fezzan":{
				"good" : "You entered mutually benefitial business agreements. You got 10 provisions.",
				"bad"  : "You violated the NAP, Fezzan funds terrorists against you. You lose 10 provisions",
				"url"  : "https://gineipaedia.com/w/images/thumb/d/db/Phezzan.jpg/300px-Phezzan.jpg"
				},
			"Orous":{
				"good" : "You inherit Earth. It comes with 10 provisions",
				"bad"  : "You spend a week doing space bureaucracy. You eat 10 provisions in the process",
				"url"  : "https://vignette.wikia.nocookie.net/jupiter-ascending/images/9/90/JA_MethodStudios_VFX_11.jpg/revision/latest/scale-to-width-down/250?cb=20150325201031"
				},
			"Mars Colony":{
				"good" : "You restore Mars' atmosphere and make out with a hot chick. You get 10 provisions",
				"bad"  : "You may or may not be a secret double/triple agent whose memory was wiped intentionally or unintentionally once or twice. In the confusion you lose 10 provisions",
				"url"  : "https://3.bp.blogspot.com/-ulLqOBJWHWI/VgGE5XVBP2I/AAAAAAAABOk/HKJiC9PewJs/s2048/01%2BAstronauts%2Bon%2BMars%2BTotal%2BRecall%2B1990%2Bmovie%2Bimage.jpg"
				},
			"Namek":{
				"good" : "You achieve SUPERSAIYAN. You get 10 provisions",
				"bad"  : "You arrive just as a midget and a monkey destroy the planet. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/dragonball/images/7/71/Namek_U7.png/revision/latest/top-crop/width/360/height/450?cb=20171203031332&path-prefix=es"
				},
			"Kaisoma's Planet":{
				"good" : "Kaisoma trains you to get stronger. You get 10 provisions",
				"bad"  : "You arrive just as Goku teleports with an exploding Cell. Pretty dick move. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/dragonball/images/e/ee/King_Kai%27s_Planet_-_Battle_of_Gods_-_001.png/revision/latest?cb=20170827070415"
				},
			"Planet Vegeta":{
				"good" : "You have somewhat returned to monke. You get 10 provisions",
				"bad"  : "You are attacked by monkeys. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/dragonballupdates/images/d/d6/PlanetVegetaBeforeItWasD.png/revision/latest/scale-to-width-down/340?cb=20120623144156"
				},
			"Broly Culo":{
				"good" : "You landed on his Culo. You get 10 provisions",
				"bad"  : "The Culo sucks you up. You lose 10 provisions",
				"url"  : "https://pbs.twimg.com/media/D0G8D8OU8AYYyUy.jpg"
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
			"Cybertron":{
				"good" : "Optimus Prime gives you an inspirational speech and 10 provisions",
				"bad"  : "Starscream betrays you. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/bumblebee/images/9/97/Cybertron.jpg/revision/latest?cb=20190405051850&path-prefix=es"
				},
			"Unicron":{
				"good" : "Unicron shares with you some of Paul Masson's French champagne and you get 10 provisions",
				"bad"  : "Unicron was set up to be in the next movie but the series was rebooted. You lose 10 provsions",
				"url"  : "https://vignette.wikia.nocookie.net/robotsupremacy/images/5/59/Transformers-Unicron.jpg/revision/latest/scale-to-width-down/340?cb=20120516141332"
				},
			"Zebes":{
				"good" : "A metroid mistakes you for his mom and gifts you 10 provisions",
				"bad"  : "You get attacked by space pirates and lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/metroid/images/9/93/Zebes_MSR.png/revision/latest?cb=20171104034134&path-prefix=es"
				},
			"Uranus":{
				"good" : "Hehe. You get 10 provisions",
				"bad"  : "Hehe. You lose 10 provisions",
				"url"  : "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg"
				},
			"Galvan Prime":{
				"good" : "Momento Galvano. You get 10 provisions",
				"bad"  : "Momento Galvano. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/ben10/images/9/99/Galvan_Prime2.png/revision/latest?cb=20130712163200&path-prefix=es"
				},
			"Capitan del espacio":{
				"good" : "Best Alfajor of the south area. You get 10 provisions",
				"bad"  : "You dont understand what an Alfajor is. You lose 10 provisions",
				"url"  : "http://muy.clarin.com/files/2016/11/2016/11/01/20161101112351_26496014_0_0.jpg"
				},
			"Pluto":{
				"good" : "This isnt a planet but you get 10 provisions",
				"bad"  : "You were sued for copyright by Disney. You lose 10 provisions",
				"url"  : "https://cdn.mos.cms.futurecdn.net/jGqBq44gCE3CogJTXAnwjT-1200-80.jpg"
				},
			"SCP-3003":{
				"good" : "The inhabitants gift you some weird beetles, you guess they're safe to eat. You win 10 provisions",
				"bad" : "You are weirded by everyone's lumps so you run away while dropping 10 provisions",
				"url" : "http://scp-wiki.wdfiles.com/local--files/scp-3003/3000.jpg"
				},
			"The Moon":{
				"good" : "A tear falls for the moon, a Deku scrub trades you 10 provisions for it",
				"bad" : "Oh shit, oh fuck. You lose 10 provisions",
				"url" : "https://i.kym-cdn.com/entries/icons/facebook/000/009/820/moon-stares-at-link-in-the-legend-of-zelda-majoras-mask_288x288.jpg"
				},
			"Macragge":{
				"good" : "The chapter master pays you for your services with 10 provisions",
				"bad"  : "Just as you arrive the Tyranid Hive Fleet Behemoth invade. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/warhammer40k/images/e/e3/Macragge2.png/revision/latest/scale-to-width-down/310?cb=20170802085537"
				},
			"Coruscant":{
				"good" : "You got some death sticks. You got 10 provisions",
				"bad"  : "You witness the collapse of democracy. You lose 10 provisions",
				"url"  : "https://star-name-registry.com/blog/user/pages/01.item/top-15-fictional-planets-in-science-fiction/name_a_star-planets-5.jpg"
				},
			"Mustafar":{
				"good" : "You have the high ground. You got 10 provisions",
				"bad"  : "You dont have the high ground. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/es.starwars/images/a/af/Mustafar_DB.png/revision/latest?cb=20160725161845"
				},
			"Ego":{
				"good" : "Your Planet-Dad gives you 10 provisions",
				"bad"  : "Your Planet-Dad steals 10 provisions from you and gives your mom cancer",
				"url"  : "https://oyster.ignimgs.com/wordpress/stg.ign.com/2017/03/Ego-The-Living-Planet.jpg"
				},
			"Space Ghost Coast to Coast":{
				"good" : "You are a guest in the show. You get 10 provisions",
				"bad"  : "Zorak attacks you. You lose 10 provisions",
				"url"  : "https://hbomax-images.warnermediacdn.com/images/GXnPCXw10BaFYqQEAAAKk/tile.jpeg?size=1280x720&format=jpeg&partner=hbomaxcom&productCode=hbomax&host=artist.api.cdn.hbo.com&w=480"
				},
			"Space Colony Neo Mexico":{
				"good" : "Orale wey, you buy a Taco. You get 10 provisions",
				"bad"  : "You get shot crossing the border. You lose 10 provisions",
				"url"  : "https://i.redd.it/rlr07vn0awd31.jpg"
				},
			"Yugopotamia":{
				"good" : "Yugopotamians try to poison you with chocolate. You get 10 provisions",
				"bad"  : "Yugopotamians try to share their food with you but its shit. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/fairlyoddparents/images/5/59/Planet.png/revision/latest?cb=20100612164014&path-prefix=en"
				},
			"Lifeforce Spaceship":{
				"good" : "You make out with naked space vampires. You get 10 provisions",
				"bad"  : "You get the blood suck out of your body by space vampires. You lose 10 provisions",
				"url"  : "https://i.pinimg.com/originals/d3/42/cb/d342cba8245717f18a44cc6cd06ea1b7.jpg"
				},
			"Brexit means Brexit":{
				"good" : "You find whats left of the british empire. You buy fish and chips. You get 10 provisions",
				"bad"  : "British 'people' try to colonize your ship. You lose 10 provisions",
				"url"  : "https://i.redd.it/em0cfvj3bln11.jpg"
				},
			"Skaro":{
				"good" : " Thankfully, the Daleks don't seem to notice you, and you manage to scavenge some provisions from a nearby piece of wreckage. You get 10 provisions",
				"bad"  : " Despite your best efforts, you are noticed by the Daleks, who order you to surrender or be exterminated. After begging for your life, they agree to let you go in exchange for some provisions. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/tardis/images/4/4a/Skaro.jpg/revision/latest?cb=20120405231507"
				},
			"Dark Star (Kirby)":{
				"good" : "You get a crystal shard. You get 10 provisions",
				"bad"  : " You fight 02. You lose 10 provisions",
				"url"  : "https://i.ytimg.com/vi/fgTBv9jkq2Q/hqdefault.jpg"
				},
			#Reach, Todos los demas de Star Wars, Vulcan, el resto de los IRL
			}	
		if name:
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
		self.icon = "Resources/Portal_icon.png"
		self.pretext = "You find a {}".format(self.name)
		self.urls = {
			"Wormhole" : "https://qph.fs.quoracdn.net/main-qimg-79f468932c9222c1648c31fbe6112fbe",
			"Wormhole (marvel)" : "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/2/23/Space_Stone_Wormhole.png/revision/latest/scale-to-width-down/340?cb=20180826084239",
			"Mass Relay" : "https://i.ytimg.com/vi/BDq4a6PqAvM/maxresdefault.jpg",
			"Infinite improbability Drive" : "https://i.redd.it/g8ofhhot01qz.jpg",
			"Warp Station" : "https://vignette.wikia.nocookie.net/pulsar-game/images/2/24/Long_range_warp_station.png/revision/latest/scale-to-width-down/340?cb=20190626124313",
			"Portal" : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT-HfXb1DmwshWvAErqfe4mxV7GAZtPQ0wpZw&usqp=CAU",
			"Bifrost" : "https://i.ytimg.com/vi/hzqWcXA_Xrk/maxresdefault.jpg",
			"Portal (R&M)" : "https://i.pinimg.com/originals/98/29/21/9829215db6f9210c0ae4e318e854cb1f.png",
			"Time hole" : "https://vignette.wikia.nocookie.net/reddwarf/images/c/c3/Time_Hole_%282%29.jpg/revision/latest/scale-to-width-down/340?cb=20150502013436",
			"Time vortex" : "https://thumbs.gfycat.com/DigitalGreenCoral-mobile.jpg",
			"Stargate" : "https://www.stargatecommand.co/sites/default/files/2019-10/CGI%20Stargate.jpg",
		}
		#Wormhole, portal, warp station, improbability drive
		if name:
			self.set_url()
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
		self.properties = {
			"Millenium Falcon":{
				"good" : "You entered a dogfight with it. You managed to steal 20 fuel from Disney",
				"bad"  : "You entered a dogfight with it. You received damage by 10 hull",
				"url"  : "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/veh-ia-1751-1576604159.jpg?crop=0.583xw:0.658xh;0.207xw,0.220xh&resize=640:*"
				},
			"Swordfish":{
				"good" : "You encounter bounty hunters. They gift you 20 fuel",
				"bad"  : "You entered a dogfight with the The bebop. You received damage by 10 hull",
				"url"  : "https://i.pinimg.com/originals/df/06/f0/df06f0e92ff45d482ceba427a5c5a2cf.gif"
				},
			"Arwing":{
				"good" : "You destroyed Slippy. You got 20 fuel",
				"bad"  : "You entered a dogfight with Starfox. You tried and failed to do a barrel roll receiving damage by 10 hull",
				"url"  : "https://www.pngitem.com/pimgs/m/17-174687_transparent-arwing-png-starlink-star-fox-arwing-png.png"
				},
			"Aloha Oe":{
				"good" : "You seduced Dandy and got 20 fuel out of him",
				"bad"  : "Dandy caused some apocalyptic shit in your vicinity. You received damage by 10 hull",
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
				"bad"  : "You barely escape its cannon. You received damage by 10 hull",
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
				"url"  : "https://ti-content-global.cdn.turner.com/PROD-APAC/C_REGSHO_0XXXX0141_REC_AFRICA/C_REGSHO_0XXXX0141_REC_AFRICA_VIDSCREENSHOT.jpg"
				},
			"Gunbuster":{
				"good" : "You get sent 12000 years into the future but there's someone waiting for you with 20 fuel",
				"bad"  : "You get sent 12000 years into the future. Your hull is damaged by 10",
				"url"  : "https://vignette.wikia.nocookie.net/gunbuster/images/9/9b/Gunbuster.jpg/revision/latest/scale-to-width-down/340?cb=20150817233125"
				},
			"Cathedral Terra":{
				"good" : "You discover that your unconquerable human spirit moves foward like a drill and pierces through the heavens. Spiral power materializes 20 fuel in your ship",
				"bad"  : "You are a bitch ass utilitarian and dont understand spirals. Your hull is damaged by 10",
				"url"  : "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/39c5b551-082f-4d2b-9d39-8e68cee8ba39/d8fq6iy-156bebaa-2d36-4d5a-b6b2-283643472d6a.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMzljNWI1NTEtMDgyZi00ZDJiLTlkMzktOGU2OGNlZThiYTM5XC9kOGZxNml5LTE1NmJlYmFhLTJkMzYtNGQ1YS1iNmIyLTI4MzY0MzQ3MmQ2YS5qcGcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.1nstNgcN3QJ9mciTya7CN4h9TEpYbXgob_I7V-t0hn0"
				},
			"Yolkian Ship":{
				"good" : "You defeat the eggs trying to kidnap your parents. You get 20 fuel",
				"bad"  : "Eggs kidnap your parents. Your hull is damaged by 10",
				"url"  : "https://vignette.wikia.nocookie.net/jimmyneutron/images/8/86/IMG_2416.jpg/revision/latest/scale-to-width-down/340?cb=20190224204450"
				},
			"Event Horizon":{
				"good" : "You spend some quality time with Sam Neil before being sent to hell. You get 20 fuel",
				"bad"  : "Oops, you are in hell. Your hull is damaged by 10",
				"url"  : "https://i.pinimg.com/originals/57/47/bc/5747bc4aee4a76741d316333e6b184c3.jpg"
				},
			"Kang and Kodos' Ship":{
				"good" : "They feed you and teach you how to cook for forty humans. You get 20 fuel",
				"bad"  : "You voted for Kodos. He still impregnates your wife. Your hull is damaged by 10",
				"url"  : "https://static.simpsonswiki.com/images/thumb/a/a4/Broken_spaceship.png/250px-Broken_spaceship.png"
				},
			"Firefly":{
				"good" : "You get renewed for a second season. You get 20 fuel",
				"bad"  : "You get cancelled on the first season. Your hull is damaged by 10",
				"url"  : "https://i.pinimg.com/originals/87/98/d6/8798d68dd2aa1362eb3d7d086e00fa9d.jpg"
				},
			"Space Godzilla":{
				"good" : "You defeat Space Godzilla. You get 20 fuel",
				"bad"  : "Space Godzilla attacks you. Your hull is damaged by 10",
				"url"  : "https://vignette.wikia.nocookie.net/godzilla/images/4/4f/SpaceGodzilla.png/revision/latest/top-crop/width/360/height/450?cb=20121120020913"
				},
			"Comet Observatory":{
				"good" : "Rosalina gifts you 20 fuel",
				"bad"  : "Rosalina performs CBT on you. Your hull is damaged by 10",
				"url"  : "data:image/jpeg;base64,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"
				},
			"Barrilete Cosmico":{
				"good" : "Maradona shares a line of coke with you. You get 20 fuel",
				"bad"  : "Maradona made you a terrible dribble. Your hull is damaged by 10",
				"url"  : "https://www.agenciapacourondo.com.ar/sites/www.agenciapacourondo.com.ar/files/styles/flexslider_full/public/articulos/gol-maradona-contra-inglaterra_0.jpg?itok=Y42qBP1P"
				},
			"Capitan Beto":{
				"good" : "His ring makes you immune to danger. You get 20 fuel",
				"bad"  : "Not even a sad shadow is left. Your hull is damaged by 10",
				"url"  : "https://live.staticflickr.com/5053/5568240946_07817746e1_n.jpg"
				},
			"Von Braun":{
				"good" : "You embark on the first manned mission to Jupiter. You get 20 fuel",
				"bad"  : "You are boarded by space terrorists trying to make you feel bad about space exploration. Your hull is damaged by 10",
				"url"  : "https://66.media.tumblr.com/43856f6f427c3597a5e002a27f79627f/tumblr_inline_pq5qwycAbn1s3ca0o_540.png"
				},
			"Dalek Fleet":{
				"good" : "You wave a sonic screwdriver a bit and they explode. You get 20 fuel",
				"bad"  : "EXTERMINATE. You lose 10 hull",
				"url"  : "https://i.pinimg.com/originals/ca/97/7e/ca977ebd5dbf5dc91a1d96720c229491.jpg"
				},
			"Vengeful Spirit":{
				"good" : "Glory to the emperor of mankind. You get 20 fuel",
				"bad"  : "Sanguinus is dead. You lose 10 hull",
				"url"  : "https://vignette.wikia.nocookie.net/warhammer40k/images/a/a0/The_Vengeful_Spirit.jpg/revision/latest?cb=20150209004009"
				},
			"Voyager 1":{
				"good" : "You steal 20 fuel from the probe",
				"bad" : "The probe's security measures damage your ship. You lose 10 hull",
				"url" : "https://www.jpl.nasa.gov/missions/web/voyager.jpg"
				},
			"Remote-controlled solid gold death star":{
				"good" : "You get a code to travel through time. You steal 20 fuel from your past self",
				"bad"  : "Nudist scammers damage your hull by 10",
				"url"  : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcROfZSeCWPDkjX3dGyajO8vljEZMfIQ3PdP-Q&usqp=CAU"
				},
			"Fortress of doom":{
				"good" : "You manage to run doom on a facebook bot. You get 20 fuel",
				"bad"  : "The Doom Slayer stares at your ship and damages it by 10 hull",
				"url"  : "https://vignette.wikia.nocookie.net/doom/images/1/1f/Anotasi_2020-02-04_083440.png/revision/latest/scale-to-width-down/340?cb=20200204013550"
				},
			" ARSAT":{
				"good" : "You manage to get from Cordoba to Japan in only 2 hours. You get 20 fuel",
				"bad"  : "A general strike by the CGT damages your ship by 10",
				"url"  : "https://perfilindustrial.com/wp-content/uploads/2020/01/satelite_argentina.jpg"
				},
			"Duck Dodgers' ship":{
				"good" : "Duck saves you from martians and gives you 20 fuel",
				"bad"  : "ACME explosives go off and you lose 10 hull",
				"url"  : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTbfB0GalNqKD_47iYuyWvdSwdIFho6SrZ5UQ&usqp=CAU"
				},
			"Jumba's ship":{
				"good" : "You spend a vacation in hawaii and get 20 fuel",
				"bad"  : "One of his experiments does damage to your ship by 10 hull",
				"url"  : "https://vignette.wikia.nocookie.net/stitchipediaalilostitch/images/9/9f/Vlcsnap-2013-02-28-13h24m27s14.png/revision/latest?cb=20130228194710"
				},
			"Axiom":{
				"good" : "You get fat in an automated consumerist society and get 20 fuel",
				"bad"  : "The Ship's Autopilot detects a plant on your ship and attacks you. You lose 10 hull",
				"url"  : "https://vignette.wikia.nocookie.net/pixar/images/8/88/Axiom_Orbit.jpg/revision/latest?cb=20121127003802"
				},
			"Captain Planet":{
				"good" : "You get 20 clean energy fuel",
				"bad"  : "Indivual Enviromental responsability is a spook. You lose 10 hull",
				"url"  : "https://www.quirkbooks.com/sites/default/files/u1177/inconvenienttruth.jpg"
				},
			"Buzz LightYear's Star Cruiser":{
				"good" : "To infinity... and beyond! You get 20 fuel",
				"bad"  : "You are a sad, strange little man. You lose 10 hull",
				"url"  : "https://vignette.wikia.nocookie.net/blosc/images/c/ce/Star_Cruiser_42.jpg/revision/latest/scale-to-width-down/340?cb=20170205094038"
				},
			"Space chimps":{
				"good" : "Return to monke...IN SPACE. You get 20 fuel",
				"bad"  : "Crackhouse vibes. You lose 10 hull",
				"url"  : "https://upload.wikimedia.org/wikipedia/en/thumb/9/92/Space_chimps.jpg/220px-Space_chimps.jpg"
				},
			"Ships from Chicken Little":{
				"good" : "You bond with your chicken father. You get 20 fuel",
				"bad"  : "Sky falls on your head. You lose 10 hull",
				"url"  : "https://rotoscopers.com/wp-content/uploads/2016/10/chicklit4.jpg"
				},
			"Great Thing":{
				"good" : "You hunt the whale. You get 20 fuel",
				"bad"  : "You barely survived the whale's bullet hell. You lose 10 hull",
				"url"  : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT4NIdbZ1c0awxI_ogHz6n9Kz-vCnjmy0CgAw&usqp=CAU"
				},
			"Space Battleship Yamato":{
				"good" : "They give your ship a resupply before going back on their merry way. You get 20 fuel",
				"bad"  : "They don't seem to like the cut of your jib, so they blast you with the Wave Motion Gun. You lose 10 hull",
				"url"  : "https://i.pinimg.com/originals/20/0b/c4/200bc4fefb4d6dfca1de7f298293bacf.png"
				},
			"Red Dwarf":{
				"good" : "They trade you 20 fuel in exchange for some curry and lager.",
				"bad"  : "You crash into Red Dwarf. Seems the crew were distracted by the Cat's snazzy outfit. Your hull is damaged by 10 points.",
				"url"  : "https://i.redd.it/olaipznagcty.jpg"
				},
			"Tylor's Landeel":{
				"good" : "You exchange A-Photon reactors with Tylor for fuel. You get 20 fuel",
				"bad"  : "Tylor and his crew try to rob your ship, but you barely escape. -10 hull.",
				"url"  : "data:image/jpeg;base64,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"
				},
			"Imperial fleet":{
				"good" : "Dock with the main star destroyer. You get 20 fuel",
				"bad"  : "Get locked by the tractor beam. You lose 10 hull",
				"url"  : "https://vignette.wikia.nocookie.net/starwars/images/b/b4/Seventh_Fleet_Star_Destroyer_SWA.png/revision/latest?cb=20180110042309"
				},
			"Ebon Hawk":{
				"good" : "The Ebon Hawk crew decides to help you, You get 20 fuel",
				"bad"  : "You come across with the Ebon Hawk being chased by the Leviathan. You lose 10 hull",
				"url"  : "https://vignette.wikia.nocookie.net/swtor/images/5/54/Ebon_Hawk.png/revision/latest?cb=20110221115231"
				},
			"Jason Bright's flock":{
				"good" : "Jason Bright thanked you for dealing with the 'demons'. You received 20 fuel.",
				"bad"  : "Jason Bright noticed you attacked a ghoul and did not like it. Your hull is damaged by 10",
				"url"  : "https://i.imgur.com/xTjmO3l.jpg"
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
		self.urls = {
			"Solar system asteroid belt" : "https://i.ytimg.com/vi/cT3K1INjQJ0/maxresdefault.jpg",
			"Fox's Satelite" : "https://i.ytimg.com/vi/jGhirX5kH_k/hqdefault.jpg",
			"ARSAT" : "https://perfilindustrial.com/wp-content/uploads/2020/01/satelite_argentina.jpg",
			"Grob gob glob grod" : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTMaD_qZs0ajJ5MQUUFAw8ROk2U-oHvGY2d7Q&usqp=CAU",
			"Bender" : "https://vignette.wikia.nocookie.net/en.futurama/images/f/f7/GodBender.jpg/revision/latest?cb=20090716180913",
			"Hoshimachi Suisei" : "https://i.imgur.com/hQnx1ex.jpg",
			"Laika" : "https://thumbs-prod.si-cdn.com/ny8o8iWseySt4th_-e2lWHg30_A=/fit-in/1600x0/https://public-media.si-cdn.com/filer/96/94/969479c1-7e9d-4cdc-ba4a-0e4e99b6e1c9/4967208430_f5f05e968e_o.jpg",
			"Attack ball" : "https://vignette.wikia.nocookie.net/dragonball/images/f/f6/SaiyanSpacePod01.png/revision/latest/top-crop/width/360/height/450?cb=20091202134307",
			"A Baoa Qu" : "https://vignette.wikia.nocookie.net/gundam/images/8/89/ABaoaQu.jpg/revision/latest?cb=20100318202253",
			"Mansion room" : "https://vignette.wikia.nocookie.net/twinpeaks/images/2/20/3.03_Spaceship.jpg/revision/latest?cb=20170820181946",
			"Kuiper belt" : "https://image.pbs.org/poster_images/assets/npls12_vid_kuiperbelt_thumb.jpg",
			"Asteroid belt outside Hoth" : "https://vignette.wikia.nocookie.net/starwars/images/1/1b/Hoth_Asteroid_Belt_TESB.png/revision/latest?cb=20161010024439",
			"Asteroid belt from Asteroids" : "https://www.researchgate.net/profile/Kc_Collins/publication/262309733/figure/fig2/AS:694796872081408@1542663891658/Original-vector-based-Asteroids-game-Atari-1979-showing-ship-in-centre-and-floating.ppm",
			"Halley's Comet" : "https://specials-images.forbesimg.com/imageserve/543871022/960x0.jpg?cropX1=0&cropX2=3072&cropY1=305&cropY2=1745",
			"Space trash" : "data:image/jpeg;base64,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",
			"Kars" : "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExIVFRUXFxgXFxcXGBcXGBgXFRcXFxcXGBgYHSggGBolHRgXITEhJSkrLi4uGB8zODMtNygtLisBCgoKDg0OFxAQFSsdHR0tLS0tKysrLS0tLS0tLS0tLS0tLS0rNy0tKy0tLS0tLS0tLS0tLS0rLS0uLTc3Kzc3Lf/AABEIAN8A4gMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAABAgADBAYHBQj/xAA7EAACAQMCBAQDBwMEAQUBAAABAhEAAyEEEgUxQVEGEyJhMnGBB0KRobHB8BQjclJi0eHxM2OCssIV/8QAFwEBAQEBAAAAAAAAAAAAAAAAAAECA//EABwRAQEBAQEBAQEBAAAAAAAAAAABESECMUFhEv/aAAwDAQACEQMRAD8A4sBQqVK2qVIxNSoagFGKlGggqRRpitVCGjRipFFSKJFAUZoBFACmFTbUAogVZYtFmCjmSAOgyYknoPer9fYVXhH8xQBLRt9X3gBPKasiMSmHehRC5ooH5VKJFLQSiBJqEcs/9UyXCJjqCDyOD8+XzFAvPvNIaehQEVAJqyxbJMCOszy5E/jiaVj78sDpVBAqEUFNM7SPfqZ5z7fjXSZiEqVKlBUxmhTEiewpa5KK945Hry+tNeSGIkGDEjI+ntSio3tUApkNLFEGgamHKlBplFUShRoEUAo1KIoHtpJgZrZuJeFyqaN0hRqbYY72+AiN7tPwpmfpWv6HUNbdLiGHRldSMncpBXHXIGK2TjvE9RZuf3SVviytvIGLTL8Bkc5Y/KI6UiV4etuhP7VtApUbWYGSxky0zEkECBgACqbOqUepEAYIVKkbg0zLexAI+orF2yffn8/l70WJxnl36VrUIv44/gpwar35qysqk0IqVJoqUCKNCgdBNEKIHeeUdMdfx/Ck3Zk04uHAnEz8qCai4GZiFCySQq/CJ6D2FITI5U1xY/X8eVKqyecVQFWrdQx9IKBSqxgQWn1At3MEZ7RSotFuv8+taxCVKMVKqKKMUTUFc2hHyoUZqUAoU1SKgiLNMKiLRqiE0KlMooFAoxXv+GfDlzWXRbt4yNzn4UBMSas8Q+E72luNbfa21tu5SCJPLHMUxGB4f0rPetmQoVg24mApUyGPsCOXXlWT451LPq3d38wkCGmdwEgH2+XTlXnWLDyERjJOQJAAXmxPYCa9FOCNcY+vcxtG4CMzdFsXfKYn723d9RVxHgZ60AmJis69oyttLm4RcLqMZGzbP/2FYpc8iM8v571cFAq4UGXv/PY0WwAfbNSwlGpFIXpkY8qmNaNLNQ/KiGohg2DSiofaoBRTBcfj+HeiFpTR3VYhlkZBiosf9/IHFQ0rCthTUokVKmKqFPaSSBBM4AXmSeUfWlApk54xHUdPesgGio+Q69c+1QxQoJUijUqB2M0hNMRS0Eq2wM1XVlnnUHe/sY4Ih0j3CJN1mVv8VgAfOZP1r0/tH4enlxNud6sS4UelgUzHqbMfKQelaX9lXiO5at3bAIn4re4xlsFVwZMgGPnT/aXxO7uVbqw7I6mQZ2l5B7SIx7MarLQOD8Ha69025ZUI3bQZ2s0AgATmK6Zr/D1u1b0+usWyLKFTcCzhCTN2IkkIWUnrAPeuccB4wNPcPx7HgPsbazAGRB5SPfFdYbiya2wycLu3BeKs1zTXNqqyMNtwAcg0mfSe886XiufeKOB3Tb0dm0i3FK3WtsgMlXun1OemFGfxrRNTbKMVMSpKmMjBI59RjnW6a6/r9KG0m25b8wfCVO8BssLZ5qrEZA5xWri2gRtwc3D8AEBR3LTz+VaiVg7uoE9/53pWtwBmsi/vPrIiT2gT7RisVzVQimnGeVI/PFXJgT0qKBEEZo7KEgt1A/GrlXHX9vesqQLTBacCga1gVlpYq1hSMKYFqGmmgTPXlypoSalSpUUoo0JqTQSjUqUBFSoKNADUqVAKyJXq+HOGHUX1tw2yd1xlBJW2CNxx+A9yK8+1aJIAEk4Fe5o+HsiunmqN6ywW4wlVnGBD9cE/SrIldJ8D8YtXdbeItKlizZBWFAKpahUHYEyxI7mvX+0m6uqZEtmyHsjed5BkNB24kRHMGuaeD9G93zdPaubN43GZ9SWxugkDueQ6xXVjprWjts406kC0Le9lADscbwYyTuM/L3FVHCeJ2XS6Sy7d3qGIUq3Jl/2mukfY5c0hd1v4vM6eS8lYgNgMDgk/jIFaTxjiJuW1s3Lfqt7tjZBEkGDP3YmAIAro32JWNPetaixdto5DJdG4CQIKyDzEEfnT18G1+IOHMqai692zqNgAVLihnX1SFlTIboM561xXiw04t+oXVuSZ8u2otx0BLkEn5VsXG7TNrRp9PcuAXXV4DEkMzF1knmVBH1o8W8CXSl3U3NYl+za3bj5hLEoY2QRhpxTzwrmDMSYJMdKRu3Q1l6wqbjbRtUsYHYE4H0qvV2gu2Pi5ntHb5/sa0jDK5og09y0eYBjn/PalYUUwxH61lgVgrmr1bbz5UgyDEe9IKKuD1zQIqqkYpCKY0DRCssYPMYIpDTmgRWapKlGalRVVGhTVAwXE9uf15UKlEUEolvwqUwtMQSBMCT7fOgjWiAG6GY94waloTT6m+zBQXkKIVf8ASOwA5Vbw6xvYKBM8h71cTW4eFvD02DqHAO4lUBncFHN17ZxPt7151trUHcpDAfEZgYIgAECOVdY4xwTyOG7EXNu2Fk5MgZ2/Wa5Fq9RMSRIgmBGc7h2nNb+Mvf8ABHFbtjK2UvCd8FQSkQNweJUZis3iX2ka4uZ8opz8o25QAf5ZPzmugfZLwe3b0P8AUMFBuktJiAi+lZ9sE/WtG+0nTaNNv9OSbrFy7KNqnfBHOfSBIgVjZVaz4x8RLr2S8NP5V0DZc2SVfaPSQOmP0pvs3435GrB3bBct3LJOYBuL6CQucOF5Ca1O7uQkbiPkcH8Kt0N0qyvOVYMPcqQw+uKuDc+O6trHEDfR7asCroEJYJEbVMgZEZBry+GXtRqtTcVWWLpc3muYtKrmWdu0EyOsxFev9pHiLSas2bmna4W2+tX+4ewJyfxjFa/a1NkPp1KzaW2Dd/33GJLH3iQADHwipPg8r+hZnfZ6lUn1DlAMbvYHGfevQTw/cu6hbFlrb3GQMBuAUsROwNy3dI74rYuAeKro821bW0pYYPloT6Jldx5KROK83xRodRpNX5lwKl07bw2bdoJMgqFwBiYq6NeZHtMQVIIJV1I6qYZWHsaxQoMgfScfT2rfNVwK7r7P9bbfzbzswuWlHqLW1BZ/SIAgjnWi3bftmrqMYtGKIf8AD9Ka+OsR+n09qrtjOairESrls4kn+fvS21g/SrSaoj8h+H/ikmiagFFAihNE0DQhKlPA7/lUqCoDBqCgKlZUaK0BVlkZqDN4bw57zrbQSzGAPn+3X6VtreGrCG5aZ3BtqRcfaYVywAZ7ZE7IPNc5BrbvsL4GrPd1LLO0eWnsWEufwgfU1vvjfhtryXu+Sm8rt3sO3IGCCREj2xV3EfMt3RFZIhlUwWEx+dbh9nPC3uXLzKgMKPUIhWJBWPckAY968HiWiuWmuK42kRK5zuyPpFbl9nKahbBu2mGwX1N1CB8Cr8THqoLcvatsum8XtXrujZUZVubSZYbeU+kEH0zMTXANaxSU2xkTMyDzjPLnXfeJbWsOgdiACp2czGInpIPfrXG9Zw9gzkHbbid1wEAlYX0YmTgcvrVsI679lNxn0NtLoEW2ZUEyGQwymOuSR9K8H7W9Zpypt2kC3rJ3bxCgBsMpUfETA/X5+d4U1WpthtKb3lElYVF3NsMElYEAnHqPLHesfxN4dupZ27idzOSxwbgBkAkzIn86x/nq65HqXkkmqzI64r1dZwtgYIiTHfl8u1ebdUiRWkAycVnWL6hdjLJBkFSBkiMnrmPzrAVSRz5UEk0HqW8KHUjnBA5/KP3rbfG3G/661Zvm2FZbYttAySsnd7iD+laICy45iZ95rOHEGKbASRkATy3ZOCKD2fBPH20mpS4uIOeZVlPxIyjuOo5GvX4xwLT3pv2Xa0G9XltF1i1wlgUVMi2J65xyrR9OJb+TNbDb1DJZL2zINvY4IiAPVOD0PWmDWtbpyrFecYnP71iGe1bHptOGs3LrMC6kFQx+IzmB1IGc1h2W0xU+atzeYAKwFEnLHvA6Uo81LvLvyq2aXW6Y2rhXmOh6MvcexpQ1Z1qLJqTSyIFMonAEn2qygmkpm+f/AEarJoH3+w/P/mpSRUopBQqUZrIlXafnVNWWjmoPoz7F2ReHycTdcknl0UZ716/ijjmle01piHU22donCriVgfFJEVon2QcbQ6W9pXG71hwJyVcAGPcMAfrW0abi1gojsluxa8ki9cIMLJIW2s8yCH+o96YjV/F1vftF63bh7KxqCsOwEAhh9xk+IxmI714/hS+qLq9AxM3AwRoXmoJEkZk4xVvGPHTvdueRsayGV1FxMKUTYHAOcwDB6gVgW/FFx0DKttA3puHy0G5pk3PMid3/ADWpMSum8Gsgadl3Fi4BZvigsik8+YwK0Xi3BnuqWtsbm64QAqnYgIIjqSYgY5ZrfNRq2t6c3QpZmQbVMgksGgR90xFeF4T1N4WgVRxbI9ZDP6ZYetF5Bobp9edb9Mxn+GOGixdtK9j+6bfMwYLHmTJLR7nHati8X6ZvIKhVdQIz8S/7/eK9JNOLb2myQRtkySCYIOTjkfxr0r9oOpU8iIrnb3jWOO6vglu45cBrQtoDcdwGJ3CdxTBCmOkmub+KdHbFx2V09RJUKCqkdCoP3T0HPmDXceKcJVncNeWTCqYDPsyoXaOcEt6j0rhHHdQp9BXKyNwMhjMBhAwsAYre6jzNFpGZHIJ5chHcY7n6VlW7FtzOUYgQo5SIkknl1/KsWztUEksWxtjEdzWWAgtrMl9+f8I6H3J/KqLLgU2+S7oUR2CkiSf9WPzrF1tqDyA5Enod3X8OUVka51b4BtHID/b0k9TVTtMljJj59AP0GKDEtoYLf6Yz2nA+Yr3/AA9wtL1nVvcuFPKtB0YQAWJICMezRAHc14Fuxk5A2ic9Y/etytW7drhEMUL37+9hu9aC0P7YA/3bmM8s1mrGjrcPevT4DoLd1yb11LdpBufcT6oPwLGZPtyE15tpBu9UxOY/OhqCFJCmR0MR+Ip+IzPE3FBqLxuraS0sBVt2xCqFxj9Z968+3ypEFWgVlpKZGIyCQe4x7UAKbbSRUHKf5NLFOq9KIt4Hc4jrVFNSmgd6lEVUTSzUFRTRViLSpXQ/A/hO3qbbepWuSDGfQhjPuTkfSrJqWvB8Im8NTbNj4wwPMgbZzuI5L3roXE+C3Llwu93dcZtw9H9uSAPQswJPXrXv8F8I6bTkKBLsJIJzA5tz945d6yuKaxg40743bl3sDbABSRcUxtYD6dK18+s265h4l4L5B3Myh5ykHKwDuOfSCcCPeruAcOEJ6rd25DeXYUEKYydzdSYgfvXs+ItTp9VZuBGDX8EWm+IKAgYW3Bggme+FnFeR4R0TKbeos3FAEi805shjjLiN22eU/nU1XQeC8aF4BBbe0UgQVMFjtU4nADCIn7pNbFptN5dq5bsHbc2sFY8gxwFC95EdhmvE4fxoX1KqCz2/QQQqs0P6rqlekRMdQIms/iXB7f8AYcXyl0mVukxJwWX/AE57fOpbwbJwm49ywvmqVYrtYGASQIY45Zmsu1bIXaTJiJ5VqFnxDsZbK77pDPuuRMHfC5AhlieWYrWb32iXrS+pkdvMyc7R/wC2IGY5yOlZk1WB4+d9Hdt3lvXRfYMr7oPp+7BiGXoRzxXI9be3M3Ukn5ZJJxWy+PPE9zWXd7MpAEAISVGOk1qEy3p64z/MV0nIyKNHPIojUVVcDYPMdD0NV7fp+1Bfd1c9arV2P1oMnL3GKzNNpSULSBtHLqYBOB9KDK4DpUe6guvtQsoc9QpImPpXaPtF0ujbSJbDevTxtKIWWAv/AKZg4kQesVyTVa3TzauWFa1cAG9DOwkKPUGmcmZ5c69zjPjiy2mNi1pLal7exmPqZTj1K3sBA5c6zZ1Y0fUOCxYDaO3OKwy+f0pr5/7qtJ6VQ6sRnsayVyOeOn/HtWMTGe/8NX6Z4MjtP44/eosWFMA4zPUTjuOlLVunu7WDbVaPusJU4jIpdmJ6cv35c60pBUWZEfr9ahFAioIVjGKlSB71KgxaYClphUFgx1rc/s98QvY1C/eBUpESSuTAA5kfEPkR1rSRWRotS1t1dSQykMCOhBkGqj6W4VqrTL/UzbO8LuuA42p90McxgmDWi+LvEjJda5aS42nYBX3ghGcMGwCOsDn+9ap4a49fuXDY9O3UXFJAAADzMqDgTyPtXW+NeEmuaO8GzdvBWJUyoZciJjGM/wCR7Vb6ZxyLgHFj5zlrYuIytvUutvk/mB/MxsKn9a93wLrF3lLdpj54KAByIdCXT1feIA+pMVp3EuDeXe23GVARI2+sTHw+2e/Kn0nEwCQ5JKD+ywIGwqwYHHPlTFdx4fpJLattNsJsbbwVw7m4jFWI6hgoaTOcdRXp8G11m9pihs+YqXWUqwmAJZXbd3kfnWleHuKstwXl1G63fHr3AhkfaWPmKe7AliP9Qr3uL8Rs2T5t69dt3mZzaa0olrWI3WyIKg4z8wa5/wAU3G9VZ0ejKqo2uN7JIBLXARKA8wpAwCPnXGNVqWa9cuJ6lG58giATBYqOv86V7/iezq795rb3t59TIXBTcoPMTgfLvjtWs8Ts39N/aaBuAYxmQRgE8jzGK6eUrC4ljyiCG9AxjnkZI/TtFYd0g42gQDJ7n+dKOouFV2debfOMe8/81ibz71pFgucpklcQTgD2+tMSvPrVG0z7/tU+dQPu6Gsh+JubflgDb6fnAmR9SZP0rH2xmRB/EfSh5Y5mQOhjnQV3rxOSf4KQvTR2qFzyooA4np1oW0/6qtxFMrEEVkX3rXpHLv8AjS2BBIpnuAihbOaSKsNSnJJ/QVFSauKSaM0SIpmtsU3xKghZ7EyQPwBNAN3sv5f80addMkD++g9ouY9sLUqDAIoCiJ/CiaA1BS0agz+G6prbq6mGVgw9ipkfpX0JouOjU6IhD8enLLJxvB2sueUNiPcV832zXQfsy1ge/b09wjy2YsA2ZMAlPkxVT/8AH3piNv4v4duuseVZS3cUGVty4ZUJOQIElTXNeOeG7lmS4IODEYggNBM+mAZzX0hxqy6qpR1S2AQwPPO2CvSeYz0auPfabZvWLwd9q+YgK7IInqpBJx79asqOe8N15tsZkgxInnB5fLpjvXTL+qu61NNqEZXu7TZuWRgbAWYTH3WiNvtXJr3OYivR4Tx29pnV0JQkYJUZB7bhBGOdWwdc4663NPZBvKTatXLr2xLXA1yItGO3PJ6e1a5xbhB8pbjqu27aW8GRgPJZR8JBgNIzAzXr+GvGGn1epS5fS3aK84aN5wdzTAJOZH+PvWT4o02mvcNuvYuAKNQ7CfSr/ESUWMmIXtCmOdZ6rkfEAxYXJmeZAiGyYzgn3FY2ntn1EGCon84mfmQPrXo8X3iAU2hgGEZXP3kzjl+tJ/QKNpYttZZyQDuZTtYf6lLDNbZbN4F0tvVzo7yEJccP5gAD22C7QdxywkgAHGZrxfFnhx9LeuW2n0sQrEQHUGN4z1q7hSXFum4jbICsShlbYPQqTJUkAfUdK6VxDjS6zhLveth7oXy1fbnzi2YxIEZPTnWbuq4Y9qK2bwjZS5Nt7TXbZA80JJe36wA46xnpNeVY04NzYerbR0H+RPYVsHE/D7afUt/RXdxtgNuQ5U7ZYgnpIaO9Uedd8LXGuMtsjaAWliBtQGAX7GcEd5rXWtwSD3/n0raNZ4guvbQMiqU3zcUeq47MrbnPIkFZivItMhuhrgLKWlgMEg8x7VR53lzz5fz8qDKAK3fxpwEWkV0Rst8fJHtsivb9PNWAYA9K02OZjHbtUnUrFIj3rLs2ewJxJgTA6n5e9Y7J2rJ0V0Krw7KxAAC8mBPrDGeXLGZo1D3AJjIx15zGR+M0z3BjpH5nue2P0qt3JJJyTkk5M/OkNVV1y+u4bVIWAGG6d0RJkj0zExmKxzUNBjWQKlSalQVjOKYKNszmfpHzpVqVUQUaBFQVFMK9Dh2qKMGUkEEEEcwQZBrz6sRqD6X8K+OLersIHUs5UrcQCfUIGDyAIO7PQHtWl/aDwhbzefbJFs7bKMZf1KSfUcwpBInptrn/AIR8QvpLy3FyMB06Mvb59jXctPxmzq7StZuC3vtepQJ2l3VXcR95RjlielEfP3HeHtauNbYoSpiUO5ZHY1i2uIOALbEvbBnYTgc5CkgxzrsnjjwZa/orV1iFuopUsoJFyEZl3HoSRj5xXGNbpihzWtRkPatkk2nMc9rwD3gRM9q9bQ+I7lpRaurvtZOwsV54wy9PblWsA1YzkwCSfzpKY3jiviTS3dHYsW7ZW7aSDduZJgksEjAmeonpXjvfttaVSxJQFU6kKTuBY8goJiPc1rQBHuKss3SPrVHUk4BqLmnt67aqI+xXKgAralSbg7jBnsPrVnEdZbt23treVrdu1qY3QFvnzIi2wz5xG07/AJAc607h3jjV2l227xEW/LEgHakbQADgQOVYt7UodMArSfMuSrH1R5dsA/Uzgdh2qYMK0pJBiSDW5ppS14Xv/UUgPcTCDdtAO6OQ6Ej6VpvDdSYdQQu5CpJ7c4+pArceF8Vt22R7cbRbKOGwATloiQuTg1Ubhxrhlv8A/medtFpmKqbagbJyyEqeTqDG4ZzmuT8X0Rt3ApTYdqmP9Uid3tM8vau6+Or/AJ2kQqo2XHtgq4gofUfMEfCCJkn964v4w13maj0srIirbQgEelBjnnJkz71nytdC8N8TTV8MOl1B3Msrb2gG5tABA/xkKPoK5VxjhjWrr2zzUkfXtWzfZpxxdNqw7AepWQFuQLcjHWvN8S8TFy/euRu3OQTEQRgADoMVrEao/wCdC1zFPf5zQtDrUWLZqMfagAT+tDpRoJoGiWpSKlEmpQqVkLNSlJqTVQ00aUU1FEU6Y7fI0gog0gsRq3HwF4pbRXg8Aq2HEZjup/brWlLWRbeOtVH1notXZ11lSIa20H5wQRj8flFcm+1HwWVZr6WggLclMoRGTtiVPX6mtY8D+NruifB3WifUn/6Xs3613KxxbTcQ0xKvuDc9uHU+45giaZ3iV8r6jTlWIgj59D71St2K6L498JGzcLWyzoVBBIk9ZUkdcde9c+1Fr2q2GqzdqWyaAHSrKKDDsIocs04ogUMIcmavV9vWk2igttZzy6xzj2qpj3E8VX/L8pnZlHQsxHT39q8riGuNwzAEACAMQOvz96pa0JxMdP8Auh5NMMKl4g9cVdd1U5kmeef5mqmtjEE8sz39o6cqW4hHahisrPWr1GKrsmrBUigaWi7E86WlVKcNM+kZAAicRGR74P4mliimJMwR+c4qCs1KlSoENSoalAaaaSiTRDCmFItGqGomkFMDSCy3citp8G+IW019H3NskC4oPxIcHHIkDI+VakastXYoPq9rGn1NhHXbctuAQRHaTy5ftXOfF32eWid9hXEn1IoDASDnMYESfniuccD8S6jTEeVdZQDu2SSh7yswZrpHDfH6agj0vb1GyAAZst1yOY5YPSa3+M44zxDTBLjLnDEZEHBiSOnyqmt3+0bgpQW9XvVkvlgFCbCpXnuAwTO7I7e4rSByrDQxRBpZomqGJqE0u6hTVWGoDVatFHdWpUWTSmhuoE0tEFQ1FNPtME4Pefegqqbj9KBNNtwDGD/45VhSVKgNMrd+gPQdvfnQJNGjFSrg/9k=",
			"Wheatley" : "https://i.ytimg.com/vi/ugGY164IK-Y/maxresdefault.jpg",
			"Master Chief" : "https://images.app.goo.gl/kPQGS3KYb1yHCzv47",
			"Space Anomaly" : "https://images.app.goo.gl/YGtn2aMciBv7HaTq7",
			"Higuain's penalty" : "https://www.rosarioplus.com/__export/1436281358095/sites/rosarioplus/img/noticias/2015/07/07/penal_higuain.jpg",
			"Poochy on his way to his home planet" : "https://i.ytimg.com/vi/4tvAjX5ACPo/hqdefault.jpg",
			"Garbage Ball" : "https://4.bp.blogspot.com/-SKBp_a6R_fw/TpsHfmij3CI/AAAAAAAAABU/1wqvwf-K9qM/s1600/GarbageBall.jpg",
			"Phantom Zone" : "https://libreriaactioncomics.files.wordpress.com/2014/05/phantom-zone.jpg?w=650",
			"Asteroid from Armageddon" : "https://cdn.mos.cms.futurecdn.net/r4FcQBz64VQo5D8f9FUf6C-1200-80.jpg",
			"Wall-e and EVE" : "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d125df43-37f9-4450-a601-50d3aa7fa501/ddqffyb-567f58f2-115e-4bc0-8fc5-b4cdfb0c0dde.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvZDEyNWRmNDMtMzdmOS00NDUwLWE2MDEtNTBkM2FhN2ZhNTAxXC9kZHFmZnliLTU2N2Y1OGYyLTExNWUtNGJjMC04ZmM1LWI0Y2RmYjBjMGRkZS5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.C2IuVN8FS3FjVTg7ShqFaPTeqM2CSBoPtam8JkpkYvY",
			"Meateroid" : "https://vignette.wikia.nocookie.net/cloudywithachanceofmeatballs/images/4/4d/Meateroid.png/revision/latest/scale-to-width-down/340?cb=20130406212617",
			}
		self.bad_text = "You crash into an object and lose 10 hull."
		self.good_text = "You set up a mining station and gain 10 hull."
		if name:
			self.set_url()

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
		self.urls = {
			"Knowhere" : "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/e/e3/Knowhere_-_Guardianes_de_la_Galaxia.png/revision/latest?cb=20151219160642&path-prefix=es",
			"Death Star" : "https://i.pinimg.com/originals/b2/f5/71/b2f571795a78175829228a409d9fa4f1.jpg",
			"International Space Station" : "https://upload.wikimedia.org/wikipedia/commons/0/04/International_Space_Station_after_undocking_of_STS-132.jpg",
			"Babylon 5" : "data:image/jpeg;base64,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",
			"The Citadel" : "https://i.pinimg.com/originals/1b/b3/54/1bb35439f2e70d1ce73fccfc6b44ae29.jpg",#la de mass effect
			"The Bunker" : "https://vignette.wikia.nocookie.net/nier/images/5/5e/Arte_conceptual_del_exterior_del_b%C3%BAnker_-_NieR_Automata.jpg/revision/latest?cb=20180722135028&path-prefix=es",#la de Nier
			"Death Egg" : "data:image/jpeg;base64,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",
			"The Halo arrays" : "data:image/jpeg;base64,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",
			"Space colony ARK" : "https://steamuserimages-a.akamaihd.net/ugc/311117801426400066/41F15F108983679CD2D9EBEBCD601940645912CD/?imw=1024&imh=576&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true",
			"ISPV 7": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRv8ug0_09vjw_vS3SMosuPX6GzSNB6zK_aGQ&usqp=CAU",
			"Space Tree Station": "https://vignette.wikia.nocookie.net/theregularshow/images/7/71/S8E03.013_Space_Tree_Station.png/revision/latest?cb=20161003224144",
			"Terra Venture": "https://i.ytimg.com/vi/HjtfksemvEM/hqdefault.jpg",
			"Space Colony Neo Mexico": "https://i.redd.it/rlr07vn0awd31.jpg",
			"Jameson Memorial": "https://vignette.wikia.nocookie.net/elite-dangerous/images/7/79/Jameson_Memorial_Station.jpg/revision/latest?cb=20151125134020",
			"Axis": "https://pm1.narvii.com/5831/76e284f0b4a8fa754d55f35d519444e04564f61f_hq.jpg",
			"Star Forge": "https://i.redd.it/1krrb9r0f3941.jpg",
			"La Vie en Rose": "https://vignette.wikia.nocookie.net/gundam/images/e/e2/Storm_2011-02-27_16-53-49-95.jpg/revision/latest?cb=20110301060509",
			"Hydroponics Station": "https://images.adsttc.com/media/images/514a/18bf/b3fc/4bb2/3d00/0018/large_jpg/mode-lina_hydroponic_pumping_station_sfw_3.jpg?1363810492",
			}
		self.good_text = "You get 50 of your lowest resource."
		if name:
			self.set_url()

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
		self.properties = {
			"Your Mom" : {
				"good" : "Your mom is very kind and loving. All resources maxed up.",
				"bad"  : "The weight of your mom destroys the ship.",
				"url"  : "https://vignette.wikia.nocookie.net/bindingofisaac/images/f/f8/250x250-400px-Mom.png/revision/latest?cb=20120610141058"
				},
			"Cthulhu" : {
				"good" : "Your tininess amuses the cosmic entity. All resources maxed up.",
				"bad"  : "Why is Cthulhu in space? Who cares, he killed you.",
				"url"  : "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e33f34df-2b2a-403e-b893-ac217b0fa237/d91af1p-1b820e44-a25b-49c1-b28a-ea131d0d5f4d.png/v1/fill/w_1024,h_866,q_80,strp/cthulhu_in_space_by_flowerewolf_d91af1p-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3siaGVpZ2h0IjoiPD04NjYiLCJwYXRoIjoiXC9mXC9lMzNmMzRkZi0yYjJhLTQwM2UtYjg5My1hYzIxN2IwZmEyMzdcL2Q5MWFmMXAtMWI4MjBlNDQtYTI1Yi00OWMxLWIyOGEtZWExMzFkMGQ1ZjRkLnBuZyIsIndpZHRoIjoiPD0xMDI0In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.15kmQPwBzug039BR-EphdWaN-vNhn3jAH-XwFw3WIto"
				},
			"Reaper" : {
				"good" : "You get the green ending. All resources maxed up.",#Mass Effect
				"bad"  : "You get the red ending (that means you died).",
				"url"  : "https://wallpapercave.com/wp/XrofXx1.jpg"
				},
			"Marker" : {
				"good" : "You are tasked with taking monolites to planets. All resources maxed up.",#Dead Space
				"bad"  : "What do you and Nicole Brennan have in common? That's right.",
				"url"  : "https://i.pinimg.com/originals/d7/6b/49/d76b494cad72f351a2c3b2c8f035d3db.jpg"
				},
			"Galactus" : {
				"good" : "You are the new herald of Galactus. All resources maxed up.",
				"bad"  : "Galactus accidentally swallows your ship whole. Permanently.",
				"url"  : "https://www.cinemascomics.com/wp-content/uploads/2019/05/galactus-heraldo-vengador.jpg"
				},
			"Space baby" : {
				"good" : "Benevolent Space baby wants to help you evolve. All resources maxed up.",
				"bad"  : "The Space baby is in stage of evolution you cant comprehend. You lose the game",
				"url"  : "data:image/jpeg;base64,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"
				},
			"That dragon from Kill the Moon" : {
				"good" : "Moffat maxes up your resources so that you don't ever talk about this.",
				"bad"  : "Your ship gets destroyed by the moonquakes the dragon causes.",
				"url"  : "https://vignette.wikia.nocookie.net/tardis/images/3/33/The_Moon_Hatches_-_Kill_The_Moon_-_Doctor_Who_-_BBC/revision/latest/scale-to-width-down/360?cb=20150920095900"
				},
			"God" : {
				"good" : "God did things right, you arent sure if he did anything at all. Your resources max out.",
				"bad"  : "God does nothing. You died in space",
				"url"  : "https://i.pinimg.com/originals/f8/e7/57/f8e757a0771ba38cd416acbbf92d870d.png"
				},
			"AntiSpiral" : {
				"good" : "You pierce the heavens with your spirit. Your resources max out.",
				"bad"  : "Your spiral power wasnt enough. You were destroyed to stave off the spiral nemesis.",
				"url"  : "https://vignette.wikia.nocookie.net/especiesaliens/images/8/81/Maxresdefault_%281%29.jpg/revision/latest/scale-to-width-down/340?cb=20170312043829&path-prefix=es"
				},
			"Zucc" : {
				"good" : "You encounter a strange android entity calling itself The Zucc. You sacrifice an asian woman to please him. Your resources max out.",
				"bad"  : "u have been zucced goodbye",
				"url"  : "https://thumbor.forbes.com/thumbor/fit-in/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5c76b7d331358e35dd2773a9%2F0x0.jpg%3Fbackground%3D000000%26cropX1%3D0%26cropX2%3D4401%26cropY1%3D0%26cropY2%3D4401"
				},
			"Page Admin" : {
				"good" : "You run into the admin of this page. Because he is a kind and benevolent admin, he fully resupplies you.",
				"bad"  : "You run into the admin of this page. Unfortunately, you haven't been reacting enough to their posts and so they decide to permaban you... with extreme prejudice.",
				"url"  : "https://stuartreviewsstuff.files.wordpress.com/2015/10/become-internet-forum-moderator.jpeg"
				},
			"Monolith" : {
				"good" : "You encounter an alien monolith. As a reward for making it out here, the aliens grant you supreme knowledge to transcend your physical humanity, and even give you a full resupply as a bonus.",
				"bad"  : "You encounter an alien monolith. Unfortunately, the aliens take one look at your primitive ship and de-evolve the crew back into apes. Game over.",
				"url"  : "https://cinemalogue.com/wp-content/uploads/2018/04/2010_screenshot08.jpg"
				},
			"Flying Spaghetti Monster" : {
				"good" : "You run into the Flying Spaghetti Monster. Seeing that your crew are dedicated believers, it gives you a full resupply.",
				"bad"  : "You run into the Flying Spaghetti Monster. Unfortunately, nobody on your crew is a believer, and so as a divine punishment, it sends you to the infinite spaghetti dimension, where you are doomed to roam for all eternity. At least you'll never run out of food.",
				"url"  : "https://cdn.theatlantic.com/thumbor/mpbEjpIUJJ-DLLUkOxgZH2URkYA=/667x0:2000x1333/500x500/media/img/2016/09/DIS_Gilsinan_BigInEurope/original.jpg"
				},
			"Alien X" : {
				"good" : "Alien X warps reality to max out your resources.",
				"bad"  : "Alien X obliterates you.",
				"url"  : "https://i.redd.it/l3tez0lwpii41.jpg"
				},
			"Aurelion Sol" : {
				"good" : "The Star Forger is amused with your puny ship. Your resources are maxed.",
				"bad"  : "The Star Forger sees your small existence, and promptly sends a beam of light to end you. ",
				"url"  : "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/AurelionSol_0.jpg"
				},
			"Moon Lord" : {
				"good" : "Moon Lord gifts you some luminite to max out your resources.",
				"bad"  : "Your ship is struck by Moon Lord's Phantasmal Laser. You die",
				"url"  : "https://static.wikia.nocookie.net/terraria_gamepedia/images/7/7f/Moon_Lord.png/revision/latest/scale-to-width-down/1200?cb=20200805023431"
				},
			"Silver surfer" : {
				"good" : "Silver surfer maxes out your resources to help you defeat Galactus.",
				"bad"  : "Galactus was gonna kill you anyway so Silver surfer does it quicker.",
				"url"  : "https://dam.smashmexico.com.mx/wp-content/uploads/2018/03/personajes-marvel-quien-es-silver-surfer.jpg"
				},
			"GOLB" : {
				"good" : "The entity of chaos watches you fly by and maxes out your resources",
				"bad"  : "GOLB is a mysterious entity who embodies chaos. You die",
				"url"  : "data:image/jpeg;base64,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"
				},
			"Dr. Manhattan " : {
				"good" : "You find Dr. Manhattan, he discusses the potential of human life. He maxes out your resources",
				"bad"  : "You find Dr. Manhattan, he's in the middle of a depressing monologue about the meaning of time. You die",
				"url"  : "https://cdn.vox-cdn.com/thumbor/Bi_V7O6hiQjw8l6bUGGjyLDIZI8=/0x0:2040x1360/920x613/filters:focal(913x655:1239x981):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/65852315/IMG_6C0791D334EA_1.0.jpeg"
				},
			"The Beast with a Billion Backs" : {
				"good" : "The Beast repents for its foul actions and leaves you in peace. Your stats are maxed out.",
				"bad"  : "The Beast rapes you with its enormous tentacles. A moment of bliss is followed by your painful death.",
				"url"  : "https://m.media-amazon.com/images/M/MV5BMjFhODZhYzQtZjgxYS00YjhjLWFkZmEtOTBkYjVkZTY1YWMxXkEyXkFqcGdeQXVyNjY1OTEzMzc@._V1_.jpg"
				},
			"02" : {
				"good" : "You win Kirby. Your stats are maxed out.",
				"bad"  : "You are not Kirby. It kills you.",
				"url"  : "https://art.ngfiles.com/images/545000/545059_kaitogfx_02-kirby-64-the-crystal-shards-art-by-kaito.jpg?f1504570808"
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
		self.urls = {
			"Sagittarius A*":"https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Sagittarius_A%2A.jpg/250px-Sagittarius_A%2A.jpg",
			"Messier 87" : "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Black_hole_-_Messier_87.jpg/330px-Black_hole_-_Messier_87.jpg",
			"Gargantua" : "https://vignette.wikia.nocookie.net/interstellarfilm/images/9/9b/Black_hole.png/revision/latest?cb=20150322005003",
			"Black Hole Sun" : "https://1.bp.blogspot.com/-eunofnAVLLI/XS5-WEONahI/AAAAAAAAaPk/GG_Evshc0rw3BIRLVMgT47K6ghZKY8DbwCLcBGAs/s280/SOUNDGARDEN%2B-%2BBLACK%2BHOLE%2BSUN.jpg",
			"Supermassive Black Hole" : "http://4.bp.blogspot.com/_KtOsypHldng/TToIzNK7mxI/AAAAAAAAADE/sDXBjghrQ48/s1600/Supermassive+Black+Hole+7.jpg",
			"Hugh Janus" : "https://mk0astronomynow9oh6g.kinstacdn.com/wp-content/uploads/2016/08/Interstellar_black_hole_960x500.jpg",
			"Dark Hole" : "https://vignette.wikia.nocookie.net/yugioh/images/0/0c/DarkHole-OP12-EN-C-UE.png/revision/latest/scale-to-width-down/340?cb=20191207180304",
			"Your mom's ass" : "data:image/jpeg;base64,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",
		}
		self.bad_text = "To escape the gravitational pull you use 10 extra fuel"
		if name:
			self.set_url()

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
		self.properties = {
			"Planet Express" : {
				"url"  : "https://www.uokpl.rs/fpng/f/11-119481_planet-express-ship.png",
				"fuel" : 100,
				"provisions"  : 100,
				"hull"  : 100,
				},
			"Rick's ship" : {
				"url"  : "https://i.pinimg.com/originals/7f/57/b5/7f57b556e5841793707379270f195106.png",
				"fuel" : 110,
				"provisions"  : 110,
				"hull"  : 80,
				},
			"X-Wing" : {
				"url"  : "http://www.pngmart.com/files/12/X-Wing-Starfighter-PNG-File.png",
				"fuel" : 130,
				"provisions"  : 100,
				"hull"  : 70,
				},
			"Gradius" : {
				"url"  : "https://pbs.twimg.com/profile_images/1531717667/gradius_1_vic_viper_sprite_by_tuleyiscool-d2ybpkw.png",
				"fuel" : 100,
				"provisions"  : 90,
				"hull"  : 110,
				},
			"Great Fox" : {
				"url"  : "https://vignette.wikia.nocookie.net/starfox/images/6/63/Sector_Z_Smash.jpg/revision/latest?cb=20100615065009",
				"fuel" : 60,
				"provisions"  : 120,
				"hull"  : 120,
				},
			"Samus' Ship" : {
				"url"  : "https://i.imgur.com/dUoLcIs.png",
				"fuel" : 90,
				"provisions"  : 140,
				"hull"  : 70,
				},
			"Naboo Royal Starship" : {
				"url"  : "https://vignette.wikia.nocookie.net/starwars/images/9/9a/Naboo_Royal_Starship_SWE.png/revision/latest?cb=20161019070103",
				"fuel" : 140,
				"provisions"  : 80,
				"hull"  : 80,
				},
			"Capsule Corp" : {
				"url"  : "https://t6.rbxcdn.com/4dee0f4eb69d7e1daf879b6de7d691f7",
				"fuel" : 100,
				"provisions"  : 110,
				"hull"  : 90,
				},
			"Dark Star" : {
				"url"  : "https://i.pinimg.com/originals/d8/ab/0e/d8ab0e6b5f7f7e45bd71d9bcded176df.jpg",
				"fuel" : 110,
				"provisions"  : 90,
				"hull"  : 100,
				},
		}
		if name:
			self.get_properties()

	def get_properties(self):
		self.url = self.properties[self.name]["url"]
		self.fuel = self.properties[self.name]["fuel"]
		self.provisions = self.properties[self.name]["provisions"]
		self.hull = self.properties[self.name]["hull"]



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