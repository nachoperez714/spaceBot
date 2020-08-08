import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import facebook
from pathlib import Path
import os
#import skimage.measure as skm
#import matplotlib.pyplot as plt
import planets

class Board:
	def __init__(self):
		#TODO: chequear que nos parezca bien el tamanio
		#TODO: conseguir initial_image
		self.lenx = 10
		self.leny = 8
		xgoal = np.random.randint(3,lenx)
		ygoal = np.random.randint(3,leny)
		self.goal = [xgoal,ygoal]
		self.events = []
		self.generate_events()
		self.img_path = 'background.png'

	def generate_events():
		#TODO: cambiar probabilidad de cada tipo de evento
		#Algoritmo de distribucion copado
		indexes = np.random.sample(range(0,loquesea),self.lenx*self.leny-2)
		for i in range(lenx):
			self.events.append([])
			for j in range(leny):
				self.events[i].append([])
				if i==0 and j ==0:
					self.events[i][j] = "Start"
				elif i==xgoal and j==ygoal:
					self.events[i][j] = "Goal"
				else:
					self.events[i][j] = planets.events[indexes[i*leny+j]]

	def update_image(x,y,event,self):
		#TODO: metodo correcto de insertar imagen
		img = load(self.img_path)
		img = img.insert(x,y,event.get_image())
		img = img.insert(x,y,las_reactions)
		save(img,self.img_path)
		return self.img_path

	def gen_gameover_image(x,y,event,self):
		#TODO
		return gameover_path

	def get_event_name(x,y,self):
		return self.events[x][y]

					
class Spaceship:
	def __init__(img_path=default,self):
		self.x = 0
		self.y = 0
		self.image = img_path
		self.fuel = 100
		self.provisions = 100
		self.hull = 100
		self.hasWeapons = False

	def move(x,y):
		self.x = x
		self.y = y
		self.fuel -= 10

	def modify_fuel(amount):
        self.fuel += amount

    def modify_hull(amount):
    	self.hull += amount

    def modify_provisions(amount):
    	self.provisions += amount

    def is_dead():
    	return self.fuel<=0 or self.hull<=0 or self.provisions<=0
    	
    def overhaul(img_path):
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
    return reacts

def get_event_from_name(name):
	dic = {
		"Planet" : planets.Planet,
		"Portal" : planets.Ship,
		"Asteroids" : planets.Asteroid,
		"Spaceport" : planets.Spaceport,
		"Being" : planets.Being,
		"BlackHole" : planets.BlackHole
		}
	for tipo in planets.types:
		if name in tipo:
			return dic[tipo](name)

def gen_initial_image(spaceship):
	img = Image.new("RGB",(1800,1800))
	fuel = Image.open("Resources/naftabien.png").convert("RGBA").resize((200,200))#transparent
	img.paste(fuel,(0,400),fuel)
	del fuel
	provisions = Image.open("Resources/sanguche.png").convert("RGBA").resize((200,200))#transparent
	img.paste(provisions,(0,600),provisions)
	del provisions
	hull = Image.open("Resources/hull.png").convert("RGBA").resize((200,200))#transparent
	img.paste(hull,(0,800),hull)
	del hull
	background = Image.open("Resources/Background.jpg")
	img.paste(background,(0,1000))
	del background
	arrow_right = Image.open("Resources/arrow_bien.png").convert("RGBA").resize((150,150))
	arrow_up = arrow_right.rotate(90)
	arrow_left = arrow_up.rotate(90)
	arrow_down = arrow_left.rotate(90)
	reacs = Image.open("Resources/reactions.png").convert("RGBA")
	wow = reacs.crop((1011,503,1446,937)).resize((150,150))
	like = reacs.crop((1011,0,1446,440)).resize((150,150))
	angery = reacs.crop((504,0,939,440)).resize((150,150))
	sad = reacs.crop((504,503,939,937)).resize((150,150))
	del reacs
	img.paste(arrow_right,(1200+450,1000+325),arrow_right)
	img.paste(arrow_up,(1200+225,1000+0),arrow_up)
	img.paste(arrow_left,(1200+0,1000+325),arrow_left)
	img.paste(arrow_down,(1200+225,1000+650),arrow_down)
	img.paste(wow,(1200+300,1000+325),wow)
	img.paste(like,(1200+225,1000+150),like)
	img.paste(angery,(1200+150,1000+325),angery)
	img.paste(sad,(1200+225,1000+500),sad)
	del arrow_up, arrow_right, arrow_left, arrow_down
	del wow, like, angery, sad
	img.save("Reference_image.png")
	draw = ImageDraw.Draw(img)
    draw.text((200,400),str(spaceship.fuel),font=get_font(140))
    draw.text((200,600),str(spaceship.provisions),font=get_font(140))
    draw.text((200,800),str(spaceship.hull),font=get_font(140))
    draw.text((0,0),"Start",font=bigfont)
    draw.text(())

def get_font(size):
	try:#Linux
        font = ImageFont.truetype("Lato-Medium.ttf",size)
    except:#Windows
        font = ImageFont.truetype("arial.ttf",size)
    #mac users BTFO
    return font

def get_fontsize(text,draw,maxlen = 800):
	pw = []
	for i in range(10):
		font = get_font((i+1)*10)
		ps = ImageDraw.ImageDraw.textsize(draw,text,font)
		pw.append(ps[0])
	return 10*maxlen/np.mean(np.diff(pw))



def main(isFirst=False):
	initial_message = "Hola"

	if isFirst:
		#generar el tablero
		spaceship = Spaceship(get_random_ship())
		postImage = gen_initial_image(spaceship)
		gr, p_id = upload(initial_message,getAccessToken(),postImage)
		was_portal = False
		np.save('data',[spaceship,gr,p_id,board,was_portal])
		return True
	else:
		data = np.load("spaceship.npy",allow_pickle=True)
		spaceship = data[0]
		previous_gr = data[1]
		previous_id = data[2]
		board = data[3]
		was_portal = data[4]
		if was_portal:
			pass
		else:
			reacts = get_reactions(previous_gr,previous_id)
			movement = get_movement_from_reactions()
			spaceship.move(spaceship.x+movement[0],spaceship.y+movement[1])
			spaceship.modify_fuel(-10)
		if spaceship.x == board.xgoal and spaceship.y == board.ygoal:
			victory_message = "Congrats..."
			gr, p_id = upload(victory_message,getAccessToken(),img_path)
			return False
		new_event = gen_event_from_name(board.get_event_name(spaceship.x,spaceship.y))
		spaceship,flavor_text = new_event.action(spaceship)
		
		message = gen_message(new_event,flavor_text)
		if spaceship.is_dead():
			death_message = message + "\nYou died..."
			game_over_path = board.gen_gameover_image(x,y,event)
			gr, p_id = upload(death_message,getAccessToken(),game_over_im)
			np.save('data',[spaceship,gr,p_id,board,event.get_type()=="Portal"])
			return False

		img_path = board.update_image(x,y,event)
		gr, p_id = upload(message,getAccessToken(),img_path)
		np.save('data',[spaceship,gr,p_id,board,event.get_type()=="Portal"])
		#TODO: Comments w/current state & SPAAAAAAAAAAAAAACE
		return True
