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


def main(isFirst):
	initial_message = "Hola"

	if isFirst:
		#generar el tablero
		spaceship = Spaceship(get_random_ship())
		postImage = gen_initial_image(spaceship.image)
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
