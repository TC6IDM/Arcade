#author: max spangaro
#date: may 18, 2021
#description: the user is presented a map of europe. they will have 10 seconds to locate the country asked of them, and then click on it to select their choice. if they are right, they get a point, if they are not right, they lose a point. the amount of points that they have will translate to how many tokens they will get.

import pygame#imports the pygame library
import random#imports the random library
import os#imports the OS library

def run(player):
	'''runs the country guesser game'''
	os.system('clear')#clears the screen
	#creates a dictonary with all the countrys and their associated RGB colors

	#Arrays/Lists--------------------------------

	dictionary={
		"Portugal":[21,172,7,255], #dictionary of all of the countries and the colour tag that it is on the image
		"Spain":[205,204,52,255],
		"Great Britian":[210,18,181,255],
		"France":[0,51,204,255],
		"Ireland":[111,246,84,255],
		"Iceland":[143,131,141,255],
		"Norway":[202,227,231,255],
		"Sweden":[29,117,206,255],
		"Denmark":[238,103,58,255],
		"Finland":[219,217,192,255],
		"Belgium":[230,195,41,255],
		"Netherlands":[226,146,51,255],
		"Germany":[47,42,48,255],
		"Poland":[244,4,253,255],
		"Latvia":[124,6,28,255],
		"Lithuania":[255,251,2,255],
		"Estonia":[15,191,181,255],
		"Russia":[9,56,4,255],
		"Belarus":[60,115,22,255],
		"Ukraine":[87,107,194,255],
		"Moldova":[86,190,129,255],
		"Romania":[168,152,17,255],
		"Hungary":[89,46,4,255],
		"Austria":[235,228,222,255],
		"Czechia":[105,94,49,255],
		"Slovakia":[190,171,217,255],
		"Slovenia":[162,73,167,255],
		"Croatia":[96,12,211,255],
		"Serbia":[137,71,11,255],
		"Bosnia":[44,116,4,255],
		"Montenegro":[79,72,64,255],
		"North Macedonia":[116,71,126,255],
		"Albania":[226,13,45,255],
		"Greece":[44,168,222,255],
		"Turkey":[159,114,75,255],
		"Cyprus":[220,70,50,255],
		"Italy":[38,68,4,255],
		"Switzerland":[179,46,67,255],
		"Bulgaria":[173,215,205,255],
	}

	#Arrays/Lists--------------------------------

	width,height=500, 500#sets the width and height of the screen
	screen = pygame.display.set_mode((width, height))#creates the screen
	clock = pygame.time.Clock()#creates a clock
	picture = pygame.image.load("./assets/CountryGuesser/Europe-Blank-map-Outline.jpg")#loads the map
	picture_rect = picture.get_rect()#gets the rectangle of the map
	screen.blit(picture, picture_rect)#places the map on the screen
	pygame.display.flip()#prints the screen to the user
	player.get_bet()#asks the user for their bet
	running=True#sets the game to always running
	countryList=list(dictionary)#creates a list out of the dictionary

	#random--------------------------------

	rand=random.randint(0,len(countryList)-1)#gets a random index of the dictionary

	#random--------------------------------

	currentCountry=countryList[rand]#gets a random country
	dictColors=dictionary[currentCountry]#gets the color of the country
	print("Click on "+str(currentCountry))#tells the user what country to click on
	correct=0#sets the amount of correct guesses to 0
	incorrect=0#sets the amount of incorrect guesses to 0
	pygame.event.clear()#clears the buffered events in pygame.event

	while running:#runs this code while the program is on
		pygame.display.flip()#draws the game
		for event in pygame.event.get():#runs whenever there is an event
			
			
			if event.type == pygame.QUIT:#checks if the user wants to quit
				running = False#stops running the program
			
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#checks if the user left clicked
				os.system('clear')#clears the screen
				x, y = event.pos#gets the position of the click
				r, g, b, a = screen.get_at((x, y))#gets the color that the user clicked on
				playerColors=r, g, b, a#sets the player's colors
				tolerance=20#sets the tolerance to 20 color values
				
				if (playerColors[0] in range (dictColors[0]-tolerance,dictColors[0]+tolerance)) and (playerColors[1] in range (dictColors[1]-tolerance,dictColors[1]+tolerance)) and (playerColors[2] in range (dictColors[2]-tolerance,dictColors[2]+tolerance)) and (playerColors[3] in range (dictColors[3]-tolerance,dictColors[3]+tolerance)):#checks if the user clicked on the correct country within a given tolerance
					print("correct")#prints correct
					correct+=1#increments the user's correct guesses
				
				else:#the user did not get the country correct
					incorrect+=1#increments the user's incorrect guesses
					print("incorrect")#prints incorrect
				print(str(correct)+" / "+str(incorrect+correct))#prints the user's correct vs incorrect score
				countryList.pop(rand)#removes the country from the country list
				
				if len(countryList)>0:#checks if there are more countrys left

					#random--------------------------------

					rand=random.randint(0,len(countryList)-1)#gets a new random index

					#random--------------------------------

					currentCountry=countryList[rand]#gets a new random country
					print("\nNow, click on "+str(currentCountry))#tells the user to click on the new country
					dictColors=dictionary[currentCountry]#finds the colors of the country
				
				else:#checks if there are no more countrys left
					print("\nGame over!")#prints that the game is over
					multi=((1/15)*correct)#finds the user's multiplier
					print (player.name+" your multiplier is "+str(multi)+"x")#displays the user's multiplier
					player.updateBal(multi)#updates the user's balance with the given multiplier
					player.display_bal()#displays the user's balance
					input("Press Enter at any time to return to the main screen")#asks the user to press enter to return to the main screen
					return#returns to the main screen
		screen.blit(picture, picture_rect)#prints the picture to the screen
		pygame.display.flip()#displays the screen
		clock.tick(60)#ticks the clock 60ms


