# Authors: Andrew Tissi
# Date: Created: 4/1/21
# Description: functions to do with checks, and end game cenarios such as checkmate, stalemate and draw

import moves#imports the moves library
import config#imports the config library
import convert#imports the convert library

#Functions--------------------------------

def check(table,move):
	'''checks if someone is in check'''
	totalMoves=moves.findPossibleMoves(table)#finds all the possible moves
	
	for c in totalMoves:#loops through all moves
		#black's turn
		
		if move=="B":#checks if the next move is black
			if ("xBK" in c) and ("W" in c):return True#checks if the opponent's king can be "taken" next move and returns that there is a check
		#white's turn
		
		else:#checks if the next move is white
			if ("xWK" in c) and ("B" in c): return True#checks if the opponent's king can be "taken" next move and returns that there is a check
	return False#nocheck

def checkmate(table,move,fullgame):
	'''checks if there is a checkmate'''
	if not(stalemate(table,move,fullgame) and check(table,move)):return False#finds if there is no stalemate and no check, then returns false
	return True#returns true when there is a stalemate and there is a check
	
def stalemate(table,move,fullgame):
	'''checks if there is a stalemate'''
	verifiedMoves=moves.findVerifiedMoves(table,move)#finds all the verified moves in this position

	#en passant to get out of checkmate, very very VERY rare
	
	if len(fullgame)>=1:#checks if there is more than 1 move in the game
		numbers=convert.findBoardNumber(fullgame[-1][-2],fullgame[-1][-1])#finds the last move and it's numbers
		doubleMove=0#a move where the pawn went up 2 spaces
		left=0#left side 
		right=0#right side
		
		if numbers[1]=="4" and fullgame[-1][1]=="6": doubleMove=1#finds if the last move moved saw a pawn moving 2 spaces up (bottom pawn)

		elif numbers[1]=="3"and fullgame[-1][1]=="1": doubleMove=1#finds if the last move moved saw a pawn moving 2 spaces up (top pawn)
			

		if int(numbers[0])-1>=0 and int(numbers[0])-1<=7:#finds if a spot to the left exists
			left=table[int(numbers[1])][int(numbers[0])-1]#finds the piece in the spot to the left
		
		if int(numbers[0])+1>=0 and int(numbers[0])+1<=7:#finds if a spot to the right exists
			right=table[int(numbers[1])][int(numbers[0])+1]#finds the piece in the spot to the right

		if doubleMove==1 and (left==move+"P" or right==move+"P"):#checks if the user can en passant
			verifiedMoves.append("en passant")#adds an en passant to the verified moves

	#can not castle when close to stalemate so i dont need to add that here

	if len(verifiedMoves)!=0:return False#no stalemate
	return True#stalemate
	
def draw(fullgame,takesAndPawnMoves,allGameStates,Chessboard):
	'''checks if there is a draw'''
	if (fiftyMoveRule(takesAndPawnMoves[-50:])):#checks the 50 move rule
		result= "50 Move Rule"#returns the result as 50 move rule
	
	elif (threefoldRepetition(allGameStates)):#checks threefold repitition
		result= "Threefold Repetition"#returns the result as Threefold Repetition move rule
	
	elif (deadPosition(Chessboard)):#checks Dead Position
		result= "Dead Position"#returns the result as a Dead Position
	
	else:
		result=False#returns no draw
	return result#returns the result

def fiftyMoveRule(takesAndPawnMoves):
	'''checks if the 50 move rule has been hit (50 moves without taking or a pawn moving)'''
	if len(takesAndPawnMoves[-50:])!=50: return False#nope
	
	if takesAndPawnMoves[-50:].count(1)!=50: return False#checks for 50 moves without taking or a pawn moving
	return True#50 move rule
	
def threefoldRepetition(allGameStates):
	'''checks if threefold repition has been reached (the same postion has been played 3 times)'''
	
	for i in range(len(allGameStates)):#loops through all game states
		
		if (allGameStates.count(allGameStates[i]))>= 3:#checks if this one game state has appeared 3 times or more
			return True#returns true
	return False#no threefold repititon

def deadPosition(Chessboard):
	'''checks if there is insufficient material to cause a checkmate (king vs king, king+bishop vs king, king+knight vs king)'''
	material=countPieces(Chessboard)#finds all the pieces on the board
	
	if len(material)==2:#only king and king, dead position
		return True#returns a dead position
	
	elif len(material)==3:#checks there are 3 pieces on the board
		
		if ("BN" in material) or ("WN" in material) or ("BB" in material) or ("WB" in material):#K+N vs K or K+B vs K
			return True#returns a dead position
	return False#no dead position

def countPieces(Chessboard):
	'''Counts all the pieces on the board'''
	material=[]#creates a material list that will hold all the material on the board
	#gathers all the material on the chessboard
	
	for i in Chessboard:#loops through the chessboard array
		
		for k in i:#loops through each sub-array of the chessboard array
			
			if k!=0:#checks if there is a piece at this position
				material.append(k)#adds the piece to the material array
	return material#returns the found material

#Functions--------------------------------