import turtle
from pygame import mixer
import random
dx = 0
dy = 0
chng_pan = 0
usr_1_scor = 0
usr_2_scor = 0
pause = False
mixer.init()
mixer.music.load('C:\\Users\\USER\\Documents\\python\\turtle\\rockpaper scissor\\hit.wav')
def moveBall():
    global dx,dy,usr_1_scor,usr_2_scor,pause,chng_pan
    lim_x,lim_y = (500/2)+30,210
    curr_x,curr_y = ball.pos()
    if curr_x >= lim_x:
        usr_1_scor += 1
        lft_scr_tur.clear()
        lft_scr_tur.write((str(usr_1_scor)),font=('normal',20))
        left_pan.sety(0)
        right_pan.sety(0)
        curr_x,curr_y = 0,0
        dy,dx = 0,0
    if curr_x <= -lim_x:
        usr_2_scor += 1
        rght_scr_tur.clear()
        rght_scr_tur.write((str(usr_2_scor)),font=('normal',20))
        right_pan.sety(0)
        left_pan.sety(0)
        curr_x,curr_y = 0,0
        dy,dx = 0,0
    if curr_y >= lim_y or curr_y <= -lim_y:
        dy*=-1
    if pause or (dy == 0 and dx == 0):
        ball.setpos(curr_x,curr_y)
        chng_pan = 0
    else:
        chng_pan = 15
        ball.setpos(curr_x+dx,curr_y+dy)
    
def move_lft(direc):
    '''
    1 ->positive direction/upward
    -1 ->negative direction/downward
    '''
    global chng_pan
    curr_y = left_pan.ycor()
    curr_y = curr_y + (direc*chng_pan)
    if curr_y >=210-40 and not(curr_y == 209-40 and direc == 1):
        curr_y=209-40
    if curr_y <=-210+40 and not(curr_y == -209+40 and direc == -1):
        curr_y=-209+40
    left_pan.sety(curr_y)
def move_rght(direc):
    '''
    1 ->positive direction/upward
    -1 ->negative direction/downward
    '''
    global chng_pan
    curr_y = right_pan.ycor()
    curr_y = curr_y + (direc*chng_pan)
    if curr_y >=210-40 and not(curr_y ==209-40 and direc == 1):
        curr_y=209-40
    if curr_y <=-210+40 and not(curr_y == -209+40 and direc == -1):
        curr_y=-209+40
    right_pan.sety(curr_y)
def collision():
    global dx,dy
    ball_x,ball_y = ball.pos()
    left_x,left_y = left_pan.pos()
    right_x,right_y = right_pan.pos()
    if ((ball_x <= left_x + 2.5 and ball_y >left_y-40) and (ball_x <= left_x - 2.5 and ball_y < left_y+40)):
        mixer.music.play()
        dx = float(random.randint(8,15)/10)
        dy = 1.5-dx
    if ((ball_x >= right_x - 2.5 and ball_y >right_y-40) and (ball_x >= right_x + 2.5 and ball_y < right_y+40)):
        mixer.music.play()
        dx = float(random.randint(8,15)/10)
        dy = 1.5-dx
        dx *=-1

def start_game():
    global dx,dy
    if dx == 0 and dy == 0:
        dx = float(random.randint(8,15)/10)
        dy = 1.5-dx
def pause_func():
    global pause
    pause = True
def cntinu():
    global pause
    pause = False
'''
Main window
'''
scr = turtle.Screen()
scr.bgcolor('black')
scr.title('ping pong')
scr.setup(550,550)
scr.tracer(0)
ball = turtle.Turtle('circle')
ball.color('white')
ball.shapesize(0.7,0.7)
ball.penup()
ball.speed(0)
lft_scr_tur = turtle.Turtle('blank')
lft_scr_tur.setpos(-50,230)
lft_scr_tur.color('white')
lft_scr_tur.write((str(usr_1_scor)),font=('normal',20))
rght_scr_tur = turtle.Turtle('blank')
rght_scr_tur.setpos(50,230)
rght_scr_tur.color('white')
rght_scr_tur.write((str(usr_2_scor)),font=('normal',20))
strt_lbl = turtle.Turtle('blank')
strt_lbl.setpos(-100,-100)
strt_lbl.color('white')

left_pan = turtle.Turtle('square')
left_pan.resizemode('user')
left_pan.penup()
left_pan.color('white')
left_pan.shapesize(4,0.5)
left_pan.setpos((-240,0))
left_pan.speed(0)
right_pan = turtle.Turtle('square')
right_pan.penup()
right_pan.color('white')
right_pan.shapesize(4,0.5)
right_pan.setpos((240,0))
left_pan.speed(0)
line_tur = turtle.Turtle('blank')
line_tur.setpos(0,210)
line_tur.color('white')
line_tur.goto(0,-210)
line_tur.goto(225,-210)
line_tur.goto(225,210)
line_tur.goto(-225,210)
line_tur.goto(-225,-210)
line_tur.goto(0,-210)
#bind the keyboard
scr.listen()
scr.onkeypress(lambda:move_lft(1),'w')
scr.onkeypress(lambda:move_lft(-1),'s')
scr.onkeypress(lambda:move_rght(1),'Up')
scr.onkeypress(lambda:move_rght(-1),'Down')
scr.onkeypress(lambda:start_game(),'space')
scr.onkeypress(pause_func,'p')
scr.onkeypress(cntinu,'c')

while True:
    try:
        moveBall()
        collision()
        scr.update()
        if dx == 0 and dy == 0:
            chng_pan = 0
            strt_lbl.write('Press Space to start\nPress \'p\' to pause\nPress \'c\' to continue',font=('normal',20))
        else:
            strt_lbl.clear()
    except:
        break