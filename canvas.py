
from PIL import Image

#All positions refer to upper left corner
canvas_size = (1800,1800)
resource_icon_size = (200,200)
fuel_position = (0,400)
fuel_text_position = (fuel_position[0]+resource_icon_size[0],fuel_position[1])
resource_text_font = 140
provisions_position = (0,600)
provisions_text_position = (provisions_position[0]+resource_icon_size[0],provisions_position[1])
hull_position = (0,800)
hull_text_position = (hull_position[0]+resource_icon_size[0],hull_position[1])
grid_size = (1200,800)
grid_position = (0,1000)
grid_len = (10,7)
square_size = (grid_size[0]//grid_len[0],grid_size[1]//grid_len[1])
arrow_size = (150,150)
arrow_up_position = (1425,1000)
arrow_left_position = (1200,1325)
arrow_down_position = (1425,1650)
arrow_right_position = (1650,1325)
reaction_size = (150,150)
wow_position = (1500,1325)
like_position = (1425,1150)
angry_position = (1350,1325)
sad_position = (1425,1500)
image_size = (1000,1000)
image_position = (800,0)
cross_font = 140
cross_up_position = (1455,1000)
cross_left_position = (1230,1315)
cross_down_position = (1455,1650)
cross_right_position = (1680,1315)
big_text_position = (0,0)
small_text_position = (0,200)
end_text_position = (200,800)

def greensquare(img_path):
	img = Image.open(img_path)
	size = img.size
	back = Image.open("Resources/greenscreen.png").convert("RGBA").resize((int(18/16*size[0]),int(18/16*size[1])))
	back.paste(img,(int(1/16*size[0]),int(1/16*size[1])))
	back.save(img_path+'.png')
	return img_path+'.png'
