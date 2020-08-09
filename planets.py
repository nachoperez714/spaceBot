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
		return spaceship, self.pretext+self.text

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
		}
		if name:
			self.set_url()

	def good_action(self,spaceship):
		spaceship.isHome = True 
		return spaceship

class Planet(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.4
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
				"good" : "Thanos farm. You get you 10 provisions",
				"bad"  : "Thanos farm. You lose 10 provisions",
				"url"  : "https://mcucosmic.com/wp-content/uploads/2018/07/0408_titan_ext_titan_50s0z.jpg"
				},
			"Krypton":{
				"good" : "Marlon Brando teaches you good morals. You get you 10 provisions",
				"bad"  : "Just as you are arriving you see a baby fly by and the planet explodes. You lose 10 provisions",
				"url"  : "https://upload.wikimedia.org/wikipedia/en/0/0a/Krypton_%28DC_Comics_planet_-_circa_2018%29.jpg"
				},
			"Arrakis":{
				"good" : "You become a Messiah-like figure and lead the sand people on a Jihad. You get 10 Spice",
				"bad"  : "JYou barely escape the jaws of a sandworm. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/dune/images/a/af/Arrakis_planet.jpg/revision/latest/scale-to-width-down/340?cb=20190804030356"
				},
			"Fezzan":{
				"good" : "You entered mutually benefitial business agreements. You got 10 provisions.",
				"bad"  : "You violated the NAP, Fezzan funds terrorists against you. You lose 10 provisions",
				"url"  : "https://gineipaedia.com/w/images/thumb/d/db/Phezzan.jpg/300px-Phezzan.jpg"
				},
			"Mars Colony":{
				"good" : "You restore Mars' atmosphere and make up with a hot chick. You get 10 provisions",
				"bad"  : "You may or may not be a secret double/triple agent whose memory was wiped intentionally or unintentionally once or twice. In the confusion you lose 10 provisions",
				"url"  : "https://3.bp.blogspot.com/-ulLqOBJWHWI/VgGE5XVBP2I/AAAAAAAABOk/HKJiC9PewJs/s2048/01%2BAstronauts%2Bon%2BMars%2BTotal%2BRecall%2B1990%2Bmovie%2Bimage.jpg"
				},
			"Namek":{
				"good" : "You achieve SUPERSAYIAN. You get 10 provisions",
				"bad"  : "You arrive just as a midget and a monkey destroy the planet. You lose 10 provisions",
				"url"  : "https://vignette.wikia.nocookie.net/dragonball/images/7/71/Namek_U7.png/revision/latest/top-crop/width/360/height/450?cb=20171203031332&path-prefix=es"
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
			"Mass Relay" : "https://i.ytimg.com/vi/BDq4a6PqAvM/maxresdefault.jpg",
			"Infinite improbability Drive" : "https://i.redd.it/g8ofhhot01qz.jpg",
			"Warp Station" : "https://vignette.wikia.nocookie.net/pulsar-game/images/2/24/Long_range_warp_station.png/revision/latest/scale-to-width-down/340?cb=20190626124313",
			"Portal" : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT-HfXb1DmwshWvAErqfe4mxV7GAZtPQ0wpZw&usqp=CAU",
			"Bifrost" : "https://i.ytimg.com/vi/hzqWcXA_Xrk/maxresdefault.jpg",
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
		self.pretext = "You find yourself in the midst of {}".format(self.name)
		self.urls = {
			"Solar system asteroid belt" : "https://i.ytimg.com/vi/cT3K1INjQJ0/maxresdefault.jpg",
			"Kuiper belt" : "https://image.pbs.org/poster_images/assets/npls12_vid_kuiperbelt_thumb.jpg",
			"Asteroid belt outside Hoth" : "https://vignette.wikia.nocookie.net/starwars/images/1/1b/Hoth_Asteroid_Belt_TESB.png/revision/latest?cb=20161010024439",
			"Asteroid belt from Asteroids" : "https://www.researchgate.net/profile/Kc_Collins/publication/262309733/figure/fig2/AS:694796872081408@1542663891658/Original-vector-based-Asteroids-game-Atari-1979-showing-ship-in-centre-and-floating.ppm",
			"Halley's Comet" : "https://specials-images.forbesimg.com/imageserve/543871022/960x0.jpg?cropX1=0&cropX2=3072&cropY1=305&cropY2=1745",
			"Space trash" : "data:image/jpeg;base64,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"
			}
		self.bad_text = "You crash into an asteroid and lose 10 hull."
		self.good_text = "You mine an asteroid and gain 10 hull."
		if name:
			self.set_url()

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
		self.icon = "Resources/Spaceport_icon.png"
		self.pretext = "You dock your ship at {}".format(self.text)
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
			}
		self.good_text = "Your fuel tank is filled."
		if name:
			self.set_url()

	def good_action(self,spaceship):
		spaceship.modify_fuel(100)
		return spaceship
	
class Being(Event):
	def __init__(self,name=""):
		super().__init__(name)
		self.bad_chance = 0.5
		self.type = "Being"
		self.icon = "Resources/Being_icon.png"
		self.pretext = "You find a cosmic entity: {}.".format(self.name)
		self.properties = {
			"Your Mom" : {
				"good" : "Your mom is ver kind and loving. All resources maxed up.",
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
				}
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
		self.pretext = "Oh no! It's the black hole {}.".format(self.name)
		self.urls = {
			"Sagittarius A*":"https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Sagittarius_A%2A.jpg/250px-Sagittarius_A%2A.jpg",
			"Messier 87" : "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Black_hole_-_Messier_87.jpg/330px-Black_hole_-_Messier_87.jpg",
			"Gargantua" : "https://vignette.wikia.nocookie.net/interstellarfilm/images/9/9b/Black_hole.png/revision/latest?cb=20150322005003",
		}
		self.bad_text = "To escape the gravitational pull you use 10 extra fuel"
		if name:
			self.set_url()

	def bad_action(self,spaceship):
		spaceship.modify_fuel(-10)
		return spaceship

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