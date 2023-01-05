# Author: Christian
# Date: 5/16/21
# Description: Game of plinko, the ball falls down the triangle of poles and eventually lands in one of the multipliers

import pygame #imports pygame libary
import random #imports random libary
import math #imports math libary
import os #imports os libary

#OOP--------------------------------

class Ball: # creates a class for the ball and all it's propertys 
	def __init__(self,surface,triangle):
		'''initilises the ball class'''
		self.radius=5#sets the radius of the ball

		#random--------------------------------

		self.linecolor=random.randint(155,255),random.randint(155,255),random.randint(155,255)#creates a random bright color

		#random--------------------------------

		self.pole_radius=3#sets the pole's radius to 3
		self.vx=0#sets the velocity in the x to 0
		self.vy=0#sets the velocity in the y to 0
		self.a=0.2#sets the acceleration to 0.2
		self.surface=surface#gets the surface
		self.w=self.surface.get_width()#finds the width of the screen
		self.h=self.surface.get_height()#finds the height of the screen
		self.released=False#the ball is not released to set released to false
		self.leftbound=round(29*self.w/64)#finds the left bound of the box
		self.rightbound=self.w-self.leftbound#finds the right bound of the box
		self.bottombound=round(self.h/12)#finds the bottom bound of the box
		self.triangle=triangle#sets the triangle of poles
		self.x11=self.triangle[0][-1][0]-self.pole_radius#finds the bottom right dot's x value
		self.y21=self.triangle[0][-1][1]#finds the bottom right dot's y value
		self.x21=self.triangle[-1][-1][0]-self.pole_radius#finds the top right dot's x value
		self.y11=self.triangle[-1][-1][1]#finds the top right dot's y value
		self.right_line=getEquationOfLine(self.x11,self.y11,self.x21,self.y21)#gets the equation of the line for the right line
		self.m_right=self.right_line[0]#gets the slope of the right line
		self.b_right=self.right_line[1]#gets the b value of the right line
		self.x12=self.triangle[0][0][0]+self.pole_radius#finds the bottom left dot's x value
		self.y22=self.triangle[0][0][1]#finds the bottom left dot's y value
		self.x22=self.triangle[-1][0][0]+self.pole_radius#finds the top ;eft dot's y value
		self.y12=self.triangle[-1][0][1]#finds the top left dot's y value
		self.left_line=getEquationOfLine(self.x12,self.y12,self.x22,self.y22)
		self.m_left=self.left_line[0]#gets the slope of the left line
		self.b_left=self.left_line[1]#gets the b value of the left line
		self.bouncyness=1.2#sets a bouncyness of the ball
		self.x=(self.leftbound+self.rightbound)/2#finds the ball's x value
		self.y=self.bottombound/2#finds the ball's y value
		self.inverseY=(self.h-self.y)#finds the inverse of the ball's y value

	def move(self):
		'''moves the ball'''
		if self.released==True:#checks if the ball is released
			self.vy+=self.a#adds the acceleration to the velocity
			self.y+=self.vy#adds the y velocity to the y value
			self.x+=self.vx#adds the x velocity to the x value
		
		else:#the ball is not released
			if self.x<=self.leftbound:#if the ball is too far to the left
				self.x=self.leftbound#moves the ball to the far left
			if self.x>=self.rightbound:#if the ball is too far to the right
				self.x=self.rightbound#moves the ball to the far right
			if self.y<=self.radius:#if the ball is too far up
				self.y=self.radius#moves the ball to the top
			if self.y>=self.bottombound:#if the ball is too far down
				self.y=self.bottombound#moves the ball to the bottom
		# self.vx+=(random.uniform(0.01, 0.02)*random.randint(-1,1))
		self.inverseY=(self.h-self.y)#resets the inverse y

	def draw_circle(self):
		'''Draws the circle'''
		pygame.draw.circle(self.surface, self.linecolor, (self.x,self.y), self.radius) #draws the ball

	def draw_box(self,triangle):
		'''Draws the starting box'''
		pygame.draw.line(self.surface, self.linecolor, (self.leftbound-self.radius, 0), (self.leftbound-self.radius, self.bottombound+self.radius))#left line
		pygame.draw.line(self.surface, self.linecolor, (self.rightbound+self.radius, 0), (self.rightbound+self.radius, self.bottombound+self.radius))#right line
		pygame.draw.line(self.surface,self.linecolor,(self.leftbound-self.radius,0),(self.rightbound+self.radius,0))#top line


		#the invisible walls (comment back in to draw them)
		# pygame.draw.line(self.surface,self.linecolor,(triangle[0][0][0]-self.pole_radius,triangle[0][0][1]),(triangle[-1][0][0]-self.pole_radius,triangle[-1][0][1]))#left diagonal
		# pygame.draw.line(self.surface,self.linecolor,(triangle[0][-1][0]+self.pole_radius,triangle[0][-1][1]),(triangle[-1][-1][0]+self.pole_radius,triangle[-1][-1][1]))#right diagonal


		if self.released==True:return#checks if the ball is released
		#opens the hatch if the ball is released
		pygame.draw.line(self.surface,self.linecolor,(self.leftbound-self.radius,self.bottombound+self.radius),(self.rightbound+self.radius,self.bottombound+self.radius))#bottom line


	def colision(self,triangle):
		'''Works the colision for when a ball hits a pole or a wall'''
		
		for i in triangle:#loops through every row in the triangle
			
			for c in i:#loops through every pole in the row
				xcomp=self.x-c[0]#finds the distance from this pole in the x direction
				ycomp=self.y-c[1]#finds the distance from this pole in the y direction
				
				if -(self.radius+self.pole_radius)<=xcomp<=(self.radius+self.pole_radius) and -(self.radius+self.pole_radius)<=ycomp<=(self.radius+self.pole_radius):#checks if the ball is close to coliding with the pole 
					distance=math.hypot(xcomp,ycomp)#finds the distance between the circles
					
					if distance<= self.radius+self.pole_radius:#checks if the ball is coliding with the pole

						if xcomp>0:#checks if the ball hits the right side of the pole
							#bounce right

							#random--------------------------------
							
							self.vx=random.uniform(0.4, 0.6)*self.bouncyness#makes a new velocity to the right

							#random--------------------------------

						if xcomp<0:#checks if the ball hits the left side of the pole
							#bounce left

							#random--------------------------------

							self.vx=random.uniform(0.4, 0.6)*self.bouncyness*-1#makes a new velocity to the left

							#random--------------------------------
							
						if xcomp==0:#checks if the ball hits directly on top of the pole
							#head on

							#random--------------------------------

							self.vx=(random.uniform(0.4, 0.6)*random.randint(-1,1))*self.bouncyness#sets a random velocity to the left or right

							#random--------------------------------

						#random--------------------------------

						self.vy*=-random.uniform(0.4, 0.6)*self.bouncyness#multiplies the y velocity with some dampness 

						#random--------------------------------

						self.y-=1#moves the ball up slightly

		
		if self.inverseY<=self.y21 and self.released==True:#checks if the ball can be effected by the invisible walls
			distance=(((self.x-self.radius)*self.m_left)+self.b_left)-self.inverseY#finds the distance to the left wall
			
			if distance<=0:#bounce right
				self.vx*=-1#reverses the velocity

			distance=((self.x+self.radius)*self.m_right+self.b_right)-self.inverseY#finds the distance to the right wall
			
			if distance<=0:#bounce left
				self.vx*=-1#reverses the velocity

#OOP--------------------------------

#Functions--------------------------------

def winnings(ball,player,risk,riskDict,columns):
	'''Calculates the winnings'''
	if risk=="high":#checks if the risk is high
		risklevel=0#sets the risk level to 0
	
	elif risk=="medium":#checks if the risk is medium
		risklevel=1#sets the risk level to 1
	
	elif risk=="low":#checks if the risk is low
		risklevel=2#sets the risk level to 2

	
	for i in range(9):#loops through each multiplier box
		
		if ball.triangle[0][i][0]<=ball.x<= ball.triangle[0][i+1][0] or ball.triangle[0][columns-(i+2)][0]<=ball.x<= ball.triangle[0][columns-(i+1)][0]:#checks if the ball landed in this box
			riskNumber=i+1#sets the risk number to the box's number
	player.updateBal(riskDict[riskNumber][risklevel])#updates the player's balance according to where the ball landed as well as the risk
	return riskDict[riskNumber][risklevel]#returns the multiplier

def create_triangle(surface,columns):
	'''creates a triangle of dots'''
	triangle=[]#creates an array to store the dots
	
	for c in range(columns,2,-1):#loops through for each colum in reverse order
		opp=(columns-c)+1#finds the opposite of the c value
		row=[]#creates an array to store each row
		
		for i in range(c):#loops through for each amount of dots in this row
			xpos=int(round(((i+(opp*(1/2)))*surface.get_width()/columns)))#gets the x position of the dot
			ypos=int(round(((((11-opp)*surface.get_height())/(columns)))+(7*surface.get_height()/columns)))#gets the y position of the dot
			row.append([xpos,ypos])#appends the x and y values to the row
		triangle.append(row)#appends the row to the triangle
	return triangle#returns the triangle

def draw_triangle(surface,triangle,radius,color):
	'''draws the triangle'''
	for i in triangle:#loops through each row in the triangle
		
		for c in i:#loops through for each dot in the triangle
			xpos=c[0]#finds the x positon of the dot
			ypos=c[1]#finds the y positon of the dot
			pygame.draw.circle(surface, color, (xpos,ypos), radius)#draws a circle around this position

def getEquationOfLine(x1,y1,x2,y2):
	'''returns the m and b values of a line, when given 2 x values, and 2 y values'''
	m=(y2-y1)/(x2-x1)#finds the m value of the line
	b=y1-(m*x1)#finds the b value of the line
	return [m,b]#returns the 2 values

def draw_multis(risk,riskDict,columns,triangle,b,font):
	'''draws the multipliers '''
	for i in range(0,len(triangle[0])-1):#loops through each multiplier
		
		if risk=="high":#checks if the risk is high
			risklevel=0#sets the risk level to 0
		
		elif risk=="medium":#checks if the risk is medium
			risklevel=1#sets the risk level to 1
		
		elif risk=="low":#checks if the risk is low
			risklevel=2#sets the risk level to 2
		x1,x2=triangle[0][i][0],triangle[0][i+1][0]#finds the x1 and x2 values of the rectangle
		y1,y2=triangle[0][i][1]+b.pole_radius,b.h#finds te y1 and y2 values of the rectangle
		R=255#sets the r value to 255
		G=(-1*abs(((i+1)*24)-216))+192#finds the green value using an equation
		B=abs(((i+1)*-8)+72)#finds the b value using an equation
		
		black=(0,0,0)#sets the color black

		box = pygame.Rect((x1,y1),(x2-x1,y2-y1))#creates a rectangle for the box

		pygame.draw.rect(b.surface,(R,G,B),box)#draws the box
		
		if i !=0:#checks if this is not the first box
			pygame.draw.line(b.surface, black, (x1, y1), (x1, b.h))#draws a line to the left to seperate the boxes

		key=(-1*abs((i+1)-9))+9#finds which number this box corresponds to in the risk dictionary
		text = font.render(str(riskDict[key][risklevel]), True, black)#prints the mutli
		textRect = text.get_rect()#gets a rectangle for the text
		textRect.center = ((x1+x2)/2,(y1+y2)/2)#alligns the center of the text box
		b.surface.blit(text, textRect)#draws the text to the screen
	

def draw_lastwin(multi,b):
	'''writes the last win on this game'''
	if multi!=0:#checks if there was a last game
		white=(255,255,255)#sets the color white
		font = pygame.font.Font('freesansbold.ttf', 24)#sets the font
		text = font.render("Last Multiplier", True, white)#prints the mutliplier
		textRect = text.get_rect()#gets a rectangle for the text
		textRect.center = (7*b.w/9,b.h/13)#alligns the center of the text box
		b.surface.blit(text, textRect)#draws the text to the screen
		text = font.render(str(multi)+"x", True, white)#prints the mutli
		textRect = text.get_rect()#gets a rectangle for the text
		textRect.center = (7*b.w/9,b.h/8)#alligns the center of the text box
		b.surface.blit(text, textRect)#draws the text to the screen

def infocard():
	'''a function that prints some basic information'''

	#prints basic information
	print("WHILE FOCUSED ON THE SCREEN (not the console)")
	print("Press 'Q' on your keyboard to return to the main hub.")
	print("Press 'B' on your keyboard to enter a new bet.")
	print("Press 'A' on your keyboard to enter a new risk.")

#Functions--------------------------------

def run(player):
	'''runs the whole game'''
	os.system('clear')#clears the screen

	#Arrays/Lists--------------------------------
	
	riskDict={#creates a dictionary which stores each multiplier
		1:[1000,110,16],
		2:[130,41,9],
		3:[26,10,2],
		4:[9,5,1.4],
		5:[4,3,1.4],
		6:[2,1.5,1.2],
		7:[0.2,1,1.1],
		8:[0.2,0.5,1],
		9:[0.2,0.3,0.5],
	}

	#Arrays/Lists--------------------------------

	bgcolor = 0, 0, 0 # sets background color
	LEFT = 1 #sets the left key press
	running = 1#sets running to 1
	w=500#sets the width of the screen
	h=600#sets the height of the screen
	columns=18#sets the amount of columns to 18
	surface = pygame.display.set_mode((w, h)) # sets display size 
	clock = pygame.time.Clock()#creates a clock
	triangle=create_triangle(surface,columns)#creates a triangle
	
	#prints some information regarding the game
	print("Welcome to Plinko!")
	print("")#prints an empty line
	print("Enter your bet and risk factor and drop the ball for a chance to win lots of tokens!")
	print("")#prints an empty line
	infocard()#calls the infocard function
	print("")#prints an empty line
	b=Ball(surface,triangle)#creates a ball object
	risk="none"#sets the risk to none
	multi=0#sets the multiplier to 0
	pygame.font.init()#initilises the pygame font
	font = pygame.font.Font('freesansbold.ttf', 12)#sets the font
	draw_triangle(surface,triangle,b.pole_radius,b.linecolor)#draws the triangle of dots
	b.draw_circle()#draws the circle
	b.draw_box(triangle)#draws the box surrounding the circle
	draw_lastwin(multi,b)#writes the user's last win
	draw_multis("medium",riskDict,columns,triangle,b,font)#draws the miltipliers
	pygame.display.flip()#displays the screen to the user
	
	while risk not in "high medium low":#checks if the user did not type high medium or low into their risk
		risk=input("high, medium, or low risk? ").lower()#gets the user's risk
		os.system('clear')#clears the screen
	player.get_bet()#gets the user's bet
	infocard()#displays the infocard
	pygame.event.clear()#clears the buffered events in pygame.event
	
	while running:#loops this game while it is running
		pygame.display.flip()#draws the game
		for event in pygame.event.get():#loops though each event as pygame recieves them
			
			if event.type == pygame.QUIT: #if the user hits the x button
				
				if b.released==False:#checks if the ball is not released
					running = 0 # program stops running
					return#program stops running
			
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:# if the user types q
				
				if b.released==False: #checks if the ball is not released
					running = 0 # program stops running
					return # program stops running
			
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_b: #if the user types b
				
				if b.released==False:#checks if the ball is not released
					os.system('clear')#clears the screen
					player.get_bet()#gets the player's new bet
					b=Ball(surface,triangle)#creates a new ball object
					os.system('clear')#clears the screen
					player.display_bal()#displays the user's balance
					infocard()#prints an infocard
			
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:#if the user types a 
				if b.released==False:#checks if the ball is not released
					os.system('clear')#clears the screen
					risk="none"#sets the risk to none
					while risk not in "high medium low":#checks if the user did not type 
						risk=input("high, medium, or low risk? ").lower()#gets the user's risk
						os.system('clear')#clears the screen
					b=Ball(surface,triangle)#creates a new ball object
					player.display_bal()#displays the user's balance
					infocard()#prints the infocard
				
			elif event.type == pygame.MOUSEMOTION: # if the mouse moves
				if b.released==False:#checks if the ball is not released
					b.x,b.y=event.pos#sets the bal's new x and y values to where the mouse is 
					b.move()#calls the move function

			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT: # if left mouse button is clicked
				b.released=True#releases the ball
			
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:#checks if the user pressed the down button
				b.linecolor = random.randint(155,255),random.randint(155,255),random.randint(155,255) # changes random color
				print("Secret Button Pressed! Board color changed to: " + str(b.linecolor)) # prints changed color
			
			# pygame.draw.line(screen, linecolor, (0, y), (w-1, y)) #draws line vertical
		
		surface.fill(bgcolor) # changes background color
		draw_triangle(surface,triangle,b.pole_radius,b.linecolor)#draws the triangle
		b.move()#moves the ball
		b.colision(triangle)#checks for colision 
		b.draw_circle()#draws the circle
		b.draw_box(triangle)#draws the box
		draw_lastwin(multi,b)#draws the last win
		draw_multis(risk,riskDict,columns,triangle,b,font)#draws the multipliers
		
		if b.y-(b.radius+b.pole_radius)>=b.triangle[0][0][1]: #checks if the ball has fallen to the bottom
			multi=winnings(b,player,risk,riskDict,columns)#gets the multiplier they landed on
			surface.fill(bgcolor) # changes background color
			draw_triangle(surface,triangle,b.pole_radius,b.linecolor)#draws the triangle
			draw_lastwin(multi,b)#draws the user's win as the last win
			b.draw_box(triangle)#draws the box
			draw_multis(risk,riskDict,columns,triangle,b,font)#draws the multipliers 
			b=Ball(surface,triangle)#creates a new ball object
			pygame.display.flip()#prints all the new information to the screen
			os.system('clear')#clears the screen
			player.display_bal()#prints the user's balance
			infocard()#dispalys an infocard
			
			if player.bet>player.bal:#checks if the user's bet is larger than their bal (because they lost enough money to make their bet more than their current balance)
				os.system('clear')#clears the screen
				print("You need to chose a new bet")#tells the user that they have to make a new bet
				player.get_bet()#gets a new bet from the user
			os.system('clear')#clears the screen
			player.display_bal()#displays the user's balance
			infocard()#prints an infocard
		pygame.display.flip()#displays all inforamtion to the screen
		clock.tick(60)#ticks the clock to set the game to 60 fps