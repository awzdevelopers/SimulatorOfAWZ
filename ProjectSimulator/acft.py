import pygame as pg



def aircraft(xACFT,yACFT,wnidow_width,window_height,acftimg,color):
    gameDis=pg.display.set_mode((wnidow_width,window_height))
    gameDis.fill(color)
    gameDis.blit(acftimg,(xACFT,yACFT))
