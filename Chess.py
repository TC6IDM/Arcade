# Authors: Andrew Tissi
# Date: Created: 4/1/21
# Description: Plays a game of chess against another user or against my own chess bot

def run(player):
	'''chess'''	
	import pygame#imports the pygame Library
	import time#imports the time Library
	import board#imports the board Library
	import moves#imports the moves Library
	import config#imports the config Library
	import math#imports the math Library
	import check#imports the check Library
	import copy#imports the copy Library
	import convert#imports the convert Library
	import os#imports the os Library
	import balance#imports the balanceLibrary
	from datetime import datetime#imports datetime from the datetime Library
	from pytz import timezone#imports timezone from the pytx Library
	import PGN#imports the PGN Library
	import ai#imports the AI Library
	
	pygame.init()#starts up pygame
	clock = pygame.time.Clock()#creates a clock for the pygame
	chessStart=""#creates a variable to hold the starting color
	chessMode=""#creates a variable to hold the game move
	chessDiff=""#creates a varuable to hold the game difficulty
	width, height = 480, 480#dimensions
	config.screen=pygame.display.set_mode((width, height))#makes the screen
	config.start=""#player 1's choice, appears at the bottom, either black or white
	config.mode=""#against a computer or against another player
 
	board.displayScreen(config.chessboard_white)#displays a default board
	pygame.display.flip()#draws the game	
	os.system('clear')#clears the screen
	print("Welcome To Chess!\n")#prints a welcome message
	#let the user decide what side
	
	while chessStart.lower() !="white" and  chessStart.lower() !="black":#runs untill the user picks white or black
		chessStart=str(input(player.name+', Would you like to play as "White" or "Black"?:\n')).lower()#asks the user what they want to play as
		os.system('clear')#clears the screen
	
	while chessMode.lower() !="computer" and  chessMode.lower() !="player":#runs untill the user picks computer or player
		chessMode=str(input(player.name+', Would you like to play against the "Computer" or another "Player":\n')).lower()#asks the user if they want to play as computer or player
		os.system('clear')#clears the screen
	
	if chessMode =="computer":#checks if the user wants to play against the computer
		
		while chessDiff.lower() !="easy" and  chessDiff.lower() !="hard":#runs untill the user picks easy or hard
			chessDiff=str(input(player.name+', Would you like to play on "Easy" mode or "Hard" mode:\nWarning: Hard mode causes the computer to think more before each move \nand each move will take longer for the computer to preform.\nHowever, you get a 4x multiplier if you win\n')).lower()#asks the user if they want to play hard mode or easy mode
			os.system('clear')#clears the screen
	config.start=chessStart#sets the start color
	config.mode=chessMode#sets the mode
	config.diff=chessDiff#sets the difficulty
	#creates the chessboards
	
	if config.start=="white":#checks if the user wants to start as white
		chessBoard=copy.deepcopy(config.chessboard_white)#uses the white chess board
	
	else:#user starts as black
		chessBoard=copy.deepcopy(config.chessboard_black)#uses the black chess board
	user1=0#sets user 1 to 0
	user2=0#sets user 2 to 0
	#asks the user for their names
	
	if config.mode=="computer":#computer is playing
		
		if config.start=="white":#user is playing as white
			user1=player#creates a user object
			white=user1.name#finds the user's name
			user1.color="white"#sets this user's color to white
			os.system('clear')#clears the screen
			black="Tissi_Bot"#sets black's name
			user1.get_bet()#gets this user's bet
		
		else:#user is playing as black
			white="Tissi_Bot"#sets white's name
			user1=player#creates a user object
			black=user1.name#finds the user's name
			user1.color="black"#sets this user's color to black
			os.system('clear')#clears the screen
			user1.get_bet()#gets this user's bet

	else:
		
		if config.start=="white":#user is playing as white
			user1=player#creates a user object
			white=user1.name#finds the user's name
			user1.color="white"#sets this user's color to white
			os.system('clear')#clears the screen
			user1.get_bet()#gets this user's bet
			user2=balance.User("Black, ")#creates a user object
			black=user2.name#finds the user's name
			user2.color="black"#sets this user's color to black
			user2.get_bet()#gets this user's bet
		
		else:
			user2=player#creates a user object
			black=user2.name#finds the user's name
			user2.color="black"#sets this user's color to black
			os.system('clear')#clears the screen
			user2.get_bet()#gets this user's bet
			user1=balance.User("White, ")#creates a user object
			white=user1.name#finds the user's name
			user1.color="white"#sets this user's color to white
			user1.get_bet()#gets this user's bet

	
	print("Enjoy The Game!")#tells the user to enjoy the game
	tz = timezone('America/New_York')#sets the timezone
	x=datetime.now(tz) #creates a time based on the given timezone
	#creates the header for PGN notation

	#Arrays/Lists--------------------------------

	PGN_List=[
			'[Event "Pygame Chess"]',
			'[Site "https://replit.com/@pogboys/chess"]',
			'[Date "'+x.strftime("%Y")+'.'+x.strftime("%m")+'.'+x.strftime("%d")+'"]',
			'[Round "?"]',
			'[White "'+white+'"]',
			'[Black "'+black+'"]',
			'[Result "*"]',
			'',
			''
			]

	#starts up most variables
	mouse2=False#sets mouse 2 to false
	verifiedMoves=[]#creates a list called verifiedMoves
	castleGame=[]#creates a list called castleGame
	takesAndPawnMoves=[]#creates a list called takesAndPawnMoves
	nextmove="W"#sets white to the first move
	checkmate=False#sets checkmate to false
	stalemate=False#sets stalemate to false
	draw=False#sets draw to false
	fullgame=[]#creates a list called fullgame
	allGameStates=[]#creates a list called allGameStates

	#Arrays/Lists--------------------------------

	move=1#sets the move to move 1
	board.displayScreen(chessBoard)	#displays the board
	allGameStates.append(copy.deepcopy(chessBoard))#adds this gamestate to a total list
	pygame.event.clear()#clears the buffered events in pygame.event
	

	#runs the game if the game is on
	
	while checkmate==False and stalemate==False and draw==False:
		#computer move
		pygame.display.flip()#draws the game
		if (nextmove.lower()!=config.start[0].lower()) and config.mode.lower()=="computer":#checks if this move is the computer's move
			PGN_List,move,takesAndPawnMoves,chessBoard,fullgame,castleGame,allGameStates,nextmove,checkmate,stalemate,draw = ai.computerMove(chessBoard,nextmove,castleGame,PGN_List,move,takesAndPawnMoves,fullgame,allGameStates)#gets the computer's move


		
		for event in pygame.event.get():#sees whenever anything happens (including mouse movement)
			mouse1=pygame.mouse.get_pressed()[0]#finds if the mouse is clicked or not
			xPixles=pygame.mouse.get_pos()[0]#gets the x coordinate of the mouse position
			yPixles=pygame.mouse.get_pos()[1]#gets the y coordinate of the mouse position
			
			if mouse1==True and mouse2==False:#mouse down
				mouse2=pygame.mouse.get_pressed()[0]#sets mouse 2 to clicked
				ySquare1 = math.floor(yPixles/config.square)#converts from pixels to squares for x
				xSquare1 = math.floor(xPixles/config.square)#converts from pixels to squares for y

				if chessBoard[ySquare1][xSquare1]!=0:#checks if the user is clicking on a piece

					totalMoves=moves.findVerifiedMoves(chessBoard,nextmove)#finds all the moves
					circleList=[]#stores all the positions of where circles needs to be drawn
					verifiedMoves=[]#stores all the verified moves
					
					for i in totalMoves:#loops through all the moves
						
						if i[1]==str(ySquare1) and i[2]==str(xSquare1):#checks if this specific move relates to the current piece
							verifiedMoves.append(i)#adds this move to the verified moves
							circleList.append(convert.findBoardNumber(i[-2],i[-1]))#adds the position to draw the circle in

					#castling (only for circles)
					
					if (chessBoard[ySquare1][xSquare1][1:2]=="K" and chessBoard[ySquare1][xSquare1][0:1]==nextmove):#checks if the user is holding a king
						castleX="no"#holds the x position of the castle
						
						if nextmove+"Q" in moves.canCastle (chessBoard,castleGame):#checks if there can be a queen side castle
							
							if config.start=="white":#checks if the user is on white
								#----------------queen side castle with white----------------
								castleX="2"#x position of the castle is 2
								
								if nextmove=="W":#checks if the next move is white's move
									castleY="7"#castle on the 8th rank
								
								else:#checks if the next move is black's move
									castleY="0"#castle on the 1st rank
							
							else:#checks if the user is on black
								#----------------queen side castle with black----------------
								castleX="5"#x position of the castle is 5
								
								if nextmove=="W":#checks if the next move is white's move
									castleY="0"#castle on the 1st rank
								
								else:#checks if the next move is black's move
									castleY="7"#castle on the 8th rank
						
						if castleX!='no':#runs this if there is a way to castle
							circleList.append(castleX+castleY)#adds the circle to be drawn

						castleX="no"#holds the x position of the castle
						
						if nextmove+"K" in moves.canCastle (chessBoard,castleGame):#checks if there can be a king side castle
							
							if config.start=="white":#checks if the user is on white
								#----------------king side castle with white----------------
								castleX="6"#x position of the castle is 6
								
								if nextmove=="W":#checks if the next move is white's move
									castleY="7"#castle on the 8th rank
								
								else:#checks if the next move is black's move
									castleY="0"#castle on the 1st rank
							
							else:#checks if the user is on black
								#----------------king side castle with black----------------
								castleX="1"#x position of the castle is 1
								
								if nextmove=="W":#checks if the next move is white's move
									castleY="0"#castle on the 1st rank
								
								else:#checks if the next move is black's move
									castleY="7"#castle on the 8th rank
						
						if castleX!='no':#runs this if there is a way to castle
							circleList.append(castleX+castleY)#adds the circle to be drawn
					#en passant
					
					if len(fullgame)>=1:#checks if more than one game has been played
						numbers=convert.findBoardNumber(fullgame[-1][-2],fullgame[-1][-1])#finds the last move
						left=0#sets left to 0
						right=0#sets right to 0
						epY="no"#sets epY to no
						epX="no"#sets epX to no
						pawnX=100#sets pawnX to 0
						pawnY=100#sets pawnY to 0
						#en passant-able
						#run this code when a bottom pawn moves 2 up
						
						if numbers[1]=="4" and fullgame[-1][1]=="6" and fullgame[-1][-3]=="P":#checks if the last move was a pawn from rank 2 to 3
							epY="5"#sets the y value of the en passant to 5
							pawnY=numbers[1]#finds the y value of the recently moved pawn
							epX=int(numbers[0])#finds the x value of the recently moved pawn
							#en passant on left side
							
							if int(numbers[0])-1>=0 and int(numbers[0])-1<=7:#checks if the position to the left is on the board
								left=chessBoard[int(numbers[1])][int(numbers[0])-1]#finds the piece at the left side of the recently moved pawn
							#en passant on right side
							
							if int(numbers[0])+1>=0 and int(numbers[0])+1<=7:#checks if the position on the right is on the board
								right=chessBoard[int(numbers[1])][int(numbers[0])+1]#finds the piece at the right side of the recently moved pawn
							#checks if the piece is a pawn
							
							if left==nextmove+"P":#checks if the piece on the left side is the opposing player's pawn
								pawnX=int(numbers[0])-1#sets the pawn's x value to the left
							
							elif right==nextmove+"P":#checks if the piece on the right side is the opposing player's pawn
								pawnX=int(numbers[0])+1#sets the pawn's x value to the right
						#run this code when a top pawn moves 2 down
						
						if numbers[1]=="3" and fullgame[-1][1]=="1" and fullgame[-1][-3]=="P":#checks if the last move was a pawn from rank 7 to 5
							epY="2"#sets the y value of the en passant to 2
							pawnY=numbers[1]#finds the y value of the recently moved pawn
							epX=int(numbers[0])#finds the x value of the recently moved pawn
							#en passant on left side
							
							if int(numbers[0])-1>=0 and int(numbers[0])-1<=7:#checks if the position to the left is on the board
								left=chessBoard[int(numbers[1])][int(numbers[0])-1]#finds the piece at the left side of the recently moved pawn
							#en passant on right side
							
							if int(numbers[0])+1>=0 and int(numbers[0])+1<=7:#checks if the position on the right is on the board
								right=chessBoard[int(numbers[1])][int(numbers[0])+1]#finds the piece at the right side of the recently moved pawn
							#checks if the piece is a pawn
							
							if left==nextmove+"P":#checks if the piece on the left side is the opposing player's pawn
								pawnX=int(numbers[0])-1#sets the pawn's x value to the left
							
							elif right==nextmove+"P":#checks if the piece on the right side is the opposing player's pawn
								pawnX=int(numbers[0])+1#sets the pawn's x value to the right
						
						if (xSquare1==int(pawnX) and ySquare1==int(pawnY)):#checks if en passant is possible
							circleList.append(str(epX)+str(epY))#adds the en passant to the circle list

					board.printAllCircles(circleList)#prints the circles

			elif mouse1==False and mouse2==True:#checks if the mose has been released
				promotestring=''#creates the promotion string
				ySquare2 = math.floor(yPixles/config.square)#gets the y coordinate of the mouse position
				xSquare2 = math.floor(xPixles/config.square)#gets the x coordinate of the mouse position
				mouse2=pygame.mouse.get_pressed()[0]#sets mouse 2 to the current mouse's activity
				newMoveString=""#creates a giant string with letters and numbers of where you can move
				
				for l in verifiedMoves:#loops through all the verified moves
					newMoveString= newMoveString+l[-2:]#adds the chess number of the move to the string
				#checks if the piece can move here
				
				if convert.findChessNumber(xSquare2,ySquare2) in newMoveString and chessBoard[ySquare1][xSquare1][0:1]==nextmove:#checks if this piece can make a move to the designated square
					#pawn promotion again
					
					if nextmove=="W":#checks if it's white's turn
						PGN_List[8]=PGN_List[8]+str(move)+". "#adds a number to the PGN list
						move+=1#increments the move

					#checks for taking or pawn moving (for 50 move rule)
					
					if (chessBoard[ySquare2][xSquare2]!=0 or chessBoard[ySquare1][xSquare1][1:2]=="P"):#checks if there was either a take or a pawn was moved
						takesAndPawnMoves.append(0)#appends a 0 to this list
					
					else:
						takesAndPawnMoves.append(1)#appends a 1 to this list

					if chessBoard[ySquare1][xSquare1][1:2]=="P":#checks if the move was a pawn
						
						if ySquare2==0 or ySquare2==7:#checks if the pawn is on the 1st or 8th rank and is supposed to promote
							promoteTo="hi"#creates the promote string
							#nqrb means Night Queen Rook Bishop
							
							while promoteTo not in "nqrb":#runs this code untill the user types either n q r or b
								os.system('clear')#clears the screen
								promoteTo = input("what would you like to promote your pawn to?\nNight: (N), Queen: (Q), Rook: (R), Bishop: (B)").lower()#asks the user what they would like to promote to
								os.system('clear')#clears the screen
								PGN.printMoves(PGN_List[8])#prints the moves
								#promote the pawn
								promotestring="="+promoteTo#gets the PGN notation of this promotion
								PGN_List[8]=PGN_List[8]+PGN.PGNADD(xSquare1,xSquare2,ySquare1,ySquare2,chessBoard,nextmove)[:-1]+promotestring.upper()+" "#adds this move to to the PGN string
								os.system('clear')#clears the screen
								PGN.printMoves(PGN_List[8])#prints all the PGN moves
								chessBoard[ySquare1][xSquare1]=nextmove+promoteTo.upper()#sets the piece on the board to the promoted piece
					
					if len(promotestring)!=2:#checks if there was not a promotion
						PGN_List[8]=PGN_List[8]+PGN.PGNADD(xSquare1,xSquare2,ySquare1,ySquare2,chessBoard,nextmove)#adds the move to the PGN string
						os.system('clear')#clears the screen
						PGN.printMoves(PGN_List[8])#prints all the PGN moves
					#sets the new chessboard
					chessBoard[ySquare2][xSquare2]=chessBoard[ySquare1][xSquare1]#moves the piece
					chessBoard[ySquare1][xSquare1]=0#sets the old position of the pice to empty or 0
					
					#creates the screen
					board.displayScreen(chessBoard)#displays the board
					fullgame.append(nextmove+str(ySquare1)+str(xSquare1)+chessBoard[ySquare2][xSquare2][1]+convert.findChessNumber(xSquare2,ySquare2))#adds this move to the full game list
					castleGame.append(str(ySquare1)+str(xSquare1))#adds some values to the castleGame list
					allGameStates.append(copy.deepcopy(chessBoard))#adds this game state to the allGameStates list
					nextmove=moves.getNextMove(nextmove)#sets the next move
					checkmate=check.checkmate(chessBoard,nextmove,fullgame)#finds if there is a checkmate this turn
					
					if (check.check(chessBoard,nextmove)) and (not checkmate):#finds if there is a check this turn but no checkmate
						PGN_List[8]=PGN_List[8][:-1]+"+ "#adds a + to the end of the string to signify a check
						os.system('clear')#clears the screen
						PGN.printMoves(PGN_List[8])#prints the moves to the board
					stalemate=check.stalemate(chessBoard,nextmove,fullgame)#finds if there is a stalemate
					draw=check.draw(fullgame,takesAndPawnMoves,allGameStates,chessBoard)#checks if there is a draw this game
				
				else:#checks if this is not an immediatly valid move
					
					if chessBoard[ySquare1][xSquare1]!=0:#checks if the user is clicking on a piece
						#copys the board
						oldBoard=copy.deepcopy(chessBoard)
						#en passant
						ep=0
						chessBoard=moves.enpassant(fullgame,xSquare1,xSquare2,ySquare1,ySquare2,nextmove,chessBoard)#saves the new chessboard if the user can en passant
						
						if chessBoard!=oldBoard:#checks if the chess board has changed
							ep=1#there is an en passant
							takesAndPawnMoves.append(0)#pawn moves so append a 0
							
							if nextmove=="W":#checks if it's white's turn
								PGN_List[8]=PGN_List[8]+str(move)+". "#adds a number to the PGN list
								move+=1#increases the amount of moves
							PGN_List[8]=PGN_List[8]+convert.findChessNumber(xSquare1,ySquare1)[0]+"x"+convert.findChessNumber(xSquare2,ySquare2)+" "#adds this string to the PGN string
							os.system('clear')#clears the screen
							PGN.printMoves(PGN_List[8])#prints the PGN moves
						#castle
						chessBoard,PGNpossible=moves.castle(nextmove,chessBoard,castleGame,xSquare1,xSquare2,ySquare1,ySquare2)#saves the new chessboard if the user can castle
						
						if chessBoard!=oldBoard and ep==0:#checks if there has been no en passant and the user can castle
							takesAndPawnMoves.append(1)#no takes and no pawn moves so append a 1
							
							if nextmove=="W":#checks if it's white's turn
								PGN_List[8]=PGN_List[8]+str(move)+". "#adds a number to the PGN list
								move+=1#increases the amount of moves
							PGN_List[8]=PGN_List[8]+PGNpossible#adds the PGN move to the string
							os.system('clear')#clears the screen
							PGN.printMoves(PGN_List[8])#prints the PGN Moves
						
						if chessBoard==oldBoard:#checks if no moves can be made
							
							if str(xSquare2)+ str(ySquare2)!=str(xSquare1)+str(ySquare1) and chessBoard[ySquare1][xSquare1]!=0:#checks if the position the user is moving to is not the position they are moving from and they arent moving an empty square
								board.drawRedSquare(xSquare2,ySquare2)#prints a red box around where the move was attempted
								time.sleep(0.5)#waits for half a second
							board.displayScreen(chessBoard)#prints the board again
						
						else:#valid move
							allGameStates.append(copy.deepcopy(chessBoard))#adds this game state to the list
							board.displayScreen(chessBoard)#prints the board
							checkmate=check.checkmate(chessBoard,nextmove,fullgame)#checks if there is a checkmate this turn
							stalemate=check.stalemate(chessBoard,nextmove,fullgame)#checks if there is a stalemate this turn
							draw=check.draw(fullgame,takesAndPawnMoves,allGameStates,chessBoard)#checks if there is a draw this turn
							
							if (check.check(chessBoard,nextmove)) and (not checkmate):#if there is no checkmate but there is a check this move then execute this code
								PGN_List[8]=PGN_List[8][:-1]+"+ "#adds a + to the end of the move signifying that this move resulted in a check
								os.system('clear')#clears the screen
								PGN.printMoves(PGN_List[8])#prints the chess moves
							nextmove=moves.getNextMove(nextmove)#gets the next move
				verifiedMoves=[]#clears the verified moves array


		
		clock.tick(20)#sets the clock to run at 20

	#game over
	os.system('clear')#clears the screen
	
	if checkmate==True:#checks if there was a checkmate
		
		if nextmove=="B":#checks if the person getting checkmated was black
			winner="White"#counts white as the winner
			PGN_List[6]='[Result "1-0"]'#sets the result to white winning
			PGN_List[8]=PGN_List[8][:-1]+"# 1-0"#adds the final string to the PGN string
			
			if config.mode=="computer":#checks if the user is playing against the computer
				
				if user1.color=="white":#checks if user 1 is white
				
					if config.diff=="hard":#checks if the difficulty is hard
						user1.updateBal(4)#multiplies the user's bet by 4 and updates it in the text file
					
					else:#checks if the difficulty is easy
						user1.updateBal(2)#multiplies the user's bet by 2 and updates it in the text file
				
				else:#checks if the user is not playing as white
					user1.updateBal(0)#multiplies the user's bet by 0 and updates it in the text file
			
			else:#the user is playing against another player
				user1.updateBal(2)#multiplies the winning user's bet by 2 and updates it in the text file
				user2.updateBal(0)#multiplies the losing user's bet by 0 and updates it in the text file
		
		else:#checks if the person getting checkmated was white
			winner="Black"#counts black as the winner
			PGN_List[6]='[Result "0-1"]'#sets the result to black winning
			PGN_List[8]=PGN_List[8][:-1]+"# 0-1"#adds the final string to the PGN string
			
			if config.mode=="computer":#checks if the user is playing against the computer
				
				if user1.color=="black":#checks if user 1 is black
					
					if config.diff=="hard":#checks if the difficluty is hard
						user1.updateBal(4)#multiplies the user's bet by 4 and updates it in the text file
				
					else:#checks if the difficulty is easy
						user1.updateBal(2)#multiplies the user's bet by 2 and updates it in the text file
				
				else:#checks if the user is not playing as black
					user1.updateBal(0)#multiplies the user's bet by 0 and updates it in the text file
			
			else:#the user is playing against another player
				user1.updateBal(0)#multiplies the losing user's bet by 0 and updates it in the text file
				user2.updateBal(2)#multiplies the winning user's bet by 2 and updates it in the text file
		print("The Winner is",winner+"!")#prints the winner of the game
	
	elif stalemate==True:#checks if there was a stalemate
		print("Stalemate!")#prints that there was a stalemate
		PGN_List[6]='[Result "1/2-1/2"]'#sets the result to a draw
		PGN_List[8]=PGN_List[8]+"1/2-1/2"#adds the final string to the PGN string
	
	elif draw!=False:#checks if there was any other draw
		PGN_List[6]='[Result "1/2-1/2"]'#sets the result to a draw
		PGN_List[8]=PGN_List[8]+"1/2-1/2"#adds the final string to the PGN string
		
		if draw=="50 Move Rule":#checks for 50 Move Rule
			print("The Game has ended in a draw because of The 50 Move Rule")#prints thre reason of the game ending
		
		elif draw=="Threefold Repetition":#checks for Threefold Repetition
			print("The Game has ended in a draw because of The Threefold Repetition Rule")#prints thre reason of the game ending
		
		elif draw=="Dead Position":#checks for Dead Position
			print("The Game has ended in a draw because There is insufficient material to cause a checkmate")#prints thre reason of the game ending

	current=len(allGameStates)-1#length of the game in moves
	print("\nThank you for playing! you can now replay the game to see all your moves\n")#thanks the user for playing the game
	file="chess games/"+str(x)[:len(str(x))-6]+".txt"#sets the file destination of the games

	#files--------------------------------

	with open(file, 'w') as f:#opens the specified file as a write only
		
		for i in PGN_List:#loops through every line in PGN_List
			f.write(str(i)+"\n")#writes the current PGN_List line
		f.close()#closes the file

	#files--------------------------------	

	while True:#allows for the game to be replayed
		user_input=input('Type "b" to go back 1 step or type "f" to go forward one step\nAlternatively, type q to quit the game ')#asks the for the user's input, f goes forward one setp b goes back 1 step and q exits the game
		os.system('clear')#clears the screen
		
		if user_input.lower() =="f":#next page
			current+=1#adds 1 to the current move
		
		elif user_input.lower() =="b":#back 1 page
			current-=1#subtracts 1 from the current move
		
		elif user_input.lower() =="q":#quit game
			print("Thank You For Playing!")#thanks the user for playing
			print("A PGN notation of this game has been saved to:\n"+file+'\nyou can replay this game at any time using https://www.chess.com/analysis?\nThen pressing "Load PGN" and pasting the contents of the .txt file into there')#tells the user that the pgn notation of the game has been saved
			
			if user1!=0:#checks if there was a user 1 in this game
				user1.display_bal()#displays user 1's balence
			
			if user2!=0:#checks if there was a user 2 in this game
				user2.display_bal()#displays user 2's balence
			input("Press Enter at any time to return to the main screen")
			return#exits the game
		
		else:#runs when the user does not put in valid input
			print('you did not send a valid input')#tells the user that they did not put in a valid input
		
		if current>len(allGameStates)-1:#too far to the right loop back to 0
			current=0#sets the current position to the first position
		
		if current==-1:#too far to the left loop back to the end of the game
			current=len(allGameStates)-1#sets the current position to the last position
		board.displayScreen(allGameStates[current])#prints the current board state
		pygame.display.flip()#draws the game

