import sys
import copy
import numpy as np
import pygame
import random
from constant import *


pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Tic Tac Toe Ai")
screen.fill(BG_color)

class Board:
    def __init__(self):
        self.squares=np.zeros((rows,cols))
        self.empty_sqrs=self.squares
        self.marked_sqrs=0
    
    def final_state(self,show=False):
        #vertical wins
        for col in range(cols):
            if self.squares[0][col]==self.squares[1][col]==self.squares[2][col]!=0:
                if show:
                    color=circle_color if self.squares[0][col]==2 else cross_color
                    ipos=(col*sqsize+sqsize//2,20)
                    fpos=(col*sqsize+sqsize//2,height-20)
                    pygame.draw.line(screen,color,ipos,fpos,cross_width)
                return self.squares[0][col]
        #horizonatal win
        for row in range(rows):
                if self.squares[row][0]==self.squares[row][1]==self.squares[row][2]!=0:
                    if show:
                        color=circle_color if self.squares[row][0]==2 else cross_color
                        ipos=(20,row*sqsize+sqsize//2)
                        fpos=(width-20,row*sqsize+sqsize//2)
                        pygame.draw.line(screen,color,ipos,fpos,cross_width)
                    return self.squares[row][0]
        #diagonal win

        if self.squares[0][0]==self.squares[1][1]==self.squares[2][2]!=0:
            if show:
                color=circle_color if self.squares[1][1]==2 else cross_color
                ipos=(20,20)
                fpos=(width-20,height-20)
                pygame.draw.line(screen,color,ipos,fpos,cross_width)           
            return self.squares[1][1]
        
        if self.squares[2][0]==self.squares[1][1]==self.squares[0][2]!=0:
            if show:
                color=circle_color if self.squares[1][1]==2 else cross_color
                ipos=(20,height-20)
                fpos=(width-20,20)
                pygame.draw.line(screen,color,ipos,fpos,cross_width)
            return self.squares[1][1]
        #no win return 0
        return 0
    def mark_sqr(self,row,col,player):
        self.squares[row][col]=player
        self.marked_sqrs+=1
    def empty_sqr(self,row,col):
        return self.squares[row][col]==0
    def get_empty_sqrs(self):
        empty_sqrs=[]
        for row in range(rows):
            for col in range(cols):
                if self.empty_sqr(row,col):
                    empty_sqrs.append((row,col))
        return empty_sqrs
    def isfull(self):
        return self.marked_sqrs==9
    def isempty(self):
        return self.marked_sqrs==0
class AI:
    def __init__(self,level=1,player=2):
        self.level=level
        self.player=player
    def rnd(self,board):
        empty_sqrs=board.get_empty_sqrs()
        idx=random.randrange(0,len(empty_sqrs))
        return empty_sqrs[idx]
    
    def minmax(self,board,maximizing):
        #terminal_case
        case=board.final_state()

        if case==1:
            return 1, None
        if case==2:
            return -1, None
        elif board.isfull():
            return 0, None
        if maximizing:
            max_eval=-100
            best_move=None
            empty_sqrs=board.get_empty_sqrs()
            for (row,col) in empty_sqrs:
                temp__board=copy.deepcopy(board)
                temp__board.mark_sqr(row,col,1)
                eval=self.minmax(temp__board,False)[0]

                if eval>max_eval:
                    max_eval=eval
                    best_move=(row,col)
            return max_eval, best_move
        elif not maximizing:
            min_eval=100
            best_move=None
            empty_sqrs=board.get_empty_sqrs()
            for (row,col) in empty_sqrs:
                temp__board=copy.deepcopy(board)
                temp__board.mark_sqr(row,col,self.player)
                eval=self.minmax(temp__board,True)[0]

                if eval<min_eval:
                    min_eval=eval
                    best_move=(row,col)
            return min_eval, best_move
    def eval(self,main_board):
        if self.level==0:
            eval='random'
            move=self.rnd(main_board)
        #min_max
        else:
            eval,move=self.minmax(main_board,False)
        print(f'AI has choosen to mark the square in pos{move} with an eval of:{eval}')
        return move
class Game:
    def __init__(self):
        self.player=1
        self.board=Board()
        self.ai=AI()
        self.running=True
        self.show_lines()
        self.gamemode='ai'
    def make_move(self,row,col):
        self.board.mark_sqr(row,col,self.player)
        self.draw_fig(row,col)
        self.next_turn()        
    def show_lines(self):
        screen.fill(BG_color)
        pygame.draw.line(screen,line_color,(sqsize,0),(sqsize,height),line_width)
        pygame.draw.line(screen,line_color,(width-sqsize,0),(width-sqsize,height),line_width)

        pygame.draw.line(screen,line_color,(0,sqsize),(width,sqsize),line_width)
        pygame.draw.line(screen,line_color,(0,height-sqsize),(width,height-sqsize),line_width)
    def draw_fig(self,row,col):
        if self.player==1:
            #draw cross
            #descending
            start_desc=(col*sqsize+offset,row*sqsize+offset)
            end_desc=(col*sqsize+sqsize-offset,row*sqsize+sqsize-offset)
            pygame.draw.line(screen,cross_color,start_desc,end_desc,cross_width)

            #ascending
            start_asc=(col*sqsize+offset,row*sqsize+sqsize-offset)
            end_asc=(col*sqsize+sqsize-offset,row*sqsize+offset)
            pygame.draw.line(screen,cross_color,start_asc,end_asc,cross_width)


        elif self.player==2:
            #draw circle
            center=(col*sqsize+sqsize//2,row*sqsize+sqsize//2)
            pygame.draw.circle(screen,circle_color,center,circle_radius,circle_width)
            
    def next_turn(self):
        self.player=self.player%2+1
    def change_gamemode(self):
        self.gamemode='ai' if self.gamemode=='pvp' else 'pvp'
    def isover(self):
        return self.board.final_state(show=True)!=0 or self.board.isfull()

    def reset(self):
        self.__init__()
def main():

    game=Game()
    board=game.board
    ai=game.ai
    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_g:
                    game.change_gamemode()
                if event.key==pygame.K_r:
                    game.reset()
                    board=game.board
                    ai=game.ai

                if event.key==pygame.K_b:
                    ai.level=0
                if event.key==pygame.K_l:
                    ai.level=1
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos
                row=pos[1]//sqsize
                col=pos[0]//sqsize

                if board.empty_sqr(row,col) and game.running:
                    game.make_move(row,col)

                    if game.isover():
                        game.running=False    
        if game.gamemode=='ai' and game.player==ai.player and game.running:
            pygame.display.update()

            row,col=ai.eval(board)
            game.make_move(row,col) 
            if game.isover():
                game.running=False
        pygame.display.update()
main()