# Authors: Andrew Tissi
# Date: Created: 4/1/21
# Description: does stuff for the computer's move

import moves#imports the moves Library
import config#imports the config Library
import os#imports the os Library
import PGN#imports the PGN Library
import convert#imports the convert Library
import random#imports the random Library
import copy#imports the copy Library
import board#imports the board Library
import check#imports the check Library

#Functions--------------------------------

def computerMove(chessBoard,nextmove,castleGame,PGN_List,move,takesAndPawnMoves,fullgame,allGameStates):
	"""Does the computer's turn"""
	promotestring=''#creates an empty string to store the promoted piece
	computerMoves=moves.findVerifiedMoves(chessBoard,nextmove)#finds all the moves the computer can do
	computerMoves2=copy.deepcopy(computerMoves)#creates a copy of the computer's moves

	if nextmove+"Q" in moves.canCastle (chessBoard,castleGame):#checks if the computer can castle

		if config.start=="black":#checks if the user is black (computer is white)
			PGN_List[8]=PGN_List[8]+str(move)+". "#adds a number to the PGN notation
			move+=1#increments the move

		if config.start=="white":#checks if the user is on the white side
			#castle queen side white
			chessBoard[0][2]="BK"#king to c8
			chessBoard[0][3]="BR"#rook to d8
			#sets old positions to empty
			chessBoard[0][0]=0
			chessBoard[0][4]=0
			takesAndPawnMoves.append(1)#not a pawn move or take so appends a 1
			PGN_List[8]=PGN_List[8]+"O-O-O "#adds the queen side castle symbol to the PGN list
			os.system('clear')#clears the screen
			PGN.printMoves(PGN_List[8])#prints all the moves

		else:#checks if the user is on the black side
			#castle queen side black
			chessBoard[0][5]="WK"#king to f8
			chessBoard[0][4]="WR"#rook to e8
			#sets old positions to empty
			chessBoard[0][7]=0
			chessBoard[0][3]=0
			takesAndPawnMoves.append(1)#not a pawn move or take so appends a 1
			PGN_List[8]=PGN_List[8]+"O-O-O "#adds the queen side castle symbol to the PGN list
			os.system('clear')#clears the screen
			PGN.printMoves(PGN_List[8])#prints all the moves

	elif nextmove+"K" in moves.canCastle (chessBoard,castleGame):

		if config.start=="black":#checks if the user is on the black side
			PGN_List[8]=PGN_List[8]+str(move)+". "#adds a number to the PGN notation
			move+=1#increments the move

		if config.start=="white":#checks if the user is on the white side
			#castle king side white
			chessBoard[0][6]="BK"#king to g8
			chessBoard[0][5]="BR"#rook to f8
			#sets old positions to empty
			chessBoard[0][7]=0
			chessBoard[0][4]=0
			takesAndPawnMoves.append(1)#not a pawn move or take so appends a 1
			PGN_List[8]=PGN_List[8]+"O-O "#adds the king side castle symbol to the PGN list
			os.system('clear')#clears the screen
			PGN.printMoves(PGN_List[8])#prints all the moves

		else:#checks if the user is on the black side
			#castle king side black
			chessBoard[0][1]="WK"#king to b1
			chessBoard[0][2]="WR"#rook to c1
			#sets old positions to empty
			chessBoard[0][0]=0
			chessBoard[0][3]=0
			takesAndPawnMoves.append(1)#not a pawn move or take so appends a 1
			PGN_List[8]=PGN_List[8]+"O-O "#adds the king side castle symbol to the PGN list
			os.system('clear')#clears the screen
			PGN.printMoves(PGN_List[8])#prints all the moves

	else:
		enpassant=0#sets en passant to 0
		#enpassant

		if len(fullgame)>=1:#makes sure there has been at least 1 move
			numbers=convert.findBoardNumber(fullgame[-1][-2],fullgame[-1][-1])#finds the board number of the last move
			left=0#sets left to 0
			right=0#sets right to 0
			#en passant-able

			if numbers[1]=="4" and fullgame[-1][1]=="6" and fullgame[-1][-3]=="P":#since the computer is always on the top, it will check if the last move was the user moving their pawn from the 2nd rank to the 4th

				if int(numbers[0])-1>=0 and int(numbers[0])-1<=7:#makes sure there is a position to the left of where the user moved
					left=chessBoard[int(numbers[1])][int(numbers[0])-1]#gets the piece which was to the left of where the user moves

				if int(numbers[0])+1>=0 and int(numbers[0])+1<=7:#makes sure there is a position to the right of where the user moved
					right=chessBoard[int(numbers[1])][int(numbers[0])+1]#gets the piece which was to the right of where the user moves

				if left==nextmove+"P":#checks if the piece to the left is an opponent's pawn

					if config.start=="black":#checks if the user is on the black side
						PGN_List[8]=PGN_List[8]+str(move)+". "#adds a number to the PGN notation
						move+=1#increments the move
					#en passant left
					chessBoard[int(numbers[1])+1][int(numbers[0])]=chessBoard[int(numbers[1])][int(numbers[0])-1]#sets the piece below the user's pawn to the computer's pawn
					chessBoard[int(numbers[1])][int(numbers[0])-1]=0#removes the computer's old pawn
					chessBoard[int(numbers[1])][int(numbers[0])]=0#sets the user's pawn to empty or taken
					PGN_List[8]=PGN_List[8]+convert.findChessNumber(int(numbers[0])-1,int(numbers[1]))[0]+"x"+convert.findChessNumber(int(numbers[0]),int(numbers[1])+1)+" "#adds the current move into the PGN list
					os.system('clear')#clears the screen
					PGN.printMoves(PGN_List[8])#prints the moves
					takesAndPawnMoves.append(0)#counts as a pawn move so appends a 0
					enpassant=1#indicates that there was an en passant
					
				elif right==nextmove+"P":#checks if the piece to the right is an opponent's pawn

					if config.start=="black":#checks if the user is on the black side
						PGN_List[8]=PGN_List[8]+str(move)+". "#adds a number to the PGN notation
						move+=1#increments the move
					#en passant right
					chessBoard[int(numbers[1])+1][int(numbers[0])]=chessBoard[int(numbers[1])][int(numbers[0])+1]#sets the piece below the user's pawn to the computer's pawn
					chessBoard[int(numbers[1])][int(numbers[0])+1]=0#removes the computer's old pawn
					chessBoard[int(numbers[1])][int(numbers[0])]=0#sets the user's pawn to empty or taken
					PGN_List[8]=PGN_List[8]+convert.findChessNumber(int(numbers[0])+1,int(numbers[1]))[0]+"x"+convert.findChessNumber(int(numbers[0]),int(numbers[1])+1)+" "#adds the current move into the PGN list
					os.system('clear')#clears the screen
					PGN.printMoves(PGN_List[8])#prints the moves
					takesAndPawnMoves.append(0)#counts as a pawn move so appends a 0
					enpassant=1#indicates that there was an en passant
		
		if enpassant==0:#checks if the computer did not en passant
			goodMoves=[]#creates a list that will contain the good moves
			stalemateMoves=[]#creates a list that will contain the stalemate moves
			gain=0#sets the gain to 0
			#find moves where the computer takes
			fiftyfifty=1#sets 50/50 to 1

			if len(check.countPieces(chessBoard))<=10:#checks if there are more than or equal to 10 pieces on the board

				#random--------------------------------

				fiftyfifty=random.randint(0,1)#sets 50/50 to a random integer from 0 to 1

				#random--------------------------------

			for thismove in range(len(computerMoves)):#loops through all the possible computer moves
				os.system('clear')#clears the console
				print("Move Loading...")#prints that the move is loading
				print("["+("▓"*(thismove+1))+(" "*(len(computerMoves)-(thismove+1)))+"]")#prints a loading bar for the current move
				currentmove=computerMoves[thismove]#finds the current move it is looking through
				moveTo=convert.findBoardNumber(currentmove[-2],currentmove[-1])#gets where the move is going
				moveFrom=currentmove[1] + currentmove[2]#gets where the move is coming from

				if config.diff=="hard":#checks if the user is in hard mode
					futureBoard=copy.deepcopy(chessBoard)#creates a copy of the chessboard
					futureBoard[int(moveTo[1])][int(moveTo[0])]=futureBoard[int(moveFrom[0])][int(moveFrom[1])]#preforms the current move
					futureBoard[int(moveFrom[0])][int(moveFrom[1])]=0#replaces the old piece with a 0

					if futureBoard[int(moveTo[1])][int(moveTo[0])][1:2]=="P":#checks if the piece is a pawn

						if int(moveTo[1])==7:#checks if the pawn can move to the bottom rank
							goodMoves.append([currentmove,9])#adds this move to the goodmoves list with a value of 9
							break

						elif int(moveTo[1])==6:#checks if the pawn can move to the second bottom rank
							goodMoves.append([currentmove,3])#adds this move to the goodmoves list with a value of 3

						elif int(moveTo[1])==5:#checks if the pawn can move to the third bottom rank
							goodMoves.append([currentmove,0.5])#adds this move to the goodmoves list with a value of 0.5
					new_check_bool=check_bool=check.check(futureBoard,moves.getNextMove(nextmove))#finds if there is a check in this position
					totalMoves=moves.findVerifiedMoves(futureBoard,moves.getNextMove(nextmove))#gets the total moves in this position

					for c in totalMoves:#loops through all the moves
						
						if "x"+futureBoard[int(moveTo[1])][int(moveTo[0])]+convert.findChessNumber(int(moveTo[0]),int(moveTo[1])) in c:#checks if the piece gets traded after this move
							
							if new_check_bool:#checks if new_check_bool is true
								new_check_bool=False#sets new_check_bool to false

					stalemate_bool=check.stalemate(futureBoard,moves.getNextMove(nextmove),fullgame)#checks if there is a stalemate in this position
					checkmake_bool = True if (check_bool and stalemate_bool) else False#checks if there is a chekcmate in this position
				
				else:#checks if the user wants easy mode
					check_bool=False#sets check to false
					stalemate_bool=False#sets stalemate to false
					checkmake_bool = False#sets checkmate to false
					new_check_bool=False#sets new check to false
				
				if checkmake_bool:#checks if there is a checkmate
					gain=9999999999999#sets the gain very high
					goodMoves.append([currentmove,gain])#adds this move to the goodmoves list with a very high value
					break#breaks the for loop since there wont be any better moves
				
				elif new_check_bool:#checks if there is a new check 
					
					if fiftyfifty:#checks if there is a 50/50
						gain=2#sets the gain to 2
						goodMoves.append([currentmove,gain])#adds this move to the goodmoves list with a value of 2
				
				elif check_bool:#checks if there is a normal check
					pass#does nothing
				
				if "x" in currentmove:#checks if this specific move is a move where a piece is taken
					trade=0#sets trade to 0
					
					if config.diff=="hard":#checks if the user is in hard mode
						futureBoard=copy.deepcopy(chessBoard)#copys the chessboard
						futureBoard[int(moveTo[1])][int(moveTo[0])]=futureBoard[int(moveFrom[0])][int(moveFrom[1])]#sets the new move
						futureBoard[int(moveFrom[0])][int(moveFrom[1])]=0#sets the old position to 0
						totalMoves=moves.findVerifiedMoves(futureBoard,moves.getNextMove(nextmove))#finds all the moves
						
						for c in totalMoves:#loops through all the moves
							gain=0#sets the gain to 0
							
							if "x"+futureBoard[int(moveTo[1])][int(moveTo[0])]+convert.findChessNumber(int(moveTo[0]),int(moveTo[1])) in c:#checks if the piece is traded out
								trade=1#sets trade to 1
						
						if trade==0:#if there is no trade
							gain=config.values[currentmove[6]]#sets the gain to the value of the piece
							goodMoves.append([currentmove,gain])#sets the move with the gain
							
							if gain>=9:#checks if the gain is greater than or equal to 9
								break#exits the for loop
					
					simplegain=config.values[currentmove[6]]-config.values[currentmove[3]]#calculates a simple gain, meaning the value of the opponents' piece minus the value of the computer's piece
					
					appenders=True#sets appenders to true
					
					for j in range(len(goodMoves)):#loops through all the good moves
						
						if currentmove in goodMoves[j]:#checks if this move is in the good moves
							appenders=False#sets appenders to 0


					
					if (simplegain>=0 and appenders) or config.diff=="easy":#checks if the gain is positive and the computer will benefit from this take
						goodMoves.append([currentmove,simplegain])#appends the move to the goodmoves list
						
						if simplegain>=6:#checks if the simplegain is greater than or equal to 6
							break#exits the for loop
				
				if stalemate_bool:#checks if there is a stalemate
					
					if not(check_bool):#checks if there is no check
						stalemateMoves.append(currentmove)#adds this move to the stalemate moves
						

			#finds the best bang for buck	move

			#random--------------------------------

			random.shuffle(goodMoves)#shuffles the moves

			#random--------------------------------

			goodMoves_pop=[]#adds a list of moves to remove
			goodMoves=sorted(goodMoves,key=lambda l:l[1], reverse=True)#sorts the moves from greatest value to lowest 
			
			for k in range(len(goodMoves)):#loops through all the moves
				
				if goodMoves[k][0] in stalemateMoves:#checks if this move will cause a stalemate
					goodMoves_pop.append(goodMoves[k])#adds this move to the pop moves
			goodMoves = [element for element in goodMoves if element not in goodMoves_pop]#removes all the pop moves from the good moves
			
			if len(goodMoves)>=1:#checks if there is more than 1 good move
				nowmove=goodMoves[0][0]#uses the most valuable move
			
			else:#no benefical moves
				#picks random move
				pop_out1=[]#creates a list to pop out moves
				pop_out2=[]#creates a list to pop out moves
				
				if config.diff=="hard":#checks if the user is on hard mode

					newermoves=copy.deepcopy(computerMoves)#cops all the computer's moves
					
					for currentmove in range(len(newermoves)):#loops through all the moves
						
						if newermoves[currentmove] in stalemateMoves:#checks if this move is a stalemate move
							pop_out2.append(newermoves[currentmove])#adds this move to the pop_out list

					evennewermoves=copy.deepcopy(newermoves)#cops the moves again
					
					for currentmove in range(len(evennewermoves)):#loops through all the moves
						moveTo=convert.findBoardNumber(evennewermoves[currentmove][-2],evennewermoves[currentmove][-1])#finds where the move is going to
						moveFrom=evennewermoves[currentmove][1] + evennewermoves[currentmove][2]#finds where the move is coming from
						futureBoard=copy.deepcopy(chessBoard)#makes a copy of the future chess board
						futureBoard[int(moveTo[1])][int(moveTo[0])]=futureBoard[int(moveFrom[0])][int(moveFrom[1])]#sets the new move on the board
						futureBoard[int(moveFrom[0])][int(moveFrom[1])]=0#sets the old positon of the board to 0
						totalMoves=moves.findVerifiedMoves(futureBoard,moves.getNextMove(nextmove))#finds all the new moves
						
						for c in totalMoves:#loops through all the moves
							
							if "x"+futureBoard[int(moveTo[1])][int(moveTo[0])]+convert.findChessNumber(int(moveTo[0]),int(moveTo[1])) in c:#checks if the piece is getting traided in this move
								pop_out1.append(evennewermoves[currentmove])#adds this move to the pop_out list

					evennewermoves = [element for element in evennewermoves if element not in pop_out1]#removes all the bad moves from this list
					newermoves = [element for element in newermoves if element not in pop_out2]#removes all the bad moves from this list
					evennewermoves = [element for element in evennewermoves if element not in stalemateMoves]#removes all the bad moves from this list
					newermoves = [element for element in newermoves if element not in stalemateMoves]#removes all the bad moves from this list
					computerMoves = [element for element in computerMoves if element not in stalemateMoves]#removes all the bad moves from this list
					
					if len(evennewermoves)>=1:#checks if there is at least one move in this list

						#random--------------------------------

						nowmove=evennewermoves[random.randint(0,len(evennewermoves)-1)]#picks a random move from this list

						#random--------------------------------

					elif len(newermoves)>=1:#checks if there is at least one move in this list

						#random--------------------------------
						
						nowmove=newermoves[random.randint(0,len(newermoves)-1)]#picks a random move from this list

						#random--------------------------------

					elif len(computerMoves)>=1:#checks if there is at least one move in this list

						#random--------------------------------

						nowmove=computerMoves[random.randint(0,len(computerMoves)-1)]#picks a random move from this list

						#random--------------------------------

					else:

						#random--------------------------------

						nowmove=computerMoves2[random.randint(0,len(computerMoves2)-1)]#gets a random move

						#random--------------------------------

				else:

					#random--------------------------------

					nowmove=computerMoves[random.randint(0,len(computerMoves)-1)]#gets a random move

					#random--------------------------------
					
			#adds to running totals
			fullgame.append(nowmove[:3]+nowmove[-3:])
			castleGame.append(nowmove[1:3])
			#finds where the pieces are moving to and from
			moveTo=convert.findBoardNumber(nowmove[-2],nowmove[-1])
			moveFrom=nowmove[1] + nowmove[2]
			#pawn promotion
			
			if chessBoard[int(moveFrom[0])][int(moveFrom[1])][1:2]=="P":#checks if the moved piece is a pawn
				takesAndPawnMoves.append(0)#counts as a pawn move so appends a 0
				
				if int(moveTo[1])==0 or int(moveTo[1])==7:#checks if the pawn is moving to the first or 8th rank

					# code for random promote (not in use)
					# promote = { #creates a dictionary from 0-3 holding different pieces
					# 0: 'N',
					# 1: 'Q',
					# 2: 'R',
					# 3: 'B',
					# }

					#random--------------------------------

					# promoteTo=promote[random.randint(0,3)]#sets promoteTo to a random piece

					#random--------------------------------

					promoteTo="Q"#sets the pawn to be promoted to a queen
					promotestring='='+promoteTo#adds the move to the promotestring
					PGN_List[8]=PGN_List[8]+PGN.PGNADD(int(moveFrom[1]),int(moveTo[0]),int(moveFrom[0]),int(moveTo[1]),chessBoard,nextmove)[:-1]+promotestring.upper()+" "#adds the move to the PGN list
					os.system('clear')#clears the screen
					PGN.printMoves(PGN_List[8])#prints the moves
					chessBoard[int(moveFrom[0])][int(moveFrom[1])]=nextmove+promoteTo.upper()#sets the move on the chessboard
			
			else:
				
				if chessBoard[int(moveTo[1])][int(moveTo[0])]!= 0:#checks if the user did not move a pawn but did take 
					takesAndPawnMoves.append(0)#appends a 0 to the list because they took
				
				else:
					takesAndPawnMoves.append(1)#appends a 1 to the list because they did not take
			#computer PGN
			
			if config.start=="black":#checks if the user is on the black side
				PGN_List[8]=PGN_List[8]+str(move)+". "#adds a number to the PGN notation
				move+=1#increments the move
			
			if len(promotestring)!=2:#checks if there was no promotion
				PGN_List[8]=PGN_List[8]+PGN.PGNADD(int(moveFrom[1]),int(moveTo[0]),int(moveFrom[0]),int(moveTo[1]),chessBoard,nextmove)#adds the move to the string
				os.system('clear')#clears the screen
				PGN.printMoves(PGN_List[8])#prints the moves

			#sets new move

			chessBoard[int(moveTo[1])][int(moveTo[0])]=chessBoard[int(moveFrom[0])][int(moveFrom[1])]#sets the new position to the chess piece that the computer is moving
			chessBoard[int(moveFrom[0])][int(moveFrom[1])]=0#sets the old position to empty or 0


	#checks if the game is still on
	allGameStates.append(copy.deepcopy(chessBoard))#adds the current game state
	nextmove=moves.getNextMove(nextmove)#finds the next move
	board.displayScreen(chessBoard)#displays the board
	checkmate=check.checkmate(chessBoard,nextmove,fullgame)#finds if there is a checkmate
	stalemate=check.stalemate(chessBoard,nextmove,fullgame)#finds if there is a stalemate
	draw=check.draw(fullgame,takesAndPawnMoves,allGameStates,chessBoard)#finds if there is a draw
	
	if (check.check(chessBoard,nextmove)) and (not checkmate):#checks if this move caused a check and not a checkmate
		PGN_List[8]=PGN_List[8][:-1]+"+ "#adds a + to the end of the PGN line meaning there was a check
		os.system('clear')#clears the screen
		PGN.printMoves(PGN_List[8])#prints the moves
	
	return PGN_List,move,takesAndPawnMoves,chessBoard,fullgame,castleGame,allGameStates,nextmove,checkmate,stalemate,draw#returns all the new information

#Functions--------------------------------