# Authors: Andrew Tissi
# Date: Created: 4/1/21
# Description: functions to do with the board

import pygame#imports the pygame library
import config#imports the config library

#Functions--------------------------------

def printBoard():
	'''prints the background of the board'''
	config.screen.fill(config.backgroundColor)#sets the background of the screen
	dark_square = pygame.image.load("./assets/chess/background/chess_dark.png")#gets the dark square sprite
	dark_square_rect = dark_square.get_rect().move(config.square,0)#creates the rectangle for the dark square
	#32 dark squares in the board
	
	for i in range (32):#loops through 32 times, once for each dark square
		config.screen.blit(dark_square, dark_square_rect)#prints the dark square onto the board
		dark_square_rect = dark_square_rect.move(config.square*2,0)#moves the dark square
		#moves down to the next row
		
		if dark_square_rect[0]+config.square>config.width:#square is off the screen
			dark_square_rect = dark_square_rect.move(-config.width-config.square,config.square)#moves the square down 1 rank
			if dark_square_rect[0]<0:#checks if the dark square is below 0
				dark_square_rect = dark_square_rect.move(config.square*2,0)#moves the dark square

def printNumbersAndLetters():
	'''prints the numbers and letters onto the board'''
	color = config.start#gets the color of the bottom player
	#conversion dictionary

	#Arrays/Lists--------------------------------

	convert = {
		'1': 'A',
		'2': 'B',
		'3': 'C',
		'4': 'D',
		'5': 'E',
		'6': 'F',
		'7': 'G',
		'8': 'H'
	}

	#Arrays/Lists--------------------------------
	
	#black numbers and letters
	
	if color=="black":#checks if the bottom player is black
		#numbers
		
		for i in range (8):#loops through 8 times
			number = pygame.image.load("./assets/chess/numbers/black/"+str(i+1)+".png")#finds the coresponding number
			number_rect = number.get_rect().move(0,config.square*i)#gets the rectangle of the coresponding number
			config.screen.blit(number, number_rect)#prints the number to the screen
		#letters
		
		for c in range (8):#loops through 8 times
			letter = pygame.image.load("./assets/chess/letters/black/"+convert[str(8-c)]+".png")#finds the coresponding letter
			letter_rect = letter.get_rect().move((config.square*c)+40,config.height-20)#gets the rectangle of the coresponding letter
			config.screen.blit(letter, letter_rect)#prints the letter to the screen
		
	#white numbers and letters

	else:#checks if the bottom is white
		#numbers
		
		for i in range (8):#loops through 8 times
			number = pygame.image.load("./assets/chess/numbers/white/"+str(8-i)+".png")#finds the coresponding number
			number_rect = number.get_rect().move(0,config.square*i)#gets the rectangle of the coresponding number
			config.screen.blit(number, number_rect)#prints the number to the screen
		#letters
		
		for c in range (8):#loops through 8 times
			letter = pygame.image.load("./assets/chess/letters/white/"+convert[str(c+1)]+".png")#finds the coresponding letter
			letter_rect = letter.get_rect().move((config.square*c)+40,config.height-20)#gets the rectangle of the coresponding letter
			config.screen.blit(letter, letter_rect)#prints the letter to the screen

def printAllPieces(table):
	'''prints all the pieces'''
	posy=0#y position
	
	for c in range(8):#loops through each row
		posx=0#x position
		
		for d in range(8):#loops through each #collum
			
			if table[c][d] != 0:#checks if the current square holds a piece
				printPiece(table[c][d],posx,posy)#prints the piece
			posx+=config.square#increases the x position by the size of the square
		posy+=config.square#increases the y position by the size of the square

def printPiece(piece,x,y):
	'''prints one piece'''
	piece = pygame.image.load("./assets/chess/pieces/"+piece+".png")#gets the sprite of the current piece
	piece_rect = piece.get_rect().move(x,y)#gets the rectangle of the piece and moves it to where its supposed to be
	config.screen.blit(piece, piece_rect)#prints the piece
	return#returns

def displayScreen(chessBoard):
	'''prints everything together'''
	printBoard()#prints the background of the board
	printNumbersAndLetters()#prints the numbers and letters
	printAllPieces(chessBoard)#prints the pieces on the board
	pygame.display.flip()	#outputs the screen

def drawRedSquare(x,y):
	'''prints a red square where the user cant go if they try'''
	red_square = pygame.image.load("./assets/chess/background/chess_red.png")#loads the red square
	red_square_rect = red_square.get_rect().move(x*config.square,y*config.square)#creates a rectangle for the red square to be in
	config.screen.blit(red_square, red_square_rect)#prints the red square to the screen
	pygame.display.flip()	#outputs the screen

def printAllCircles(circles):
	'''prints the circles to guide the user where they can go'''
	
	for i in circles:#loops through for all the positions where the circles need to be
		posy=0#y position
		
		for c in range(8):#loops through each row
			posx=0#x position
			
			for d in range(8):#loops through each #collum
				
				if d==int(i[0]) and c==int(i[1]):#finds if a circle needs to be printed here
					printCircle(posx,posy)#prints the circle
				posx+=config.square#increases the x position by the size of the square
			posy+=config.square#increases the y position by the size of the square

def printCircle(x,y):
	'''prints one circle to show the user where they can go'''
	dot = pygame.image.load("./assets/chess/background/dot.png")#loads the dot from the assets folder
	dot_rect = dot.get_rect().move(x,y)#gets the rectangle of the dot and moves it to where it needs to be moved to
	config.screen.blit(dot, dot_rect)#prints the dot
	pygame.display.flip()#optputs the game
	return#returns

#Functions--------------------------------