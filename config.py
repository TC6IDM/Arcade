# Authors: Andrew Tissi
# Date: Created: 4/1/21
# Description: configuration for chess

import pygame #imports pygame
#specs
width, height = 480, 480#dimensions
backgroundColor = 238, 238, 210#background color
square=60#square height
screen = pygame.display.set_mode((width, height))#makes the screen without the bar at the top

#Arrays/Lists--------------------------------

#white chess board
chessboard_white=[
			["BR","BN","BB","BQ","BK","BB","BN","BR"],
			["BP","BP","BP","BP","BP","BP","BP","BP"],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			["WP","WP","WP","WP","WP","WP","WP","WP"],
			["WR","WN","WB","WQ","WK","WB","WN","WR"]
			]
#black chess board
chessboard_black=[
			["WR","WN","WB","WK","WQ","WB","WN","WR"],
			["WP","WP","WP","WP","WP","WP","WP","WP"],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			["BP","BP","BP","BP","BP","BP","BP","BP"],
			["BR","BN","BB","BK","BQ","BB","BN","BR"]
			]

#values of each piece
values = {
  "P": 1,
  "N": 3,
  "B": 3,
	"R": 5,
	"Q": 9,
	"K": 0
}

#Arrays/Lists--------------------------------

start=""#player 1's choice, appears at the bottom, either black or white
mode=""#against a computer or against another player
diff=""#hard or easy difficulty