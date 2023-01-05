# Authors: Andrew Tissi
# Date: Created: 4/1/21
# Description: A class to help users

from os import path#imports path from the os library
import os#imports the os library
import time#imports the time library

#Functions--------------------------------

def is_number(string):
	'''Checks if this string contains a number'''
	try:#runs the below code
		float(string)#converts the string to a float
		return True#returns true
	except ValueError:#checks if the string cant be converted to a float 
		 return False#returns false

#Functions--------------------------------

#OOP--------------------------------

class User:
	"""A user class that can work with the user's balance"""
	def __init__(self,prefix):
		'''initializes the user class'''
		self.get_name(prefix)#gets the name of the user
		self.get_balance()#gets the user's balance
	
	def get_name(self,prefix):
		'''gets the name of the user'''
		self.name=input(str(prefix)+"What is your name? ")#asks the user what their name is
		os.system('clear')#clears the screen

	def get_balance(self):
		'''gets the balance of the user'''

		#files--------------------------------

		if not(path.exists('people/'+self.name.lower()+'.txt')):#checks if the user does not have a file
			
			with open('people/'+self.name.lower()+'.txt', 'w') as f:#creates a file and makes it a write only
				f.write(str(500))#write 500 to the file
				f.close()#closes the file
			print(str(self.name)+", We see this is your first time playing, we have started you with $500")#tells the user that they do not have a account and creates one from them
			self.bal=float(500)#writes 500 to the user's balance
		
		with open('people/'+self.name.lower()+'.txt', 'r') as f:#opens the specified file as a read only
			self.bal=float(f.read())#reads the user's balance
			f.close()#closes the file
		
		#files--------------------------------

	def get_bet(self):
		'''gets the user's bet'''
		self.bet=" "#makes the bet larger than the user's balance
		
		while (not(self.bet.isnumeric() or is_number(self.bet))) or ((self.bet.isnumeric() or is_number(self.bet)) and float(self.bet)>self.bal):#runs this code while the user's bet is larger than what they actually have or if their bet is not a real number
			self.display_bal()#displays the user's balence
			self.bet=input(str(self.name)+", What is your bet? ")#asks the user for their bet
			os.system("clear")#clears the screen
		self.bet=float(self.bet)#sets the bet to a float
	
	def display_bal(self):
		"""displays the user's balance"""
		print(str(self.name)+", Your current balance is: $"+str(self.bal))#displays the user's balance

	def updateBal(self,multi):
		"""updates the user's balance with the multiplier from the game"""
		self.bal+=(self.bet*multi) - self.bet#make a new balance for the user given their bet and the multiplier they were given at the end of a game
		self.bal=round(self.bal,2)#round the balance to 2 decimal places
		self.writeBal()#Writes the user's balance to their txt file
	
	def writeBal(self):
		"""Writes the user's balance to their txt file"""

		#files--------------------------------

		with open('people/'+self.name.lower()+'.txt', 'w') as f:#opens the specified file as a write only
			f.write(str(self.bal))#writes the user's balance to the file
			f.close()#closes the file

		#files--------------------------------

#OOP--------------------------------