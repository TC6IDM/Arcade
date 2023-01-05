# Authors: Andrew Tissi
# Date: Created: 4/1/21
# Description: functions to do with conversions
import config#imports the config

#Functions--------------------------------

def findChessNumber(x,y):
	'''digit to chess number'''
	color=config.start#finds the starting color
	
	if color=="white":#checks if player 1 is white
		#creates a dictionary that can convert from a digit to a chess number for the colum

		#Arrays/Lists--------------------------------

		colum = {
				'0': '8',
				'1': '7',
				'2': '6',
				'3': '5',
				'4': '4',
				'5': '3',
				'6': '2',
				'7': '1',
		}
		#creates a dictionary that can convert from a digit to a chess letter for the row
		row = {
				'0': 'a',
				'1': 'b',
				'2': 'c',
				'3': 'd',
				'4': 'e',
				'5': 'f',
				'6': 'g',
				'7': 'h',
		}

		#Arrays/Lists--------------------------------

	else:#checks if player 1 is black
		#creates a dictionary that can convert from a digit to a chess number for the colum

		#Arrays/Lists--------------------------------

		colum = {
				'0': '1',
				'1': '2',
				'2': '3',
				'3': '4',
				'4': '5',
				'5': '6',
				'6': '7',
				'7': '8',
		}
		#creates a dictionary that can convert from a digit to a chess letter for the row
		row = {
				'0': 'h',
				'1': 'g',
				'2': 'f',
				'3': 'e',
				'4': 'd',
				'5': 'c',
				'6': 'b',
				'7': 'a',
		}

		#Arrays/Lists--------------------------------

	x=str(x)#converts x to a string
	y=str(y)#converts y to a string
	return row[x]+colum[y]#returns a string of length 2, it will hold a chess position

def findBoardNumber(x,y):
	'''chess number to digit'''
	color=config.start#finds the starting color
	
	if color=="white":#checks if player 1 is white
		#creates a dictionary that can convert from a chess number to a digit for the colum

		#Arrays/Lists--------------------------------

		colum = {
				'8': '0',
				'7': '1',
				'6': '2',
				'5': '3',
				'4': '4',
				'3': '5',
				'2': '6',
				'1': '7',
		}
		#creates a dictionary that can convert from a letter to a chess number for the row
		row = {
				'a': '0',
				'b': '1',
				'c': '2',
				'd': '3',
				'e': '4',
				'f': '5',
				'g': '6',
				'h': '7',
		}

		#Arrays/Lists--------------------------------

	else:#checks if player 1 is black
		#creates a dictionary that can convert from a chess number to a digit for the colum

		#Arrays/Lists--------------------------------

		colum = {
				'1': '0',
				'2': '1',
				'3': '2',
				'4': '3',
				'5': '4',
				'6': '5',
				'7': '6',
				'8': '7',
		}
		#creates a dictionary that can convert from a letter to a chess number for the row
		row = {
				'h': '0',
				'g': '1',
				'f': '2',
				'e': '3',
				'd': '4',
				'c': '5',
				'b': '6',
				'a': '7',
		}
		
		#Arrays/Lists--------------------------------

	x=str(x)#converts x to a string
	y=str(y)#converts y to a string
	return row[x]+colum[y]#returns a string of length 2, it will hold a digit that can be understood by indexing the list

#Functions--------------------------------