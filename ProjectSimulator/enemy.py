import random
import pygame as py

global enemyX
global enemyY
def showEnenmy(displayGame,acftIMG,rec_x,rec_y,window_width,window_height):
    # rec_y=random.randrange(10,window_height)
    py.draw.rect(displayGame,acftIMG,[rec_x,rec_y,100,100])


def traffics(displayGame,acftIMG,rec_x,rec_y,window_width,window_height):
    displayGame.blit(acftIMG,(rec_x,rec_y))
    enemyX=rec_x
    enemyY=rec_y
