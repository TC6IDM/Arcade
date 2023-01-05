# Authors: Andrew Tissi
# Date: Created: 4/1/21
# Description: functions to do with PGN notation

import convert#imports the convert library
import config#imports the config library
import moves#imports the moves library
import copy#imports the copy library

#Functions--------------------------------

def PGNADD(x1,x2,y1,y2,chessBoard,nextmove):
	'''Adds a new move to the PGN list'''
	if chessBoard[y1][x1][1]=="P":#checks if the move was made by a pawn
		
		if chessBoard[y2][x2]==0:#checks if the position where the piece is moving to is empty
			return convert.findChessNumber(x2,y2)+" "#returns the chess notation for a pawn
		return convert.findChessNumber(x1,y1)[0]+"x"+convert.findChessNumber(x2,y2)+" "#returns the chess notation with an x in the middle to show that a piece was taken by a pawn
	
	else:#anything other than a pawn
		verifiedMoves=moves.findVerifiedMoves(chessBoard,nextmove)#finds all the moves
		shortenedMoves=copy.copy(verifiedMoves)#copys all the moves
		ambiguousMoves=[]#creates a list for ambiguous moves
		
		for p in range(len(shortenedMoves)):#loops through all the moves
			
			if shortenedMoves[p][3]+shortenedMoves[p][-2:]==chessBoard[y1][x1][1]+convert.findChessNumber(x2,y2):#finds the piece that is being moved, as well as any other piece of the same type that can move to the same square
				ambiguousMoves.append(verifiedMoves[p])#appends the piece to a new list
			shortenedMoves[p]=shortenedMoves[p][3]+shortenedMoves[p][-2:]#removes anything around the move and leaves it as the type of piece, and where it moves to
		
		if shortenedMoves.count(chessBoard[y1][x1][1]+convert.findChessNumber(x2,y2))>=2:#checks if more than one of the same piece can move to the specified location
			rank=[]#creates a list for all the ranks which pieces of the same type can move to
			file=[]#creates a list for all the files which pieces of the same type can move to
			
			for c in ambiguousMoves:#loops through every piece of the same type that can move to that square
				rank.append(c[1])#adds the current rank to the rank list
				file.append(c[2])#adds the current file to the file list
			take=""#creates a string that will store an x if the piece will take if it moves
			
			if chessBoard[y2][x2]!=0:#checks if the piece will take if it moves
				take="x"#sets the string to indicate that the piece will take
			xy=convert.findChessNumber(x1,y1)#gets the chess notation of where the piece is moving from
			
			if rank.count(str(y1))>=2 and file.count(str(x1))>=2:#there are multiple of the same piece, on the same file and rank that can move to the specified square
				return chessBoard[y1][x1][1]+xy+take+convert.findChessNumber(x2,y2)+" "#use rank and file to determine the piece that moves in PGN notation
			
			elif file.count(str(x1))>=2:#multiple of the same piece on the same file that can move to the specified square
				return chessBoard[y1][x1][1]+xy[1]+take+convert.findChessNumber(x2,y2)+" "#uses rank to determine the piece that moves in PGN notation
			
			#no other case is met, but 2 pieces can still move to the same square
			return chessBoard[y1][x1][1]+xy[0]+take+convert.findChessNumber(x2,y2)+" "#uses file to determine the piece that moves in PGN notation

		if chessBoard[y2][x2]==0:#no piece being taken
			return chessBoard[y1][x1][1]+convert.findChessNumber(x2,y2)+" "#returns a regular move in PGN notation
		return chessBoard[y1][x1][1]+"x"+convert.findChessNumber(x2,y2)+" "# returns a regular take in PGN notation

def printMoves(moves):
	'''Prints all the moves in the game and adds as the game continues'''
	count=0#sets the count of spaces to 0
	moves=list(moves)#converts the string to a list
	moveString=""#creates a string to hold all the moves
	
	for i in range(len(moves)):#loops through the whole list of moves
		
		if moves[i]==" ":#checks if there is a space at this part of the string
			count+=1#increases the count of spaces
		
		if count==3:#finds the third space
			moves[i]="\n"#eplaces it with a newline charater
			count=0#resets the count of spaces to 0
	
	for j in moves:#loops through the new list
		moveString+=j#changes the list back to a string
	print(moveString)#prints the new string

#Functions--------------------------------