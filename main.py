import pygame
import random
import math
from support import*

pygame.init()



def game_intro_loop():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(azure)
		#background_img('image_4.jpg')
		#game title
		message_display('Chris -', 60, int(display_height*0.1), int(display_width*0.3)+100 , red ,'freesansbold.ttf' )
		message_display('X',  100, int(display_height*0.1), int(display_width*0.3) +200, red, 'freesansbold.ttf')	

		#player1
		message_display('Player 1',40, int(display_height*0.1)+100, int(display_width*0.2) , blue, 'Western.ttf')
		pygame.draw.rect(gameDisplay, grey, (int(display_width*0.1)+40, int(display_height*0.1)+125, 80, 25))
		pygame.draw.rect(gameDisplay, black, (int(display_width*0.1)+44, int(display_height*0.1)+127, 70, 20))

		#player2
		message_display('Player 2',40, int(display_height*0.1)+100, int(display_width*0.2)+400 , blue, 'Western.ttf')
		pygame.draw.rect(gameDisplay, light_yellow, (int(display_width*0.1)+440, int(display_height*0.1)+125, 80, 25))
		pygame.draw.rect(gameDisplay, red, (int(display_width*0.1)+444, int(display_height*0.1)+127, 70, 20))

		#play button
		#button(msg, button_x, button_y, button_width, button_height, inactive_color, active_color, textfont, text_size, object of the function)
		button('Play!', int(display_width*0.1)+240, int(display_height*0.1)+100, 100, 50 , green, red, 'freesansbold.ttf', 45, game_loop)

		#How To Play
		#message_display(text, size, x,y , color, font)
		message_display('How To Play',40, 290, 120 , black, 'Western.ttf')
		img = pygame.image.load('ss_1.png')
		gameDisplay.blit(pygame.transform.scale(img, (250,250)), (150, 320))

		img = pygame.image.load('ss_2.png')
		gameDisplay.blit(pygame.transform.scale(img, (250,250)), (420, 320))



		pygame.display.update()

		clock.tick(60)


def game_loop():
	a_point, b_point = 0,0
	a_warriors, b_warriors = [[40, 150], [40, 300], [40, 450]] ,[[760, 150], [760, 300], [760, 450]]
	a_all_moves = []
	b_all_moves = []
	while True:
		for event in pygame.event.get():
			#print(event)
			if event.type==pygame.QUIT:
				quit_fun()
			if event.type==pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					#print('Hello')
					mouse = pygame.mouse.get_pos()
					check = check_warrior_click(a_warriors,b_warriors,mouse)
					#print('cordi',mouse)
					if check[0]:
						#print('Check done')
						#warrior_coordinates.remove(check[1])
						next_warrior=click_and_draw(check[1])
						if check[0]=='a':
							#print('in a')
							a_warriors.append(next_warrior)
							a_all_moves.append([check[1],next_warrior])
							#a_warriors.remove(check[1])
							b_all_moves, a_point = fight((check[1],next_warrior),b_all_moves,b_warriors, a_point)
						elif check[0]=='b':
							#print('in b')
							b_warriors.append(next_warrior)
							b_all_moves.append([check[1],next_warrior])
							#b_warriors.remove(check[1])
							a_all_moves, b_point = fight((check[1],next_warrior),a_all_moves, a_warriors, b_point)



		gameDisplay.fill(burlywood)
		#player1/fighter1
		#background_img('image_4.jpg')
		button('<', 25, 12, 40, 30 , red, grey, 'freesansbold.ttf', 45, game_intro_loop)

		frighter_drawer( 40, 150, grey, 20)
		frighter_drawer( 40, 150, black, warrior_radius)

		#player1/fighter2
		frighter_drawer( 40, 300, grey, 20)
		frighter_drawer( 40, 300, black, warrior_radius)

		#player1/fighter3
		frighter_drawer( 40, 450, grey, 20)
		frighter_drawer( 40, 450, black, warrior_radius)

		#player2/fighter1
		frighter_drawer( 760, 150, light_yellow, 20)
		frighter_drawer( 760, 150, red, warrior_radius)

		#player2/fighter2
		frighter_drawer( 760, 300, light_yellow, 20)
		frighter_drawer( 760, 300, red, warrior_radius)

		#player2/fighter2
		frighter_drawer( 760, 450, light_yellow, 20)
		frighter_drawer( 760, 450, red, warrior_radius)

		#score board:
		message_display('Player1',40, 25, 300 , white, 'Western.ttf')
		pygame.draw.rect(gameDisplay,white,(360,5,40,40))
		message_display(str(a_point),40, 26, 377 , black, 'Western.ttf')
		message_display('Vs',50, 25, 425 , red, 'Western.ttf')
		pygame.draw.rect(gameDisplay,white,(450,5,40,40))
		message_display(str(b_point),40, 26, 467 , black, 'Western.ttf')
		message_display('Player2',40, 25, 550 , white, 'Western.ttf')

		#field
		empty_rectangle((field_coordinates[0],field_coordinates[1]),(field_coordinates[0]+field_width,field_coordinates[1]),(field_coordinates[0]+field_width,field_coordinates[1]+field_height),(field_coordinates[0],field_coordinates[1]+field_height),3)

		for i in a_all_moves:
			pygame.draw.line(gameDisplay, grey, i[0], i[1], 3)
		for i in b_all_moves:
			pygame.draw.line(gameDisplay, red, i[0], i[1], 3)

		pygame.display.update()

		clock.tick(60)

if __name__=='__main__':
	game_intro_loop()