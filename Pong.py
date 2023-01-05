# Author: Alexander
# Date: 6/11/21
# Description: Game of pong, the ball moves untill hit by another paddle, first to reach a specified score, wins


import pygame #imports pygame libaray
import sys #imports system libaray
import random #imports random libaray   
import balance
import os
#----------------------------------------------------------#

#OOP--------------------------------

class Ball: #all the parameters for the pong ball 
	def __init__(self,screen,color,X,Y,size):
		self.screen = screen
		self.color = color
		self.X = X
		self.Y = Y
		self.size = size
		self.VX = 0 #How the ball is going to be moving in the X axis
		self.VY = 0 #How the ball is going to be moving in the Y axis
		self.display()

	def display(self):#displays the ball
		pygame.draw.circle(self.screen,self.color, (self.X,self.Y) ,self.size)

	def start(self): #how to ball will start
		positions=[[15,5],[-15,-5],[15,-5],[-15,5]]		
		
		#random--------------------------------

		rand=random.randint(0,len(positions)-1)

		#random--------------------------------

		self.VX = positions[rand][0]
		self.VY = positions[rand][1]

	def LGO(self):#Left goaled on: if the left player got scored on the ball will start on there side
		positions=[[15,5],[15,-5]]

		#random--------------------------------

		rand=random.randint(0,len(positions)-1)

		#random--------------------------------
		
		self.VX = positions[rand][0]
		self.VY = positions[rand][1]

	def RGO(self):#Right goaled on: if the Right player got scored on the ball will start on there side
		positions=[[-15,5],[-15,-5]]

		#random--------------------------------
		
		rand=random.randint(0,len(positions)-1)
		
		#random--------------------------------

		self.VX = positions[rand][0]
		self.VY = positions[rand][1]


	def move(self): #how the ball moves
		self.X += self.VX
		self.Y += self.VY
	
	def paddlecollision(self):#collision with paddle
		self.VX = -self.VX

	def wallcollision(self): #how the ball will react after hitting a wall
		self.VY = -self.VY

	def Reset_Left(self):#if right player scores it will reset te ball to the middle then call 'self.LGO'
		self.X = pong_width/2
		self.Y = pong_length/2
		self.VX = 0
		self.VY = 0
		self.display()
		self.LGO()

	def Reset_Right(self):#if Left player scores it will reset te ball to the middle then call 'self.RGO'
		self.X = pong_width/2
		self.Y = pong_length/2
		self.VX = 0
		self.VY = 0
		self.display()
		self.RGO()

#----------------------------------------------------------#	
class Paddle: #all the parameters for the pong paddles 
	def __init__(self,screen,color,X,Y,width,length):
		self.initX=X
		self.initY=Y
		self.screen = screen
		self.color = color
		self.X = X
		self.Y = Y
		self.width = width
		self.length = length
		self.state = 0 #going to tell us if the paddle is going up or down
		self.display()

	def display(self): #displays the paddles
		pygame.draw.rect(self.screen,self.color, (self.X,self.Y,self.width,self.length))

	def move(self): #allows the paddles to move
		if self.state == 1:
			self.Y -= 10
		elif self.state == 2:
			self.Y += 10

	def collision(self):#adds wall collisions to the paddles 
		#up  wall collision
		if self.Y <= 0:
			self.Y = 0
		#down wall collision
		if (self.Y+self.length) >= pong_length:
			self.Y = pong_length-self.length

	def Reset(self):#if right player scores it will reset te ball to the middle then call 'self.LGO'
		self.X = self.initX
		self.Y = self.initY
		self.display()


#----------------------------------------------------------#
class Score:
	def __init__(self,screen, points,X,Y):
		self.screen = screen
		self.points = points
		self.X = X
		self.Y = Y
		self.font = pygame.font.SysFont("monospace", 40, bold=True) #creates a font
		self.label = self.font.render(self.points, 0, Bcolor)
		self.show

	def show (self):
		self.screen.blit(self.label,(self.X - self.label.get_rect().width/2,self.Y))#displays the scores and puts it in coder defined place 

	def score (self):
		points = int( self.points ) + 1
		self.points = str(points)
		self.label = self.font.render(self.points, 0, Bcolor)

#----------------------------------------------------------#
class Info:
	def __init__(self,screen, text,X,Y):
		self.screen = screen
		self.text = text
		self.X = X
		self.Y = Y
		self.font = pygame.font.SysFont("monospace", 40, bold=True) #creates a font
		self.label = self.font.render(self.text, 0, Bcolor)
		self.show

	def show (self):
		self.screen.blit(self.label,(self.X - self.label.get_rect().width/2,self.Y))#displays the scores and puts it in coder defined place 


#----------------------------------------------------------#
class Collision_management:

	def LPB(self, ball, LeftPaddle):#collision bettween left paddle and ball
		
		if ball.Y + ball.size > LeftPaddle.Y and ball.Y - ball.size < LeftPaddle.Y +LeftPaddle.length:#checks if balls y cord is at the right position
			
			if ball.X - ball.size <= LeftPaddle.X + LeftPaddle.width:#checks if balls x cord is at the right position
				return True
		return False

	def RPB (self, ball, RightPaddle): #collision bettween rigth paddle and ball
		
		if ball.Y + ball.size > RightPaddle.Y and ball.Y - ball.size < RightPaddle.Y + RightPaddle.length:#checks if balls y cord is at the right position
			
			if ball.X + ball.size >= RightPaddle.X: #checks if balls x cord is at the right position
				return True
		return False

	def BW (self,ball): #collision with the ball and any wall

		#top collision
		if ball.Y - ball.size <= 0:
			return True

		#bottem collision
		if ball.Y + ball.size >= pong_length:
			return True

		return False

	def CGL(self,ball):#checks if left player got a goal 
		return ball.X - ball.size >=pong_width
	
	def CGR(self,ball):#checks if right player got a goal
		return ball.X + ball.size <= 0 

#OOP--------------------------------

pong_width = 900 
pong_length = 500 
Acolor = (0,0,0) #Black
Bcolor = (255,255,255)#white

def run(player):
	pygame.init()

	clock = pygame.time.Clock()#adds FPS variable which allows us to set the fps




	screen = pygame.display.set_mode((pong_width,pong_length)) #sets the display size
	pygame.display.set_caption("Pong") #set the window name to pong

	def screen_color():#set the background black and adds a white line in the middle
		screen.fill(Acolor)#makes the color of the screen what 'Acolor' is 
		pygame.draw.line(screen, Bcolor, (pong_width/2,0), (pong_width/2, pong_length),5 )#makes a 'Bcolor' line in the middle of the window
	screen_color() #calls the function

	#------------------------------------Objects------------------------------------#
	#--------------Ball and Paddle set parameters Objects--------------#
	ball = Ball(screen, Bcolor, pong_width/2, pong_length/2, 10) #sets the ball parameters 
	LeftPaddle = Paddle(screen, Bcolor, 10, pong_length/2 - 60, 20, 120)#sets the left Paddle parameters 
	RightPaddle = Paddle(screen, Bcolor, pong_width-20-10, pong_length/2-60, 20, 120)#sets the right Paddle parameters 
	collision = Collision_management()
	Leftscore = Score (screen,"0",pong_width/4, 15)
	Rightscore = Score (screen,"0",pong_width - pong_width/4, 15)
	player.get_bet()
	player2=balance.User("Player 2, ")
	player2.get_bet()
	Info_start = Info (screen,"Press P to Start",pong_width/2, pong_length/2)
	name_Left = Info (screen,player.name,pong_width/4, pong_length-100)
	name_Right = Info (screen,player2.name,pong_width - pong_width/4, pong_length-100)
	Info_Left = Info (screen,"W/S  P1",pong_width/4, pong_length-50)
	Info_Right = Info (screen,"↑/↓  P2",pong_width - pong_width/4, pong_length-50)
	#-------------------------------------------------------------------------------#
	rounds=" "
	
	while (not(rounds.isnumeric() or balance.is_number(rounds))) or ((rounds.isnumeric() or balance.is_number(rounds)) and int(rounds)<=0):#runs this code while the user's bet is larger than what they actually have or if their bet is not a real number
		rounds=input(str(player.name)+", First to how many points wins? " )#asks the user for their bet
		os.system("clear")#clears the screen
	#FInds the ammount of rounds -------------------------------------------------------
		

	playing = False

	#----------Main Loop----------#
	while True:
		pygame.display.flip()#draws the game
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				sys.exit()#if the exit button is clicked, end 

				
			if event.type == pygame.KEYDOWN:#checks to see if player pushed down a key
				
				if event.key == pygame.K_p: 
					ball.start()
					playing = True
		

				#Movement for Left Paddle
				if event.key == pygame.K_w:#if user inputs W
					LeftPaddle.state = 1
				
				if event.key == pygame.K_s:#if user inputs S
					LeftPaddle.state = 2

				#Movement for Right Paddle
				if event.key == pygame.K_UP:#if user inputs the up arrow
					RightPaddle.state = 1
				
				if event.key == pygame.K_DOWN:#if user inputs the down arrow
					RightPaddle.state = 2
			
			if event.type == pygame.KEYUP:#if player isnt using inputs the paddles will stop moving
				LeftPaddle.state = 0
				RightPaddle.state = 0
		
		if playing:
			screen_color()

			#ball
			ball.move()
			ball.display()#displays the ball

			#LeftPaddle
			LeftPaddle.move()
			LeftPaddle.collision()
			LeftPaddle.display()#displays the left Paddle
			#RightPaddle
			RightPaddle.move()
			RightPaddle.collision()
			RightPaddle.display()#displays the right paddles

			#---------------Checking for Collisions---------------#
			if collision.LPB(ball, LeftPaddle):#collision with left paddle and ball
				ball.paddlecollision()

			if collision.RPB(ball, RightPaddle):#collision with right paddle and ball
				ball.paddlecollision()
			
			if collision.BW(ball):#collision with ball and wall
				ball.wallcollision()

			if collision.CGL(ball):#collision with the ball and the right side of the window
				LeftPaddle.Reset()
				RightPaddle.Reset()
				Leftscore.score()
				ball.Reset_Left()

			if collision.CGR(ball):#collision with the ball and the left side of the window
				LeftPaddle.Reset()
				RightPaddle.Reset()
				Rightscore.score()
				ball.Reset_Right()
		
		else:
			Info_start.show()
			
		Leftscore.show()#shows score of the left paddle player
		Rightscore.show()#shows score of the right paddle player
		name_Left.show()
		name_Right.show()
		Info_Left.show()#shows score of the left paddle player
		Info_Right.show()#shows score of the right paddle player
		
		clock.tick(16)#Max FPS so the speed of everything doesnt freakout
		pygame.display.update()#updates the screen

		if Leftscore.points == rounds:
			player.updateBal(2)
			player2.updateBal(0)
			print(player.name,"Wins!")
		
		elif Rightscore.points == rounds:
			player.updateBal(0)
			player2.updateBal(2)
			print(player2.name,"Wins!")
		
		if Leftscore.points == rounds or Rightscore.points == rounds:
			player.display_bal()
			player2.display_bal()
			input("press enter to continue")
			return


