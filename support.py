import pygame
import math
import random

pygame.init()


#display settings
display_width=800
display_height=600
field_width = 640
field_height = 500
field_coordinates = (80,50)
warrior_radius = 5
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chris-Cross')
clock = pygame.time.Clock()

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (119,136,153)
burlywood =(222,184,135)
whitesmoke = (245,245,245)
azure = (240,255,255)
light_yellow = (255,255,51)


def text_objects(text,font, color):
	text_surface = font.render(text, True, color)
	return text_surface, text_surface.get_rect()


def text_prop(font,size):
	return pygame.font.SysFont(font,size)


def message_display(text, size, x,y , color, font):
	text_font = text_prop(font,size)
	text_surface,text_rect = text_objects(text,text_font,color)
	text_rect.center = (y,x)
	gameDisplay.blit(text_surface,text_rect)


def quit_fun():
	pygame.quit()
	quit()

def background_img(img):
	image = pygame.image.load(img)
	gameDisplay.blit(pygame.transform.scale(image, (800, 600)), (0, 0))


def button(msg, button_x, button_y, button_width, button_height, inactive_color, active_color, textfont, text_size, action):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if button_x+button_width>mouse[0]>button_x and button_y+button_height>mouse[1]>button_y:
		pygame.draw.rect(gameDisplay,active_color,(button_x, button_y, button_width, button_height))
		if click[0]==1 and action!=None:
			action()
	else:
		pygame.draw.rect(gameDisplay,inactive_color,(button_x, button_y, button_width, button_height))

	message_display(msg, text_size,int((button_y+(button_height/2))),int((button_x+(button_width/2))), black, textfont)



def frighter_drawer(x, y, color, radius):
	pygame.draw.circle(gameDisplay, color, (x,y),radius )

def check_warrior_click(a_warriors, b_warriors,mouse):
	for a_warrior in a_warriors:
		if (a_warrior[0]+warrior_radius)>mouse[0]>(a_warrior[0]-warrior_radius) and (a_warrior[1]+warrior_radius)>mouse[1]>(a_warrior[1]-warrior_radius):
			return ('a',a_warrior)
	for b_warrior in b_warriors:
		if (b_warrior[0]+warrior_radius)>mouse[0]>(b_warrior[0]-warrior_radius) and (b_warrior[1]+warrior_radius)>mouse[1]>(b_warrior[1]-warrior_radius):
			return ('b',b_warrior)
	return (False,0)

def empty_rectangle(x,y,z,w,width):
	pygame.draw.line(gameDisplay, black, x,y,width)
	pygame.draw.line(gameDisplay, black, y,z,width)
	pygame.draw.line(gameDisplay, black, z,w,width)
	pygame.draw.line(gameDisplay, black, w,x,width)

def in_field(x,y):
	if x>=field_coordinates[0]+field_width:
		x=field_coordinates[0]+field_width-5
	elif x<field_coordinates[0]:
		x=field_coordinates[0]+5
	if y>=field_coordinates[1]+field_height:
		y = field_coordinates[1]+field_height-5
	elif y<field_coordinates[1]:
		y = field_coordinates[1]+5
	return (x,y)




def click_and_draw(mouse):
	#print('click and draw')
	while True:
		for event in pygame.event.get():
			if event.type==pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					mo = pygame.mouse.get_pos()
					if mouse[0]!=mo[0]:
						distance = random.randrange(50,200)
						#print('mouse',mouse)
						#print('mo',mo)
						Q = ((mo[1]-mouse[1])/(mo[0]-mouse[0]))
						#print(Q)
						#print('distance',distance)
						if mouse[0]<mo[0]:
							x,y = int(mouse[0]+(distance*math.cos(Q))),int(mouse[1]+(distance*math.sin(Q)))
						else:
							x,y=int(mouse[0]-(distance*math.cos(Q))),int(mouse[1]-(distance*math.sin(Q)))
						return in_field(x,y)
					else:
						return (mouse[0]+distance,mouse[1])


def equ_solver(tuple1,tuple2):
    x = (tuple2[1]-tuple1[1])/(tuple1[0]-tuple2[0])
    y = (tuple1[0]*x)+tuple1[1]
    return (x,y)


def satisfy(line_cord1, line_cord2, tuple1, line_cord11, line_cord12):
    #print('line_cord1',line_cord1)
    #print('line_cord2',line_cord2)
    #print('tuple1',tuple1)

    if min(line_cord1[0],line_cord2[0])<=tuple1[0]<=max(line_cord2[0],line_cord1[0]) and min(line_cord1[1],line_cord2[1])<=tuple1[1]<=max(line_cord2[1],line_cord1[1]):
    	if min(line_cord11[0],line_cord12[0])<=tuple1[0]<=max(line_cord12[0],line_cord11[0]) and min(line_cord11[1],line_cord12[1])<=tuple1[1]<=max(line_cord12[1],line_cord11[1]):
        	return True
    else:
        return False


def fight(move,all_moves, warrior, point):

    for w_move in all_moves:
        m1 = (w_move[1][1]-w_move[0][1])/(w_move[1][0]-w_move[0][0])
        m2 = (move[1][1]-move[0][1])/(move[1][0]-move[0][0])
        if m1!=m2:
            #print('Not Equal')
            a1 = m1
            b1 = w_move[0][1]-(w_move[0][0]*m1)

            a2 = m2
            b2 = move[0][1]-(move[0][0]*m2)

            #equ_solver(tuple1,tuple2)
            tuple1 = equ_solver((a1,b1),(a2,b2))
            #print('tuple1',tuple1)

            if satisfy(w_move[0], w_move[1], tuple1,move[0], move[1]):
            	try:
            		i=warrior.index(w_move[1])
            		warrior[i] = w_move[0]
	            	j=all_moves.index(w_move)
	            	all_moves = all_moves[:j]
	            	point+=1
            	except Exception as e:
            		print(e)
            	
            	#all_moves.remove(w_move)
    return (all_moves,point)

