#coding: utf-8
import pygame
from pygame.locals import Rect, Color, QUIT
import sys

SCR_RECT = Rect(0, 0, 800, 800)
CS = 5  # セルサイズ
NUM_ROW = SCR_RECT.height / CS
NUM_COL = SCR_RECT.width / CS

# 各状態の色
state2color = ["black", "blue", "red", "green", "yellow", "magenta", "white", "cyan"]

class CancerModel
	def CND(X):

	    (a1,a2,a3,a4,a5) = (0.31938153, -0.356563782, 1.781477937, 

	     -1.821255978, 1.330274429)
	    L = abs(X)

	    K = 1.0 / (1.0 + 0.2316419 * L)

	    w = 1.0 - 1.0 / sqrt(2*pi)*exp(-L*L/2.) * (a1*K + a2*K*K + a3*pow(K,3) +

	    a4*pow(K,4) + a5*pow(K,5))
	    if X<0:

	        w = 1.0-w

	    return w
	    # Black Sholes Function

	def BlackSholes(CallPutFlag,S,X,T,r,v):

	    d1 = (log(S/X)+(r+v*v/2.)*T)/(v*sqrt(T))

	    d2 = d1-v*sqrt(T)
	    if CallPutFlag=='c':

	        return S*CND(d1)-X*exp(-r*T)*CND(d2)

	    else:

	        return X*exp(-r*T)*CND(-d2)-S*CND(-d1)
	    

	def __init__(self):
		 pygame.init()
		 self.screen = pygame.display.set_mode(SCR_RECT.size)
		 pygame.display.set_caption("CancerModel")

		# フィールドを作成
		self.field = [[0 for x in range(NUM_COL)] for y in range(NUM_ROW)]

		# 状態を初期化
		self.init()
		
		self.mainLoop()
		
	def init(self)
		offset = (NUM_ROW - len(CancerModel)) / 2
		for y in range(len(CancerModel)):
			for x in range(len(CancerModel)):
				self.field[y + offset][x + offset - 10] = CancerModel[y][x]
				
	def update(self)
		nextField = [[0 for x in range(NUM_COL)] for y in range(NUM_ROW)]
		        for y in range(NUM_ROW):
		            for x in range(NUM_COL):
						try:
							  self.field[y][x] =
							  self.field[y - 1][x] =
							  self.field[y][x + 1] =
							  self.field[y + 1][x] =
					          self.field[y][x - 1] =
