# Authors: Andrew Tissi, Max Spangaro, Christian Ricci, Alexander Penha
# Date: 6/9/21
# Description: Final summative for computer science, this is the title screen which allows the user to navigate to each game

import pygame#imports the pygame library
import Chess#imports the chess game
import CountryGuesser#imports the country guesser game
import Plinko#imports the plinko game
import Pong#imports the pong game
import os#imports the os library
import balance#imports the balance library
from os import path#imports path from the os library

#Functions--------------------------------

def userinfo(user,screen):
	"""Displays the user's information"""
	w=screen.get_width()#gets the width of the screen
	h=screen.get_height()#gets the height of the screen
	color=(255,255,255)#the color of the text
	font = pygame.font.Font('freesansbold.ttf', 30)#sets the font
	text = font.render("Username: "+str(user.name)+"     Balance: $"+str(user.bal), True, color)#prints the information
	textRect = text.get_rect()#gets a rectangle for the text
	textRect.center = (w/2,h*0.27)#alligns the center of the text box
	screen.blit(text, textRect)#draws the text to the screen

#Functions--------------------------------

def run():
	'''Runs the main title'''
	width = 640#sets the width of the screen
	height = 400#sets the height of the screen

	clock = pygame.time.Clock()#creates a clock
	running = True#sets the game to running
	LEFT = 1#defines a left click as 1
	screen = pygame.display.set_mode((width, height))#creates a screen
	pygame.font.init()#initilises the pygame font
	#coordinates for boxes
	#			x1 , y1   x2 , y2

	#Arrays/Lists--------------------------------

	countryGuesser_box=[[16,166],[147,317]]#country guesser box coordinates
	chess_box=[[143,166],[310,317]]#chess box coordinates
	plinko_box=[[330,166],[469,317]]#plinko box coordinates
	pong_box=[[490,166],[626,317]]#pong box coordinates
	quit_box=[[193,351],[321,382]]#quit box coordinates
	switch_box=[[331,352],[459,379]]#switch account box coordinates

	#Arrays/Lists--------------------------------

	TitleScreen = pygame.image.load("./assets/Title/Title Screen.png")#gets the image of the title screen
	TitleScreen_rect = TitleScreen.get_rect()#makes a rectangle for the title screen
	screen.blit(TitleScreen, TitleScreen_rect)#places the title screen image onto the screen
	pygame.display.flip()#prints the screen
	os.system('clear')#clears the console
	player=balance.User("Welcome to the arcade!\n\nIMPORTANT: If you are running this on the spotlight page,\nsome of the screen will be hidden under the console.\nTo fix this, just fork the project (top right) and run it as a new project\n\n")#creates a user object
	test=0#sets test to 0 because nothing needs to be tested now

	while running:#runs this as in infinite loop
		pygame.display.flip()#draws the game
		for event in pygame.event.get():#runs whenever there is an event

			if event.type == pygame.QUIT:#checks if the user quits
				running = False#stops the game

			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:#checks if the user left clicked
				x, y = event.pos#gets the position of the click
				if test==1:#checks if we want to test
					print(x, y)#prints coordinates wherever the user clicks (for finding rectangles of the boxes)

				elif countryGuesser_box[0][0]<=x<=countryGuesser_box[1][0] and countryGuesser_box[0][1]<=y<=countryGuesser_box[1][1]:#checks if the user clicked on the country guesser box 
					os.system('clear')#clears the screen
					pygame.event.clear()#clears the buffered events in pygame.event
					CountryGuesser.run(player)#runs the country guesser game
					screen = pygame.display.set_mode((width, height))#resets the screen
					os.system('clear')#clears the screen
					x=y=0#resets the x and y coordinates for the mouse
					pygame.event.clear()#clears the buffered events in pygame.event
					break

				elif chess_box[0][0]<=x<=chess_box[1][0] and chess_box[0][1]<=y<=chess_box[1][1]:#checks if the user clicked on the chess box 
					os.system('clear')#clears the screen
					pygame.event.clear()#clears the buffered events in pygame.event
					Chess.run(player)#runs the chess game
					screen = pygame.display.set_mode((width, height))#resets the screen
					os.system('clear')#clears the screen
					x=y=0#resets the x and y coordinates for the mouse
					pygame.event.clear()#clears the buffered events in pygame.event
					break

				elif plinko_box[0][0]<=x<=plinko_box[1][0] and plinko_box[0][1]<=y<=plinko_box[1][1]:#checks if the user clicked on the plinko box
					os.system('clear')#clears the screen
					pygame.event.clear()#clears the buffered events in pygame.event
					Plinko.run(player)#runs the plinko game
					screen = pygame.display.set_mode((width, height))#resets the screen
					os.system('clear')#clears the screen
					x=y=0#resets the x and y coordinates for the mouse
					pygame.event.clear()#clears the buffered events in pygame.event
					break

				elif pong_box[0][0]<=x<=pong_box[1][0] and pong_box[0][1]<=y<=pong_box[1][1]:#checks if the user clicked on the pong box
					os.system('clear')#clears the screen
					pygame.event.clear()#clears the buffered events in pygame.event
					Pong.run(player)#runs the pong game		
					screen = pygame.display.set_mode((width, height))#resets the screen
					os.system('clear')#clears the screen
					x=y=0#resets the x and y coordinates for the mouse
					pygame.event.clear()#clears the buffered events in pygame.event
					break

				elif quit_box[0][0]<=x<=quit_box[1][0] and quit_box[0][1]<=y<=quit_box[1][1]:#checks if the user clicked on the quit box
					os.system('clear')#clears the screen
					pygame.event.clear()#clears the buffered events in pygame.event
					print("Thanks for playing!")#thanks the user for playing
					pygame.event.clear()#clears the buffered events in pygame.event
					return

				elif switch_box[0][0]<=x<=switch_box[1][0] and switch_box[0][1]<=y<=switch_box[1][1]:#checks if the user clicked on the switch account box
					os.system('clear')#clears the screen
					pygame.event.clear()#clears the buffered events in pygame.event
					player=balance.User("Welcome to the arcade!\n")#creates a new user object
					pygame.event.clear()#clears the buffered events in pygame.event
					break
					
		screen.blit(TitleScreen, TitleScreen_rect)#prints the title screen
		userinfo(player,screen)#prints the user's info
		pygame.display.flip()#displays the screen
		clock.tick(60)#delays 60ms before drawing the screen again



if path.exists('assets/coconut.jpg'): #only runs the game if the coconut exists, (TF2 reference)
	run()#runs the entire game