import pygame as py
import random
from acft import aircraft
import enemy
import checkPOINTS
import Labels

py.init()
# window dims
window_width=800
window_height=600

leftmouseX=0
leftmouseY=0
# POINTS
EGVAX=(430, 29)
ITIBI=(536, 112)
GODMO=(308, 536)
GABSU=(95, 518)


# blip dims
b_width=window_width*0.45
b_hieght=window_height*.8

# acft x y
acftX=400
acftY=400
# rec_x=random.randrange(0, window_width)
# enemy 1
rec_x=EGVAX[0]
rec_y=EGVAX[1]
leftIAF=False
# enenmy 2
rec_x2=ITIBI[0]
rec_y2=ITIBI[1]

black=(0,0,0)
green=(0,255,0)
white=(255,255,255)
displayGame=py.display.set_mode((window_width, window_height))
# Surface1=py.Surface((window_width,window_height))
py.display.set_caption('simulator')
clock=py.time.Clock()

iaf=py.image.load('acft.png')
acft1=py.image.load('acft1.png')
acft2=py.image.load('acft2.png')
# aircraft

# text

# acft
x=0
crashed=False
# circle


while not crashed:



    for evevt in py.event.get():

        if evevt.type==py.QUIT:
            crashed=True

    # displayGame.fill(green)
    # aircraft(b_width,b_hieght,window_width,window_height,acft1,green)
    # py.display.update()
    # for i in range(10,50,5 ):
        if evevt.type==py.KEYDOWN:
            if evevt.key==py.K_LEFT:
                x=-5
            elif evevt.key==py.K_RIGHT:
                x=5

        if evevt.type==py.KEYUP:
           if evevt.key==py.K_LEFT or evevt.key==py.K_RIGHT:
                x=0



    acftX+=x

    aircraft(acftX,acftY,window_width,window_height,iaf,green)
    # drawCTR
    py.draw.circle(displayGame,(0,50,120),(300,300),300)
    py.draw.line(displayGame,(0,10,10),(599,294),(251,596),5)
    py.draw.line(displayGame,(10,90,0),(268,269),(341,328),5)
    Labels.showLabelRWY("30", displayGame, 341, 328)
    Labels.showLabelRWY("12", displayGame, 260, 269)
    Labels.showLabelRWY("AWZ DVOR", displayGame, 270, 280)
    Labels.showLabelRWY("EGVAX", displayGame, 430, 29)
    Labels.showLabelRWY("ITIBI", displayGame, 536, 112)
    Labels.showLabelRWY("GODMO", displayGame, 308, 536)
    Labels.showLabelRWY("GABSU", displayGame, 95, 518)
    # ROUTES
    py.draw.line(displayGame,(10,90,0),(430,29),(314,305),5)
    py.draw.line(displayGame,(10,90,0),(536,112),(314,305),5)
    py.draw.line(displayGame,(10,90,0),(308,536),(314,305),5)
    py.draw.line(displayGame,(10,90,0),(95,518),(314,305),5)










    enemy.traffics(displayGame,acft1,rec_x,rec_y,window_width,window_height)
    enemy.traffics(displayGame,acft2,rec_x2,rec_y2,window_width,window_height)
    Labels.showLabelACFT("IZG4012",displayGame, rec_x2-10, rec_y2-10)
    Labels.showLabelACFT("IRA412",displayGame, rec_x-10, rec_y-10)

    # EGAVX
    rec_x+=-.05
    rec_y=(-277/116*rec_x)+61237/58
    # rec_y+=.05
    #
    if evevt.type==py.MOUSEBUTTONDOWN:
        print(str(evevt.pos))
        print(str(evevt.button))
        leftmouseX,leftmouseY=evevt.pos
        # print("correct left pos"+str(leftmouseX)+":"+str(leftmouseY))
        print("acft2 X"+str(rec_x2)+" :: "+"mouse X"+str(leftmouseX))
        if ((rec_x2)<leftmouseX and leftmouseX<((rec_x2)+50)) and ((rec_y2)<leftmouseY and leftmouseY<((rec_y2)+30)):
            print("equallllllll???")

            # if ((rec_x2)<leftmouseX and leftmouseX<((rec_x2)+50)):
            #     print("acft1 equal x and y")
    if checkPOINTS.checkIAF(rec_x,rec_y,acftX,acftY,leftIAF):
       leftIAF=True


    rec_y2+=0.005
    rec_x2+=.05
    # label above
    Labels.TitleOfSim("AWZ Simulator",displayGame)
    # if rec_y >= window_height:
    #     rec_y=0
    #     rec_x=random.randrange(0,window_width)
    # if rec_y+100> b_hieght:
    #     crashed=True
    if leftIAF:
        Labels.Messages("left iaf", displayGame)



    py.display.update()
    clock.tick(60)

py.quit()
quit()
