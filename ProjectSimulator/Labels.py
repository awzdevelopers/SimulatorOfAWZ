import pygame as py

def TitleOfSim(title,displayGame):
    font=py.font.SysFont("B-Zar",25)
    text=font.render(title,True,(50,200,155))
    displayGame.blit(text,(50,50))

def Messages(title,displayGame):
    font=py.font.SysFont("B-Zar",25)
    text=font.render(title,True,(50,0,155))
    displayGame.blit(text,(300,300))

# def drawCTR(position,radius,color,displaygame,Surface1):
#     Surface2=py.Surface((300,300))
#     Surface1.fill((0,0,200))
#     py.draw.circle(Surface1, color, position, radius)
#     py.blit
def showLabelACFT(info,displayGame,x,y):
    font=py.font.SysFont("B-Zar",25)
    text=font.render(info,True,(0,0,0))
    displayGame.blit(text,(x,y))

def showLabelRWY(info,displayGame,x,y):
    font=py.font.SysFont("B-Zar",25)
    text=font.render(info,True,(0,0,0))
    displayGame.blit(text,(x,y))
