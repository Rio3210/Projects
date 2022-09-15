import pygame, sys
import numpy as np
pygame.init()
width=600  #You can modify the screen size 
height=600
board_rows=3
board_cols=3
BG_color=(235, 134, 52)
line_color=(255, 255, 255)
line_width=15
circle_radius=60
circle_width=15
circle_color=(15, 15, 15)
cross_width=25
space=55
cross_color=(15, 15, 15)
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_color)

#board
board=np.zeros((board_rows,board_cols))

def draw_lines():
    pygame.draw.line(screen,line_color,(0,200),(600,200),line_width)
    pygame.draw.line(screen,line_color,(0,400),(600,400),line_width)

    pygame.draw.line(screen,line_color,(200,0),(200,600),line_width)
    pygame.draw.line(screen,line_color,(400,0),(400,600),line_width)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col]==1:
                pygame.draw.circle(screen,circle_color,(int(col*200+100),int(row*200+100)),circle_radius,circle_width)
            elif board[row][col]==2:
                pygame.draw.line(screen,cross_color,(col*200 +space,row*200+200-space),(col*200+200-space,row*200+space),cross_width)
                pygame.draw.line(screen,cross_color,(col*200 +space,row*200+space),(col*200+200-space,row*200+200-space),cross_width)
            
def mark_square(row,col,player):
    board[row][col]=player
def available_square(row,col):
    if board[row][col]==0:
        return True
    else:
        return False

def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col]==0:
                return False
    return True

def check_win(player):
    #vertical win
    for col in range(board_cols):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_wining_line(col,player)
            return True
    #horizonatal win
    for row in range(board_rows):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_wining_line(row,player)
            return True
    #diagonal
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagonal(player)
        return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_des_diagonal(player)
        return True

    return False
def draw_vertical_wining_line(col,player):
    posx=col*200+100

    if player==1:
        color=circle_color
    elif player==2:
        color=cross_color
    
    pygame.draw.line(screen,color,(posx,15),(posx,height-15),15)
def draw_horizontal_wining_line(row,player):
    posy=row*200+100
    if player==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen,color,(15,posy),(width-15,posy),15)
    
def  draw_asc_diagonal(player):
    if player==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen,color,(15,height-15),(width-15,15),15)
def draw_des_diagonal(player):
    if player==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen,color,(15,15),(width-15,height-15),15)

def restart():
    screen.fill(BG_color)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col]=0
draw_lines()

player=1
game_over=False
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:

            mousex=event.pos[0]
            mousey=event.pos[1]

            clicked_row=int(mousey//200)
            clicked_col=int(mousex//200)

            if available_square(clicked_row,clicked_col):
                mark_square(clicked_row,clicked_col,player)
                if check_win(player):
                    game_over=True
                player=player%2+1
                draw_figures()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
                game_over=False
                player=1
    pygame.display.update()