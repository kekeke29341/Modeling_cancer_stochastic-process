#coding:utf-8
import Image, ImageDraw, ImageFont
import numpy as np
from pylab import *
import random
import math

state2color = ["black", "blue", "red", "green", "yellow", "magenta", "white", "cyan"]


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
    


def ca(width, height):
    """1次元セルオートマトンの図を描画"""
    results = []

    # 初期状態（中央のセルだけON）
    first_row = [0] * width
    for i in range(width):
	  S = random.randint(13000, 15000)
	  X = random.randint(10000, 12000)
	  T = random.random()
	  r = 0.44
	  v = 0.01
	  first_row[i] = BlackSholes('c',S,X,T,r,v)
	
    
   
    results.append(first_row)

    for i in range(height - 1):
        old_row = results[-1]
        new_row = []
        for j in range(width):
            # widthの剰余を取るのは、端同士がつながっているため
            n = 4 * old_row[(j-1)%width] + 2 * old_row[j] + old_row[(j+1)%width]
            if old_row[j-1] < old_row[j]:
               new_row.append(old_row[j])
               results.append(new_row)
            else: 
				new_row.append(old_row[j-1])
				results.append(new_row)
    return results

def render(results, width, height, filename="ca12.png"):
    """セルオートマトンを描画"""
    img = Image.new("RGB", (width, height), (255,255,255))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        for x in range(width):
            if results[y][x] > results[y][x-1]:
                draw.point((x, y), (30, 30, 30))
    img.save(filename, "PNG")

if __name__ == "__main__":
    width, height = 300, 150
    results = ca(width, height)
    render(results, width, height)
 


