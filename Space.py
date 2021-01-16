import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#import facebook
from pathlib import Path
import os
import urllib.request
import textwrap
import random
#import time
#import skimage.measure as skm
#import matplotlib.pyplot as plt
import planets
import canvas as cv

class Board:
	def __init__(self):
		self.lenx = planets.boardlenx
		self.leny = planets.boardleny
		self.goalLoc = 0
		self.startLoc = 0
		self.events = []
		self.eventlist = []
		self.area = self.lenx*self.leny-2
		self.goal = ""
		self.start = ""
		self.set_start()
		self.set_goal()
		self.generate_events()
		self.img_path = 'background.png'

	def set_start(self):
		xs = np.random.randint(0,self.lenx)
		ys = np.random.randint(0,self.leny)
		self.startLoc = [xs,ys]
		#TODO player ship here
		#self.goal = np.random.choice([*planets.Goal().urls])
	
	def set_goal(self):
		xgoal = self.startLoc[0]
		ygoal = self.startLoc[1]
		while abs(xgoal-self.startLoc[0])+abs(ygoal-self.startLoc[1])<3 :
			xgoal = np.random.randint(0,self.lenx)
			ygoal = np.random.randint(0,self.leny)
		self.goalLoc = [xgoal,ygoal]
		print("startLoc:",self.startLoc[0],",",self.startLoc[1])
		print("goalLoc:",xgoal,",",ygoal)
		self.goal = np.random.choice([*planets.Goal().urls])

	def generate_eventlist(self):
		size = self.lenx*self.leny-2
		beingNum = min(len([*planets.Being().properties]),np.random.poisson(size/30)+1)
		size-=beingNum
		holeNum = min(len([*planets.BlackHole().urls]),np.random.poisson(size/25)+1)
		size-=holeNum
		stationNum = min(len([*planets.Spaceport().urls]),np.random.poisson(size/12)+1)
		size-=stationNum
		portalNum = min(len([*planets.Portal().urls]),np.random.poisson(size/11)+1)
		size-=portalNum
		rockNum = min(len([*planets.Asteroid().urls]),np.random.poisson(size/8)+1)
		size-=rockNum
		planNum = size//2
		shipNum = size-planNum
		self.eventlist+=random.sample([*planets.Planet().properties],planNum)
		self.eventlist+=random.sample([*planets.Ship().properties],shipNum)
		self.eventlist+=random.sample([*planets.Asteroid().urls],rockNum)
		self.eventlist+=random.sample([*planets.Spaceport().urls],stationNum)
		self.eventlist+=random.sample([*planets.Portal().urls],portalNum)
		self.eventlist+=random.sample([*planets.BlackHole().urls],holeNum)
		self.eventlist+=random.sample([*planets.Being().properties],beingNum)
		

	def generate_events(self):
		#TODO: cambiar probabilidad de cada tipo de evento
		#Algoritmo de distribucion copado
		self.generate_eventlist()
		indexes = list(range(self.area))
		np.random.shuffle(indexes)
		#print(indexes)
		offset = 1
		for i in range(self.lenx):
			self.events.append([])
			for j in range(self.leny):
				self.events[i].append([])
				if i==self.startLoc[0] and j ==self.startLoc[1]:
					self.events[i][j] = "Start"
				elif i==self.goalLoc[0] and j==self.goalLoc[1]:
					self.events[i][j] = self.goal
					offset = 2
				else:
					#print(i,j,i*self.leny+j-offset,indexes[i*self.leny+j-offset],self.eventlist[indexes[i*self.leny+j-offset]])
					self.events[i][j] = self.eventlist[indexes[i*self.leny+j-offset]]

	def get_event_name(self,x,y):
		#print (self)
		return self.events[x][y]

					
class Spaceship:
	def __init__(self,player=""):
		self.x = 0
		self.y = 0
		self.image = ""
		self.player = ""
		self.fuel = 100
		self.provisions = 100
		self.hull = 100
		self.item = ""
		#self.tool = ""
		self.isHome = False
		self.initialize(player)

	def has_item(self):
		return bool(self.item)

	#def get_item(self):
	#	return self.item

	def initialize(self,player):
		if player:
			aux = get_event_from_name(player)
		else:
			aux = get_event_from_name(random.sample([*planets.Player().properties],1)[0])
		print(aux.url)
		self.player = get_image_from_url_player(aux.url)
		self.player = cv.greensquare(self.player)
		self.fuel = aux.fuel
		self.provisions = aux.provisions
		self.hull = aux.hull
		self.item = planets.Consumable("Self Destruct Button")

	def move(self,x,y):
		self.x = x
		self.y = y
		#self.fuel -= 10

	def reach_goal(self):
		self.isHome = True

	def modify_fuel(self,amount):
		self.fuel = min(150,self.fuel+amount)

	def modify_hull(self,amount):
		self.hull = min(150,self.hull+amount)

	def modify_provisions(self,amount):
		self.provisions = min(150,self.provisions+amount)

	def is_dead(self):
		return self.fuel<=0 or self.hull<=0 or self.provisions<=0
		
	def overhaul(self,img_path):
		self.image = img_path


def upload_comment(graph, post_id, message="", img_path=None):
	if img_path:
		post = graph.put_photo(image=open(img_path, 'rb'),
							   album_path='%s/comments' % (post_id),
							   message=message)
	else:
		post = graph.put_object(parent_object=post_id,
								connection_name="comments",
								message=message)
	return post
   
def upload_reply(graph, comment_id, message='',img_path=None):
	upload_comment(graph,comment_id,message,img_path)
 
def upload(message, access_token, img_path=None):
	graph = facebook.GraphAPI(access_token)
	if img_path:
		post = graph.put_photo(image=open(img_path, 'rb'),
							   message=message)
	else:
		post = graph.put_object(parent_object='me',
								connection_name='feed',
								message=message)
	return graph, post['post_id']

def getAccessToken(filename='access_token.txt'):
	return Path(filename).read_text().strip()

def get_reactions(graph,post_id):
	reactions = graph.get_connections(post_id,connection_name='reactions')
	reactions = reactions['data']
	reacts = []
	for reaction in reactions:
		reacts.append(reaction['type'])
	#print (reacts)
	return reacts

def get_input_from_reactions(reacs,spaceship):
	nlike = 0
	nwow = 0
	nsad = 0
	nangry = 0
	for reac in reacs:
		if reac=='LIKE' and spaceship.y!=0:
			nlike+=1
		elif reac=='WOW' and spaceship.x!=planets.boardlenx-1:
			nwow+=1
		elif reac=='SAD' and spaceship.y!=planets.boardleny-1:
			nsad+=1
		elif reac=='ANGRY' and spaceship.x!=0:
			nangry+=1

	nreacts = [nlike,nwow,nsad,nangry]
	nmax = max(nreacts)
	if nmax==0:
		return [0,0]
	movement = [0,0]
	if nlike==nmax:
		movement[1]-=1
	if nwow==nmax:
		movement[0]+=1
	if nsad==nmax:
		movement[1]+=1
	if nangry==nmax:
		movement[0]-=1
	return movement

def get_vote_from_reactions(reacs,ship_list):
	nreacs = [0,0,0,0,0,0]
	dic = {"LIKE":0,"WOW":1,"SAD":2,"ANGRY":3}
	for reac in reacs:
		nreacs[dic[reac]]+=1
	return ship_list[int(min(np.argmax(nreacs),len(ship_list)))]

def get_event_from_name(name):
	clas = [planets.Planet,
		planets.Ship,
		planets.Spaceport,
		planets.BlackHole,
		planets.Being,
		planets.Asteroid,
		planets.Portal,
		planets.Start,
		planets.Goal,
		planets.Player
		]
	for ic, cla in enumerate(clas):
		if name in list(cla().properties.keys()) or name in list(cla().urls.keys()):
			return cla(name)


def gen_initial_image(spaceship,board):
	img = Image.new("RGB",cv.canvas_size)
	fuel = Image.open("Resources/naftabien.png").convert("RGBA").resize(cv.resource_icon_size)#transparent
	img.paste(fuel,cv.fuel_position,fuel)
	del fuel
	provisions = Image.open("Resources/sanguche.png").convert("RGBA").resize(cv.resource_icon_size)#transparent
	img.paste(provisions,cv.provisions_position,provisions)
	del provisions
	hull = Image.open("Resources/hull.png").convert("RGBA").resize(cv.resource_icon_size)#transparent
	img.paste(hull,cv.hull_position,hull)
	del hull
	background = Image.open("Resources/Background.jpg").convert("RGBA").resize(cv.grid_size)
	img.paste(background,cv.grid_position)
	del background
	arrow_right = Image.open("Resources/arrow_bien.png").convert("RGBA").resize(cv.arrow_size)
	arrow_up = arrow_right.rotate(90)
	arrow_left = arrow_up.rotate(90)
	arrow_down = arrow_left.rotate(90)
	reacs = Image.open("Resources/reactions.png").convert("RGBA")
	wow = reacs.crop((1011,503,1446,937)).resize(cv.reaction_size)
	like = reacs.crop((1011,0,1446,440)).resize(cv.reaction_size)
	angery = reacs.crop((504,0,939,440)).resize(cv.reaction_size)
	sad = reacs.crop((504,503,939,937)).resize(cv.reaction_size)
	love = reacs.crop((0,503,434,937)).resize(cv.reaction_size)
	del reacs
	img.paste(arrow_right,(cv.arrow_right_position),arrow_right)
	img.paste(arrow_up,(cv.arrow_up_position),arrow_up)
	img.paste(arrow_left,(cv.arrow_left_position),arrow_left)
	img.paste(arrow_down,(cv.arrow_down_position),arrow_down)
	img.paste(wow,cv.wow_position,wow)
	img.paste(like,cv.like_position,like)
	img.paste(angery,cv.angry_position,angery)
	img.paste(sad,cv.sad_position,sad)
	img.paste(love,cv.love_position,love)
	del arrow_up, arrow_right, arrow_left, arrow_down
	del wow, like, angery, sad, love
	spaceship.x = board.startLoc[0]
	spaceship.y = board.startLoc[1]
	img = add_icon(img,"Resources/Start_icon.png",spaceship.x,spaceship.y)
	img.save("Reference_image.png")

	start = Image.open("Resources/Start.png").convert("RGBA").resize(cv.image_size)
	img = add_event_image(img,start)
	del start
	img = add_spaceship(img,spaceship)
	img = add_numbers(img,spaceship)
	draw = ImageDraw.Draw(img)
	draw.text(cv.big_text_position,"Start",font=get_font(get_fontsize("Start",draw)))
	#draw.text(cv.use_item_position,"Use\nitem",font=get_font(50))
	#draw.text(cv.tool_text_position,"Tool: {}".format(spaceship.tool.name),font=get_font(cv.item_big_text_size))
	#draw.text(cv.tool_desc_position,"{}".format(spaceship.tool.description),font=get_font(cv.item_small_text_size))
	#draw.text(cv.item_text_position,"Item: {}".format(spaceship.item.name),font=get_font(cv.item_big_text_size))
	#draw.text(cv.item_desc_position,"{}".format(spaceship.item.description),font=get_font(cv.item_small_text_size))
	draw.text(cv.small_text_position,'Your journey begins!,travel space to find\n {}.\nUse reactions to move the ship'.format(board.goal),font=get_font(40))
	add_item_text(img,spaceship)
	img = add_crosses(img,spaceship)
	del draw
	img.save("Post_image.png")

	return "Post_image.png"

def update_image(spaceship,event):
	#TODO: metodo correcto de insertar imagen
	#print (event.text)
	previous = Image.open("Reference_image.png")
	if event.type!="Goal":
		previous = add_icon(previous,event.icon,spaceship.x,spaceship.y)
		previous.save("Reference_image.png")
	try:
		img_path = get_image_from_url(event.url)
	except:
		img_path = "Resources/failsafe.jpeg"
	img = Image.open(img_path)
	lenx = img.size[0]
	leny = img.size[1]
	if lenx > leny:
		img = img.resize((1000,1000*leny//lenx))
	elif leny < lenx:
		img = img.resize((1000*lenx//leny),1000)
	else:
		img = img.resize(cv.image_size)
	previous = add_event_image(previous,img)
	previous = add_spaceship(previous,spaceship)
	previous = add_numbers(previous,spaceship)
	previous = add_crosses(previous,spaceship,event.type=="Portal")
	previous = add_text(previous,event)
	previous = add_item_text(previous,spaceship)
	previous.save("Post_image.png")
	return "Post_image.png"

def gen_goal_image():
	image = Image.open("Post_image.png")
	draw = ImageDraw.Draw(image)
	draw.text(cv.end_text_position,"YOU WON",font=get_font(300),fill="green")
	image.save("Victory_image.png")
	return "Death_image.png"

def gen_gameover_image(board):
	image = Image.open("Post_image.png")
	image = add_icon(image,"Resources/Goal_icon.png",board.goalLoc[0],board.goalLoc[1])
	draw = ImageDraw.Draw(image)
	draw.text(cv.end_text_position,"YOU DIED",font=get_font(300),fill="red")
	image.save("Death_image.png")
	return "Death_image.png"

def add_text(img,event):
	draw = ImageDraw.Draw(img)
	draw.text((0,0),event.name,font=get_font(get_fontsize(event.name,draw)))
	size,lines = find_font(event.text,draw)
	#font1 = get_fontsize(event.text,draw)
	#font2 = get_fontsize(textwrap.fill(event.text,len(event.text)//2+1),draw)
	#font3 = get_fontsize(textwrap.fill(event.text,len(event.text)//3+2),draw)
	#if font1>=font2 and font1>=font3:
	#	draw.text((0,200),event.text,font=get_font(font1))
	#elif font2>=font3:
	#	draw.text((0,200),textwrap.fill(event.text,len(event.text)//2+1),font=get_font(font2))
	#else:
	#	draw.text((0,200),textwrap.fill(event.text,len(event.text)//3+2),font=get_font(font3))
	draw.text((0,200),textwrap.fill(event.text,len(event.text)//lines+lines-1),font=get_font(size))
	return img

def find_font(text,draw,x=800,y=200):
	font1 = get_fontsize(text,draw,x,y)
	font2 = get_fontsize(textwrap.fill(text,len(text)//2+1),draw,x,y)
	font3 = get_fontsize(textwrap.fill(text,len(text)//3+2),draw,x,y)
	if font1>=font2 and font1>=font3:
		return font1, 1
	elif font2>=font3:
		return font2, 2
	else:
		return font3, 3

def add_item_text(img,ship):
	#img.paste(Image.open(ship.tool.icon).convert("RGBA").resize(cv.item_icon_size),cv.tool_icon_position)
	img.paste(Image.open(ship.item.icon).convert("RGBA").resize(cv.item_icon_size),cv.item_icon_position)
	#toolname = "Tool: "+ship.tool.name
	#tooldesc = ship.tool.description
	itemname = "Item: "+ship.item.name
	itemdesc = ship.item.description
	print("itemname ",itemname," itemdesc ",itemdesc)
	draw = ImageDraw.Draw(img)
	#tnFont, tnLines = find_font(toolname,draw,650,150)
	#tdFont, tdLines = find_font(tooldesc,draw,650,125)
	inFont, inLines = find_font(itemname,draw,650,150)
	idFont, idLines = find_font(itemdesc,draw,650,125)
	namefont = inFont#min(tnFont,inFont)
	descfont = idFont#min(idFont,tdFont)
	draw.text(cv.use_item_position,"Use\nitem",font=get_font(80))
	#draw.text(cv.tool_text_position,textwrap.fill(toolname,len(toolname)//tnLines+tnLines-1),font=get_font(namefont))
	#draw.text(cv.tool_desc_position,textwrap.fill(tooldesc,len(tooldesc)//tdLines+tdLines-1),font=get_font(descfont))
	draw.text(cv.item_text_position,textwrap.fill(itemname,len(itemname)//inLines+inLines-1),font=get_font(namefont))
	draw.text(cv.item_desc_position,textwrap.fill(itemdesc,len(itemdesc)//idLines+idLines-1),font=get_font(descfont))
	return img

def add_icon(image,icon,x,y):
	ic = Image.open(icon).convert("RGBA").resize(cv.square_size)
	image.paste(ic,(cv.grid_position[0]+cv.square_size[0]*x,cv.grid_position[1]+cv.square_size[1]*y),ic)
	return image

def add_event_image(canvas,image):
	canvas.paste(image,cv.image_position)
	return canvas

def add_spaceship(img,ship):
	print(ship.player)
	print(ship.image)
	spaceshipng = Image.open(ship.player).resize(cv.square_size)
	img.paste(spaceshipng,(cv.grid_position[0]+cv.square_size[0]*ship.x,cv.grid_position[1]+cv.square_size[1]*ship.y))
	return img

def add_numbers(img,ship):
	draw = ImageDraw.Draw(img)
	draw.text(cv.fuel_text_position,str(ship.fuel),font=get_font(cv.resource_text_font),fill=get_fill(ship.fuel))
	draw.text(cv.provisions_text_position,str(ship.provisions),font=get_font(cv.resource_text_font),fill=get_fill(ship.provisions))
	draw.text(cv.hull_text_position,str(ship.hull),font=get_font(cv.resource_text_font),fill=get_fill(ship.hull))
	return img

def get_fill(resource):
	if resource==150:
		return "green"
	if resource<=20 and resource>0:
		return "orange"
	if resource<=0:
		return "red"
	if resource<=40:
		return "yellow"
		return

def add_crosses(img,ship,is_portal=False):
	draw = ImageDraw.Draw(img)
	if ship.x==0 or is_portal:
		draw.text(cv.cross_left_position,"X",font=get_font(140),fill="red")
	if ship.x==planets.boardlenx-1 or is_portal:
		draw.text(cv.cross_right_position,"X",font=get_font(140),fill="red")
	if ship.y==0 or is_portal:
		draw.text(cv.cross_up_position,"X",font=get_font(140),fill="red")
	if ship.y==planets.boardleny-1 or is_portal:
		draw.text(cv.cross_down_position,"X",font=get_font(140),fill="red")
	if not ship.has_item() or is_portal:
		draw.text(cv.cross_item_position,"X",font=get_font(140),fill="red")
	return img

def get_font(size):
	try:#Linux
		font = ImageFont.truetype("Lato-Medium.ttf",size)
	except:#Windows
		font = ImageFont.truetype("arial.ttf",size)
	#mac users BTFO
	return font

def get_fontsize(text,draw,maxlenx = 800, maxleny = 200):
	pw = []
	ph = []
	for i in range(10):
		font = get_font((i+1)*10)
		ps = draw.textsize(text,font)
		pw.append(ps[0])
		ph.append(ps[1])
	#print (pw, ph)
	print ("pw ",pw," ph ",ph)
	return int(min(10*maxlenx//np.mean(np.diff(pw)),10*maxleny//np.mean(np.diff(ph))))

def get_image_from_url(url):
	urllib.request.urlretrieve(url,'event_image')
	return 'event_image'

def get_image_from_url_player(url):
	urllib.request.urlretrieve(url,'player_image')
	return 'player_image'

def vote_ship(direction=""):
	img_path, ship_list = make_vote_image()
	message = "The next voyage will start soon, pick your ship!"
	if not direction:
		gr, p_id = upload(message,getAccessToken(),img_path)
		return gr, p_id, ship_list
	else:
		return 0,0,ship_list

def choose_ship(gr,p_id,ship_list,direction=""):
	if not direction:
		reacts = get_reactions(gr,p_id)
		return get_vote_from_reactions(reacts,ship_list)
	else:
		dic = {"like":0,"wow":1,"sad":2,"angry":3}
		return ship_list[dic[direction]]

def make_vote_image():
	img = Image.new("RGB",(1000,1000))
	ships = random.sample([*planets.Player().properties],4)
	reacs = Image.open("Resources/reactions.png").convert("RGBA")
	wow = reacs.crop((1011,503,1446,937)).resize((150,150))
	like = reacs.crop((1011,0,1446,440)).resize((150,150))
	angery = reacs.crop((504,0,939,440)).resize((150,150))
	sad = reacs.crop((504,503,939,937)).resize((150,150))
	reacs = [like,wow,sad,angery]
	xs = [0,1,0,1]
	ys = [0,0,1,1]
	for i, ship in enumerate(ships):
		shipimg = Image.new("RGB",(495,495))
		myship = get_event_from_name(ship)
		shipicon = Image.open(get_image_from_url_player(myship.url)).convert("RGBA").resize((300,300))
		shipimg.paste(shipicon,(0,190))
		fuel = Image.open("Resources/naftabien.png").convert("RGBA").resize((100,100))
		resources = Image.open("Resources/sanguche.png").convert("RGBA").resize((100,100))
		hull = Image.open("Resources/hull.png").convert("RGBA").resize((100,100))
		shipimg.paste(fuel,(300,190))
		shipimg.paste(resources,(300,290))
		shipimg.paste(hull,(300,390))
		shipimg.paste(reacs[i],(0,0))
		draw = ImageDraw.Draw(shipimg)
		draw.text((400,190),str(myship.fuel),font=get_font(50))
		draw.text((400,290),str(myship.provisions),font=get_font(50))
		draw.text((400,390),str(myship.hull),font=get_font(50))
		font1 = get_fontsize(ship,draw,345,190)
		font2 = get_fontsize(textwrap.fill(ship,len(ship)//2+1),draw,345,190)
		if font1>=font2:
			draw.text((150,0),ship,font=get_font(font1))
		else:
			draw.text((150,0),textwrap.fill(ship,len(ship)//2+1),font=get_font(font2))
		img.paste(shipimg,(xs[i]*505,ys[i]*505))
	draw = ImageDraw.Draw(img)
	draw.line([(500,0),(500,1000)],"white",10)
	draw.line([(0,500),(1000,500)],"white",10)
	img.save("vote_image.png")
	return "vote_image.png", ships
#
#TURN
#
#[0:vote ship,1:first,2:normal turn]
def main(turn=0,direction="",vote=True):

	if direction:
		gr = 0
		p_id = 0

	if turn==0:
		gr, p_id, ship_list = vote_ship(direction)
		np.save('data',[gr,p_id,ship_list])
		return True

	if turn==1:
		#generar el tablero
		board  =Board()
		initial_message = "Welcome traveler, move your ship across space to reach {} or perish in your quest to find it".format(board.goal)
		if vote:
			data = np.load('data.npy',allow_pickle=True)
			gr = data[0]
			p_id = data[1]
			ship_list = data[2]
			ship = choose_ship(gr,p_id,ship_list,direction)
			spaceship = Spaceship(ship)
		else:
			spaceship = Spaceship()#get_random_ship())
		postImage = gen_initial_image(spaceship,board)
		if direction:
			gr = 0
			p_id = 0
		else:
			gr, p_id = upload(initial_message,getAccessToken(),postImage)
		was_portal = False
		np.save('data',[spaceship,gr,p_id,board,was_portal])
		return True
	else:
		data = np.load("data.npy",allow_pickle=True)
		spaceship = data[0]
		previous_gr = data[1]
		previous_id = data[2]
		board = data[3]
		was_portal = data[4]

		if was_portal:
			spaceship.move(np.random.randint(board.lenx),np.random.randint(board.leny))
		else:
			if direction=='item':
				spaceship.item.use(spaceship)
				movement = [0,0]
			elif direction:
				usertest = {
					"up" : [0,-1],
					"left" : [-1,0],
					"right" : [1,0],
					"down" : [0,1]
					}
				movement = usertest[direction]
			else:
				reacts = get_reactions(previous_gr,previous_id)
				movement = get_input_from_reactions(reacts,spaceship)
			spaceship.move(spaceship.x+movement[0],spaceship.y+movement[1])
			#spaceship.move(spaceship.x+1,spaceship.y+0)
			spaceship.modify_fuel(-5)
			spaceship.modify_provisions(-5)

		event = get_event_from_name(board.get_event_name(spaceship.x,spaceship.y))
		spaceship,message = event.action(spaceship)

		if spaceship.isHome:
			message += '\nCongratulations, you have reached your destination, see you in the next voyage.'
			victory_path = update_image(spaceship,event)
			gen_goal_image()
			if direction:
				print (message)
			else:
				#FACEBOOK
				gr, p_id = upload(message,getAccessToken(),"Victory_image.png")
			return False
		if spaceship.is_dead():
			message += '\nYou died before reaching your destination, better luck on the next voyage.'
			game_over_path = update_image(spaceship,event)
			gen_gameover_image(board)
			if direction:
				print(message)
			else:
				#FACEBOOK
				gr, p_id = upload(message,getAccessToken(),"Death_image.png")
			np.save('data',[spaceship,board,event.get_type()=="Portal"])
			return False
		if not event.get_type()=="Portal":
			message+="\n Use the reactions to move the ship."
		img_path = update_image(spaceship,event)
		if direction:
			print(message)
		else:
			#FACEBOOK
			gr, p_id = upload(message,getAccessToken(),img_path)
			upload_comment(gr,p_id,"Beep boop: I'm a Space Bot. Right now the ship has {} fuel, {} provisions and {} hull integrity. For further details on how everything works check the post pinned at the top of the page.".format(spaceship.fuel,spaceship.provisions,spaceship.hull))
			space_comment = "SP"
			As = np.random.randint(1,100)
			for i in range(As):
				space_comment+="A"
			space_comment+="CE"
			upload_comment(gr,p_id,space_comment,"Resources/Space_Core.png")
			upload_comment(gr,p_id,"You can add events in this form: https://docs.google.com/forms/d/e/1FAIpQLSfttY8c1XM-nrJpOw7mYZ0-0ulr9kCDfo-CGD63r6TxYzdoZw/viewform")
			if np.random.rand()<0.01:
                            upload_comment(gr,p_id,"If you are feeling generous you can help to maintain this bot at paypal.me/DelRioFer")
			upload_comment(previous_gr,previous_id,"The ship has moved on, check the latest post")
		np.save('data',[spaceship,gr,p_id,board,event.get_type()=="Portal"])
		return True

def testUrls():
	arrayProperties = []
	arrayUrls = []
	brokenUrls = []
	print("Planets: ",len([*planets.Planet().properties]))
	print("Ships: ",len([*planets.Ship().properties]))
	print("Beings: ",len([*planets.Being().properties]))
	print("Asteroids: ",len([*planets.Asteroid().urls]))
	print("Portals: ",len([*planets.Portal().urls]))
	print("BlackHoles: ",len([*planets.BlackHole().urls]))
	print("Spaceports: ",len([*planets.Spaceport().urls]))
	print("Goals: ",len([*planets.Goal().urls]))
	print("Players: ",len([*planets.Player().properties]))

	arrayProperties+=[*planets.Planet().properties]
	arrayProperties+=[*planets.Player().properties]
	arrayProperties+=[*planets.Ship().properties]
	arrayProperties+=[*planets.Being().properties] 
	arrayUrls+=[*planets.Asteroid().urls]
	arrayUrls+=[*planets.Portal().urls]
	arrayUrls+=[*planets.BlackHole().urls]
	arrayUrls+=[*planets.Goal().urls]
	arrayUrls+=[*planets.Spaceport().urls]
	for name in arrayProperties:
		try:
			aux = get_event_from_name(name)
			print(name)
			urllib.request.urlretrieve(aux.url,'event_image')
		except:
			print(">arreglar esta ^")
			brokenUrls+=name
	for name in arrayUrls:
		try:
			aux = get_event_from_name(name)
			print(name)
			urllib.request.urlretrieve(aux.url,'event_image')
		except:
			print(">arreglar esta ^")
			brokenUrls+=name
	print("Broken urls: ",brokenUrls)

def localtest():
	br = False
	while not br:
		b = input("Press n for a new one; wasd to move, x to use item or q to quit")
		if b=="n":
			main(1,"hola",False)
		elif b=="w":
			main(2,"up")
		elif b=="a":
			main(2,"left")
		elif b=="s":
			main(2,"down")
		elif b=="d":
			main(2,"right")
		elif b=="q":
			br = True
		elif b=='x':
			main(2,"item")
		else:
			print("That's not a valid command, try again")
