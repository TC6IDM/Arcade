# Authors: Andrew Tissi
# Date: Created: 4/1/21
# Description: functions to do with chess moves

import config#imports the config library
import convert#imports the convert library
import copy#imports the copy library
import check#imports the check library

#Functions--------------------------------

def findPossibleMoves(table):
	'''Finds all the possible moves'''
	possibleMoves=[]#creates a list to store the possible moves
	
	if config.start=="white":#checks if player 1 is white
		topPawn="BP"#sets top pawn to BP
		bottomPawn="WP"#sets bottom pawn to WP
	
	else:#checks if player 1 is black
		topPawn="WP"#sets top pawn to WP
		bottomPawn="BP"#sets bottom pawn to BP
	posy=0#sets the y position to 0
	
	for c in range(8):#loops through each row
		posx=0#sets the x position to 0
		
		for d in range(8):#loops through each collum
			
			if table[c][d] != 0:#checks if this square on the table is empty
				
				if table[c][d][1:2]=="B":#checks if this square on the table is a bishop
					bishopMoves (table,d,c,possibleMoves)#gets all the bishop moves
				
				elif table[c][d][1:2]=="K":#checks if this square on the table is a king
					kingMoves (table,d,c,possibleMoves)#gets all the king moves
				
				elif table[c][d][1:2]=="N":#checks if this square on the table is a knight
					knightMoves (table,d,c,possibleMoves)#gets all the knight moves
				
				elif table[c][d][1:2]=="Q":#checks if this square on the table is a queen
					queenMoves (table,d,c,possibleMoves)#gets all the queen moves
				
				elif table[c][d][1:2]=="R":#checks if this square on the table is a rook
					rookMoves (table,d,c,possibleMoves)#gets all the rook moves
				
				elif table[c][d]==topPawn:#checks if this square on the table is a top pawn
					topPawnMoves (table,d,c,possibleMoves)#gets all the top pawn moves
				
				elif table[c][d]==bottomPawn:#checks if this square on the table is a bottom pawn
					bottomPawnMoves (table,d,c,possibleMoves)#gets all the bottom pawn moves
			posx+=config.square#increments the x value by the size of a square
		posy+=config.square#increments the y value by the size of a square
	return possibleMoves#returns all the moves

def bishopMoves (table,x,y,possibleMoves):
	'''Finds all the moves that the Bishop can make'''
	color = table[y][x][0:1]#finds the color of the current piece
	piece = table[y][x][1:2]#finds the type of the current piece
	stop1=False#does not stop in the +,+ direction
	stop2=False#does not stop in the -,- direction
	stop3=False#does not stop in the +,- direction
	stop4=False#does not stop in the -,+ direction

	for d in range(1,8):#goes through every square
		
		if -1<y+d<8 and -1<x+d<8 and stop1==False:#checks if the square is within the board and if we havent stopped moving in the +,+ direction
			
			if table[y+d][x+d] ==0:#move along positive positive untill stopped
				possibleMoves.append(color+str(y)+str(x)+piece+convert.findChessNumber(x+d,y+d))#adds moving without resistance to the list
			
			elif table[y+d][x+d][0:1]==color:#checks if the piece runs into its own color piece
				stop1=True#stops at this position
			
			elif table[y+d][x+d][0:1]!=color:#checks if the piece runs into a piece of another color
				possibleMoves.append(color+str(y)+str(x)+piece+"x"+table[y+d][x+d]+convert.findChessNumber(x+d,y+d))#adds taking another piece to the list
				stop1=True#stops at this position
	
		if -1<y-d<8 and -1<x-d<8 and stop2==False:#checks if the square is within the board and if we havent stopped moving in the -,- direction
			
			if table[y-d][x-d] ==0:#move along negative negative untill stopped
				possibleMoves.append(color+str(y)+str(x)+piece+convert.findChessNumber(x-d,y-d))#adds moving without resistance to the list
			
			elif table[y-d][x-d][0:1]==color:#checks if the piece runs into its own color piece
				stop2=True#stops at this position
			
			elif table[y-d][x-d][0:1]!=color:#checks if the piece runs into a piece of another color
				possibleMoves.append(color+str(y)+str(x)+piece+"x"+table[y-d][x-d]+convert.findChessNumber(x-d,y-d))#adds taking another piece to the list
				stop2=True#stops at this position
		
		if -1<y+d<8 and -1<x-d<8 and stop3==False:#checks if the square is within the board and if we havent stopped moving in the +,- direction
			
			if table[y+d][x-d] ==0:#move along positive negative untill stopped
				possibleMoves.append(color+str(y)+str(x)+piece+convert.findChessNumber(x-d,y+d))#adds moving without resistance to the list
			
			elif table[y+d][x-d][0:1]==color:#checks if the piece runs into its own color piece
				stop3=True#stops at this position
			
			elif table[y+d][x-d][0:1]!=color:#checks if the piece runs into a piece of another color
				possibleMoves.append(color+str(y)+str(x)+piece+"x"+table[y+d][x-d]+convert.findChessNumber(x-d,y+d))#adds taking another piece to the list
				stop3=True#stops at this position
		
		if -1<y-d<8 and -1<x+d<8 and stop4==False:#checks if the square is within the board and if we havent stopped moving in the -,+ direction
			
			if table[y-d][x+d] ==0:#move along negative positive untill stopped
				possibleMoves.append(color+str(y)+str(x)+piece+convert.findChessNumber(x+d,y-d))#adds moving without resistance to the list
			
			elif table[y-d][x+d][0:1]==color:#checks if the piece runs into its own color piece
				stop4=True#stops at this position
			
			elif table[y-d][x+d][0:1]!=color:#checks if the piece runs into a piece of another color
				possibleMoves.append(color+str(y)+str(x)+piece+"x"+table[y-d][x+d]+convert.findChessNumber(x+d,y-d))#adds taking another piece to the list
				stop4=True#stops at this position
		
def kingMoves (table,x,y,possibleMoves):
	'''Finds all the moves that the King can make'''
	color = table[y][x][0:1]#finds the color of the piece
	
	#Arrays/Lists--------------------------------

	#every square the king can move to
	possibleKingMoves=[
		[-1,-1],
		[-1,1],
		[1,-1],
		[1,1],
		[0,-1],
		[0,1],
		[1,0],
		[-1,0]
		]

	#Arrays/Lists--------------------------------

	#checks each one to see which ones are currently valid
	for c in range(len(possibleKingMoves)):#loops through every possible king's move
		moveLookupX=possibleKingMoves[c][0]#finds the x increment of the king's move
		moveLookupY=possibleKingMoves[c][1]#finds the y increment of the king's move
		
		if -1<x+moveLookupX<8 and -1<y+moveLookupY<8:#checks if the move is within the chess board
			
			if table[y+moveLookupY][x+moveLookupX] ==0:#checks if the move does not take a piece
				possibleMoves.append(color+str(y)+str(x)+"K"+convert.findChessNumber(x+moveLookupX,y+moveLookupY))#adds moving without resistance to the list
			
			elif table[y+moveLookupY][x+moveLookupX][0:1]==color:#checks if the piece runs into its own color piece
				pass #does nothing
			
			else:#checks if the piece runs into a piece of another color
				possibleMoves.append(color+str(y)+str(x)+"Kx"+table[y+moveLookupY][x+moveLookupX]+convert.findChessNumber(x+moveLookupX,y+moveLookupY))#adds taking another piece to the list

def knightMoves (table,x,y,possibleMoves):
	'''Finds all the moves that the Knight can make'''
	color = table[y][x][0:1]#finds the color of the piece

	#Arrays/Lists--------------------------------
	
	#every square the knight can move to
	possibleKnightMoves=[
		[-1,2],
		[-2,1],
		[-2,-1],
		[-1,-2],
		[1,-2],
		[2,-1],
		[2,1],
		[1,2]
		]

	#Arrays/Lists--------------------------------

	#checks each one to see which ones are currently valid
	
	for c in range(len(possibleKnightMoves)):#loops through every possible knight's move
		moveLookupX=possibleKnightMoves[c][0]#finds the x increment of the knight's move
		moveLookupY=possibleKnightMoves[c][1]#finds the y increment of the knight's move
		
		if -1<x+moveLookupX<8 and -1<y+moveLookupY<8:#checks if the move does not take a piece
			
			if table[y+moveLookupY][x+moveLookupX] ==0:#checks if the move does not take a piece
				possibleMoves.append(color+str(y)+str(x)+"N"+convert.findChessNumber(x+moveLookupX,y+moveLookupY))#adds moving without resistance to the list
			
			elif table[y+moveLookupY][x+moveLookupX][0:1]==color:#checks if the piece runs into its own color piece
				pass #does nothing
			
			else:
				possibleMoves.append(color+str(y)+str(x)+"Nx"+table[y+moveLookupY][x+moveLookupX]+convert.findChessNumber(x+moveLookupX,y+moveLookupY))#adds taking another piece to the list

def queenMoves (table,x,y,possibleMoves):
	'''Finds all the moves that the Queen can make'''
	#queens move as rooks and bishops fused into one
	rookMoves (table,x,y,possibleMoves)#finds all the rook's moves
	bishopMoves (table,x,y,possibleMoves)#finds all the bishop's moves

def rookMoves (table,x,y,possibleMoves):
	'''Finds all the moves that the Rook can make'''
	color = table[y][x][0:1]#gets the color of the piece
	piece = table[y][x][1:2]#gets the type of the piece
	stopy1=False#does not stop in the positive y direction
	stopx1=False#does not stop in the positive x direction
	
	for d in range(1,8):#goes through every square
	
		if -1<y+d<8 and stopy1==False:#checks if the square is within the board and if we havent stopped moving in the positive y direction
			
			if table[y+d][x] ==0:#moves up untill stopped
				possibleMoves.append(color+str(y)+str(x)+piece+convert.findChessNumber(x,y+d))#adds moving without resistance to the list
			
			elif table[y+d][x][0:1]==color:#checks if the piece runs into its own color piece
				stopy1=True#stops at this position
			
			elif table[y+d][x][0:1]!=color:#checks if the piece runs into a piece of another color
				possibleMoves.append(color+str(y)+str(x)+piece+"x"+table[y+d][x]+convert.findChessNumber(x,y+d))#adds taking another piece to the list
				stopy1=True#stops at this position
		
		if -1<x+d<8 and stopx1==False:#checks if the square is within the board and if we havent stopped moving in the positive x direction
			
			if table[y][x+d] ==0:#moves right untill stopped
				possibleMoves.append(color+str(y)+str(x)+piece+convert.findChessNumber(x+d,y))#adds moving without resistance to the list
			
			elif table[y][x+d][0:1]==color:#checks if the piece runs into its own color piece
				stopx1=True#stops at this position
			
			elif table[y][x+d][0:1]!=color:#checks if the piece runs into a piece of another color
				possibleMoves.append(color+str(y)+str(x)+piece+"x"+table[y][x+d]+convert.findChessNumber(x+d,y))#adds taking another piece to the list
				stopx1=True#stops at this position
	stopy2=False#does not stop in the negative y direction
	stopx2=False#does not stop in the negative x direction

	for f in range(1,8):#goes through every square
		d=f*(-1)#inverses f
		
		if -1<y+d<8 and stopy2==False:#checks if the square is within the board and if we havent stopped moving in the negative y direction
		
			if table[y+d][x] ==0:#moves down untill stopped
				possibleMoves.append(color+str(y)+str(x)+piece+convert.findChessNumber(x,y+d))#adds moving without resistance to the list
			
			elif table[y+d][x][0:1]==color:#checks if the piece runs into its own color piece
				stopy2=True#stops at this position
			
			elif table[y+d][x][0:1]!=color:#checks if the piece runs into a piece of another color
				possibleMoves.append(color+str(y)+str(x)+piece+"x"+table[y+d][x]+convert.findChessNumber(x,y+d))#adds taking another piece to the list
				stopy2=True#stops at this position
	
		if -1<x+d<8 and stopx2==False:#checks if the square is within the board and if we havent stopped moving in the negative x direction
			
			if table[y][x+d] ==0:#moves left untill stopped
				possibleMoves.append(color+str(y)+str(x)+piece+convert.findChessNumber(x+d,y))#adds moving without resistance to the list
			
			elif table[y][x+d][0:1]==color:#checks if the piece runs into its own color piece
				stopx2=True#stops at this position
			
			elif table[y][x+d][0:1]!=color:#checks if the piece runs into a piece of another color
				possibleMoves.append(color+str(y)+str(x)+piece+"x"+table[y][x+d]+convert.findChessNumber(x+d,y))#adds taking another piece to the list
				stopx2=True#stops at this position

def bottomPawnMoves (table,x,y,possibleMoves):
	'''Finds all the moves that the relative Bottom Pawn can make'''
	color = table[y][x][0:1]#finds the color of the current pawn
	
	if config.start=="white":#finds if player 1's color is white
		topPawn="B"#sets the top pawn's color to black
	
	else:#finds if player 1's color is black
		topPawn="W"#sets the top pawn's color to white
	
	if y==6:#checks if the pawn is on it's starting rank
		
		if table[y-1][x]==0 and table[y-2][x]==0:#checks if the path is clear
			possibleMoves.append(color+str(y)+str(x)+"P"+convert.findChessNumber(x,y-2))#adds moving without resistance to the list
	
	if -1<y-1<8:#checks if the value up exists
		
		if table[y-1][x]==0:#checks if the square above is empty
			possibleMoves.append(color+str(y)+str(x)+"P"+convert.findChessNumber(x,y-1))#adds moving without resistance to the list
	
	if -1<y-1<8 and -1<x-1<8:#checks if the square above and to the left is on the board
		
		if str(table[y-1][x-1])[0:1]==topPawn:#checks if the piece above and to the left is on the other team
			possibleMoves.append(color+str(y)+str(x)+"Px"+table[y-1][x-1]+convert.findChessNumber(x-1,y-1))#adds taking another piece to the list

	if -1<y-1<8 and -1<x+1<8:#checks if the square above and to the right is on the board
		
		if str(table[y-1][x+1])[0:1]==topPawn:#checks if the piece above and to the right is on the other team
			possibleMoves.append(color+str(y)+str(x)+"Px"+table[y-1][x+1]+convert.findChessNumber(x+1,y-1))#adds taking another piece to the list
			
def topPawnMoves (table,x,y,possibleMoves):
	'''Finds all the moves that the relative Bottom Pawn can make'''
	color = table[y][x][0:1]#finds the color of the current pawn
	
	if config.start=="white":#finds if player 1's color is white
		bottomPawn="W"#sets the bottom pawn's color to white
	
	else:#finds if player 1's color is black
		bottomPawn="B"#sets the bottom pawn's color to black
	#checks if it can move twice
	
	if y==1:#checks if the pawn is on it's starting rank
		
		if table[y+1][x]==0 and table[y+2][x]==0:#checks if the path is clear
			possibleMoves.append(color+str(y)+str(x)+"P"+convert.findChessNumber(x,y+2))#adds moving without resistance to the list
	
	if -1<y+1<8:#checks if the value down exists
		
		if table[y+1][x]==0:#checks if the square below is empty
			possibleMoves.append(color+str(y)+str(x)+"P"+convert.findChessNumber(x,y+1))#adds moving without resistance to the list
	
	if -1<y+1<8 and -1<x-1<8:#checks if the square below and to the left is on the board
		
		if str(table[y+1][x-1])[0:1]==bottomPawn:#checks if the piece below and to the left is on the other team
			possibleMoves.append(color+str(y)+str(x)+"Px"+table[y+1][x-1]+convert.findChessNumber(x-1,y+1))#adds taking another piece to the list
	
	if -1<y+1<8 and -1<x+1<8:#checks if the square below and to the right is on the board
		
		if str(table[y+1][x+1])[0:1]==bottomPawn:#checks if the piece below and to the right is on the other team
			possibleMoves.append(color+str(y)+str(x)+"Px"+table[y+1][x+1]+convert.findChessNumber(x+1,y+1))#adds taking another piece to the list

def canCastle (chessBoard,castleGame):
	'''Checks if castling is possible'''

	castle=""#sets the castle string

	if config.start=="white": #checks if player 1 is white


		if (((str(chessBoard[7][0])+str(chessBoard[7][1])+str(chessBoard[7][2])+str(chessBoard[7][3])+str(chessBoard[7][4])=="WR000WK") and (not("70" in castleGame))and (not("74" in castleGame))and (not(check.check(chessBoard,"W"))))):#checks if the king, and queen side rook have not moved this game, also checks if the path shows white rook, 3 empty spaces then white king, and that the king is not in check
			castlechessBoard=copy.deepcopy(chessBoard)#copys the chessboard
			castlechessBoard[7][3]="WK"#moves the white king to the left
			castlechessBoard[7][4]=0#sets the previous spot to empty
			
			if not(check.check(castlechessBoard,"W")):#checks if there is not a check in this position
				castlechessBoard[7][2]="WK"#moves the white king to the left
				castlechessBoard[7][3]=0#sets the previous spot to empty
				
				if not(check.check(castlechessBoard,"W")):#checks if there is not a check in this position
					castle+="WQ"#adds white queen side to the castle string


		if (((str(chessBoard[7][7])+str(chessBoard[7][6])+str(chessBoard[7][5])+str(chessBoard[7][4])=="WR00WK")and (not("77" in castleGame))and (not("74" in castleGame))and (not(check.check(chessBoard,"W"))))):#checks if the king, and king side rook have not moved this game, also checks if the path shows white rook, 2 empty spaces then white king, and that the king is not in check
			castlechessBoard=copy.deepcopy(chessBoard)#copys the chessboard
			castlechessBoard[7][5]="WK"#moves the white king to the right
			castlechessBoard[7][4]=0#sets the previous spot to empty
			
			if not(check.check(castlechessBoard,"W")):#checks if there is not a check in this position
				castlechessBoard[7][6]="WK"#moves the white king to the right
				castlechessBoard[7][5]=0#sets the previous spot to empty
				
				if not(check.check(castlechessBoard,"W")):#checks if there is not a check in this position
					castle+="WK"#adds white king side to the castle string


		if (((str(chessBoard[0][0])+str(chessBoard[0][1])+str(chessBoard[0][2])+str(chessBoard[0][3])+str(chessBoard[0][4])=="BR000BK") and (not("00" in castleGame))and (not("04" in castleGame))and (not(check.check(chessBoard,"B"))))):#checks if the king, and queen side rook have not moved this game, also checks if the path shows black rook, 3 empty spaces then black king, and that the king is not in check
			castlechessBoard=copy.deepcopy(chessBoard)#copys the chessboard
			castlechessBoard[0][3]="BK"#moves the black king to the left
			castlechessBoard[0][4]=0#sets the previous spot to empty
			
			if not(check.check(castlechessBoard,"B")):#checks if there is not a check in this position
				castlechessBoard[0][2]="BK"#moves the black king to the left
				castlechessBoard[0][3]=0#sets the previous spot to empty
				
				if not(check.check(castlechessBoard,"B")):#checks if there is not a check in this position
					castle+="BQ"#adds black queen side to the castle string


		if (((str(chessBoard[0][7])+str(chessBoard[0][6])+str(chessBoard[0][5])+str(chessBoard[0][4])=="BR00BK")and (not("07" in castleGame))and (not("04" in castleGame))and (not(check.check(chessBoard,"B"))))):#checks if the king, and king side rook have not moved this game, also checks if the path shows black rook, 2 empty spaces then black king, and that the king is not in check
			castlechessBoard=copy.deepcopy(chessBoard)#copys the chessboard
			castlechessBoard[0][5]="BK"#moves the black king to the right
			castlechessBoard[0][4]=0#sets the previous spot to empty
			
			if not(check.check(castlechessBoard,"B")):#checks if there is not a check in this position
				castlechessBoard[0][6]="BK"#moves the black king to the right
				castlechessBoard[0][5]=0#sets the previous spot to empty
				
				if not(check.check(castlechessBoard,"B")):#checks if there is not a check in this position
					castle+="BK"#adds black king side to the castle string


	else:#checks if player 1 is black
		

		if (((str(chessBoard[7][7])+str(chessBoard[7][6])+str(chessBoard[7][5])+str(chessBoard[7][4])+str(chessBoard[7][3])=="BR000BK") and (not("77" in castleGame))and (not("73" in castleGame))and (not(check.check(chessBoard,"B"))))):#checks if the king, and queen side rook have not moved this game, also checks if the path shows black rook, 3 empty spaces then black king, and that the king is not in check
			castlechessBoard=copy.deepcopy(chessBoard)#copys the chessboard
			castlechessBoard[7][4]="BK"#moves the white king to the right
			castlechessBoard[7][3]=0#sets the previous spot to empty
			
			if not(check.check(castlechessBoard,"B")):#checks if there is not a check in this position
				castlechessBoard[7][5]="BK"#moves the white king to the right
				castlechessBoard[7][4]=0#sets the previous spot to empty
				
				if not(check.check(castlechessBoard,"B")):#checks if there is not a check in this position
					castle+="BQ"#adds black queen side to the castle string

		if (((str(chessBoard[7][0])+str(chessBoard[7][1])+str(chessBoard[7][2])+str(chessBoard[7][3])=="BR00BK")and (not("70" in castleGame))and (not("73" in castleGame))and (not(check.check(chessBoard,"B"))))):#checks if the king, and king side rook have not moved this game, also checks if the path shows black rook, 2 empty spaces then black king, and that the king is not in check
			castlechessBoard=copy.deepcopy(chessBoard)#copys the chessboard
			castlechessBoard[7][2]="BK"#moves the white king to the left
			castlechessBoard[7][3]=0#sets the previous spot to empty
			
			if not(check.check(castlechessBoard,"B")):#checks if there is not a check in this position
				castlechessBoard[7][1]="BK"#moves the white king to the left
				castlechessBoard[7][2]=0#sets the previous spot to empty
				
				if not(check.check(castlechessBoard,"B")):#checks if there is not a check in this position
					castle+="BK"#adds black king side to the castle string


		if (((str(chessBoard[0][7])+str(chessBoard[0][6])+str(chessBoard[0][5])+str(chessBoard[0][4])+str(chessBoard[0][3])=="WR000WK") and (not("07" in castleGame))and (not("03" in castleGame))and (not(check.check(chessBoard,"W"))))):#checks if the king, and queen side rook have not moved this game, also checks if the path shows white rook, 3 empty spaces then white king, and that the king is not in check
			castlechessBoard=copy.deepcopy(chessBoard)#copys the chessboard
			castlechessBoard[0][4]="WK"#moves the white king to the right
			castlechessBoard[0][3]=0#sets the previous spot to empty
			
			if not(check.check(castlechessBoard,"W")):#checks if there is not a check in this position
				castlechessBoard[0][5]="WK"#moves the white king to the right
				castlechessBoard[0][4]=0#sets the previous spot to empty
				
				if not(check.check(castlechessBoard,"W")):#checks if there is not a check in this position
					castle+="WQ"#adds white queen side to the castle string


		if (((str(chessBoard[0][0])+str(chessBoard[0][1])+str(chessBoard[0][2])+str(chessBoard[0][3])=="WR00WK")and (not("00" in castleGame))and (not("03" in castleGame))and (not(check.check(chessBoard,"W"))))):#checks if the king, and king side rook have not moved this game, also checks if the path shows white rook, 2 empty spaces then white king, and that the king is not in check
			castlechessBoard=copy.deepcopy(chessBoard)#copys the chessboard
			castlechessBoard[0][2]="WK"#moves the white king to the left
			castlechessBoard[0][3]=0#sets the previous spot to empty
			
			if not(check.check(castlechessBoard,"W")):#checks if there is not a check in this position
				castlechessBoard[0][1]="WK"#moves the white king to the left
				castlechessBoard[0][2]=0#sets the previous spot to empty
				
				if not(check.check(castlechessBoard,"W")):#checks if there is not a check in this position
					castle+="WK"#adds white king side to the castle string
	return castle#returns the castle string

def castle(nextmove,chessBoard,castleGame,xSquare1,xSquare2,ySquare1,ySquare2):
	'''checks for any castles'''
	PGN=""#sets the PGN string
	
	if nextmove=="W":#checks if the next move is white

		if ("WQ" in canCastle(chessBoard,castleGame)) and int(xSquare1) ==4 and int(xSquare2) == 2 and int(ySquare1) == 7 and int(ySquare2) == 7 and config.start=="white":#checks if castling white queen side is possible and the user is in the right mouse positions to execute it
			chessBoard[7][2]="WK"#moves the king to where it needs to be
			chessBoard[7][3]="WR"#moves the rook to where it needs to be
			chessBoard[7][0]=0#sets the previous spot to empty
			chessBoard[7][4]=0#sets the previous spot to empty
			PGN="O-O-O "#adds the PGN notation for queen side castle

		elif ("WK" in canCastle(chessBoard,castleGame)) and int(xSquare1) ==4 and int(xSquare2) == 6 and int(ySquare1) == 7 and int(ySquare2) == 7 and config.start=="white":#checks if castling white king side is possible and the user is in the right mouse positions to execute it
			chessBoard[7][6]="WK"#moves the king to where it needs to be
			chessBoard[7][5]="WR"#moves the rook to where it needs to be
			chessBoard[7][7]=0#sets the previous spot to empty
			chessBoard[7][4]=0#sets the previous spot to empty
			PGN="O-O "#adds the PGN notation for king side castle

	else:#checks if the next move is black

		if ("BK" in canCastle(chessBoard,castleGame)) and int(xSquare1) ==4 and int(xSquare2) == 6 and int(ySquare1) == 0 and int(ySquare2) == 0 and config.start=="white":#checks if castling black king side is possible and the user is in the right mouse positions to execute it
			chessBoard[0][6]="BK"#moves the king to where it needs to be
			chessBoard[0][5]="BR"#moves the rook to where it needs to be
			chessBoard[0][7]=0#sets the previous spot to empty
			chessBoard[0][4]=0#sets the previous spot to empty
			PGN="O-O "#adds the PGN notation for king side castle

		if ("BQ" in canCastle(chessBoard,castleGame)) and int(xSquare1) ==4 and int(xSquare2) == 2 and int(ySquare1) == 0 and int(ySquare2) == 0 and config.start=="white":#checks if castling black queen side is possible and the user is in the right mouse positions to execute it
			chessBoard[0][2]="BK"#moves the king to where it needs to be
			chessBoard[0][3]="BR"#moves the rook to where it needs to be
			chessBoard[0][0]=0#sets the previous spot to empty
			chessBoard[0][4]=0#sets the previous spot to empty
			PGN="O-O-O "#adds the PGN notation for queen side castle

	if nextmove=="W":#checks if the next move is white

		if ("WK" in canCastle(chessBoard,castleGame)) and int(xSquare1) ==3 and int(xSquare2) == 1 and int(ySquare1) == 0 and int(ySquare2) == 0 and config.start=="black":#checks if castling white king side is possible and the user is in the right mouse positions to execute it
			chessBoard[0][1]="WK"#moves the king to where it needs to be
			chessBoard[0][2]="WR"#moves the rook to where it needs to be
			chessBoard[0][0]=0#sets the previous spot to empty
			chessBoard[0][3]=0#sets the previous spot to empty
			PGN="O-O "#adds the PGN notation for king side castle

		elif ("WQ" in canCastle(chessBoard,castleGame)) and int(xSquare1) ==3 and int(xSquare2) == 5 and int(ySquare1) == 0 and int(ySquare2) == 0 and config.start=="black":#checks if castling white queen side is possible and the user is in the right mouse positions to execute it
			chessBoard[0][5]="WK"#moves the king to where it needs to be
			chessBoard[0][4]="WR"#moves the rook to where it needs to be
			chessBoard[0][7]=0#sets the previous spot to empty
			chessBoard[0][3]=0#sets the previous spot to empty
			PGN="O-O-O "#adds the PGN notation for queen side castle

	else:#checks if the next move is black

		if ("BQ" in canCastle(chessBoard,castleGame)) and int(xSquare1) ==3 and int(xSquare2) == 5 and int(ySquare1) == 7 and int(ySquare2) == 7 and config.start=="black":#checks if castling black queen side is possible and the user is in the right mouse positions to execute it
			chessBoard[7][5]="BK"#moves the king to where it needs to be
			chessBoard[7][4]="BR"#moves the rook to where it needs to be
			chessBoard[7][7]=0#sets the previous spot to empty
			chessBoard[7][3]=0#sets the previous spot to empty
			PGN="O-O-O "#adds the PGN notation for queen side castle

		if ("BK" in canCastle(chessBoard,castleGame)) and int(xSquare1) ==3 and int(xSquare2) == 1 and int(ySquare1) == 7 and int(ySquare2) == 7 and config.start=="black":#checks if castling black king side is possible and the user is in the right mouse positions to execute it
			chessBoard[7][1]="BK"#moves the king to where it needs to be
			chessBoard[7][2]="BR"#moves the rook to where it needs to be
			chessBoard[7][3]=0#sets the previous spot to empty
			chessBoard[7][0]=0#sets the previous spot to empty
			PGN="O-O "#adds the PGN notation for king side castle
			
	return [chessBoard,PGN]#returns the new chessboard along with the PGN notation

def enpassant(fullgame,x1,x2,y1,y2,nextmove,chessBoard):
	'''Checks for any en passants'''
	if len(fullgame)>=1:#checks if the game has been longer than 1 move
		numbers=convert.findBoardNumber(fullgame[-1][-2],fullgame[-1][-1])#finds the position of the last moved piece
		changingy=0#creates the changing y value
		changingx=0#creates the changing x value

		if numbers[1]=="4" and fullgame[-1][1]=="6":#checks if the last move was from rank 2 to rank 4
			changingy=int(numbers[1])+1#sets the chaning y value to 1 more than the last move

		elif numbers[1]=="3"and fullgame[-1][1]=="1":#checks if the last move was from rank 7 to rank 5
			changingy=int(numbers[1])-1#sets the chaning y value to 1 less than the last move
		#en passant to the left
		
		if x1==int(numbers[0])-1 and y1==int(numbers[1]) and chessBoard[int(numbers[1])][int(numbers[0])-1]==nextmove+"P":#checks if the piece can be taken with en passant from the left
			changingx=int(numbers[0])-1#sets the chaning x value to the left of the last move
		#en passant to the right
		
		elif x1==int(numbers[0])+1 and y1==int(numbers[1]) and chessBoard[int(numbers[1])][int(numbers[0])+1]==nextmove+"P":#checks if the piece can be taken with en passant from the right
				changingx=int(numbers[0])+1#sets the chaning x value to the right of the last move

		if (changingx>=0 and changingx<=7):#checks if the changing x values exist on the board
			if x2==int(numbers[0]) and y2==changingy and fullgame[-1][-3]=="P":#checks if the position where the user wants to move is where they would have to move for en passant, and the piece they want to en passant is a pawn
				chessBoard[changingy][int(numbers[0])]=chessBoard[int(numbers[1])][changingx]#move the en passant
				chessBoard[int(numbers[1])][changingx]=0#sets the previous spot to empty
				chessBoard[int(numbers[1])][int(numbers[0])]=0#sets the previous spot to empty
	return chessBoard#returns the new chessboard

def getNextMove(move):
	'''calculates the next move'''
	if move=="B":#checks if the move is black
		return "W"#returns white
	return "B"#returns black if the move is white

def findVerifiedMoves(table,move):
	'''finds all the legal moves'''
	verifiedMoves=[]#creates a list for the verified moves
	moveString=""#creates a string for the moves
	singularMoves=findPossibleMoves(table)#finds all the possible moves
	#makes a big string of all the moves
	
	for k in singularMoves:#loops through all the moves
		moveString= moveString+k[-2:]#adds up to the last 2 characters to the string
	#checks every move for validity
	
	for nowmove in singularMoves:#loops through all the moves in the list
		nextmove=getNextMove(move)#finds the next move, black or white
		moveTo=convert.findBoardNumber(nowmove[-2],nowmove[-1])#finds where the move is to
		moveFrom=nowmove[1] + nowmove[2]#finds where the move is from
		futurechessBoard=copy.deepcopy(table)#clones the chessboard 
		futurechessBoard[int(moveTo[1])][int(moveTo[0])]=futurechessBoard[int(moveFrom[0])][int(moveFrom[1])]#proceeds with the move
		futurechessBoard[int(moveFrom[0])][int(moveFrom[1])]=0#sets the previous spot to empty
		
		if not (check.check(futurechessBoard,move)):#finds if there is no check
			
			if (convert.findChessNumber(int(moveTo[-2]),int(moveTo[-1])) in moveString)and nextmove!=nowmove[0:1]:#verifys the move if it is legal
				verifiedMoves.append(nowmove)#adds the move to the verified list
	return verifiedMoves#returns the verified moves

#Functions--------------------------------