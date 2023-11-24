import numpy as np
import pygame 

from enum import Enum 
import os   

from params import * 
from enviroment import * 
from node import *  
from agent import * 

# initialize:
FPS = 60
pygame.init()
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Search Game") 

maze_path = './Maze.npy' 
Maze = np.load(maze_path)

state = {}
state['board'] = Maze 
state['agent'] = (6, 0) 
state['end'] = (12,0)
root = Node(father=None, state=state) 

def main(): 
 
    run = True
    clock = pygame.time.Clock()
    WIN.fill(colors.black) 
    
    # setting start and end point :
    start = {'x': 6, 'y': 0}
    end = {'x': 12, 'y': 0}  
    gameBoard = Board(start, end, Maze) 

    agent = Agent(root) 
    path = agent.fs('d')  

    path_color(gameBoard, path)  
    print(path) 
    
    maze_changed = False 

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
        
            pos = pygame.mouse.get_pos()  # gets the current mouse coords
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(rows):
                    for j in range(cols):
                        rect = gameBoard.boardArray[i][j]
                        if rect.is_inside_me(pos):
                
                            if event.button == 1: 
                                maze_changed = True
                                Maze[j,i] = 0  
                                gameBoard = Board(start, end, Maze)   
                                root.state['board'] = Maze 
                                agent = Agent(root) 
                                    
                            if event.button == 3: 
                                maze_changed = True
                                Maze[j,i] = 1 
                                gameBoard = Board(start, end, Maze) 
                                root.state['board'] = Maze 
                                agent = Agent(root) 
                                    
                                
            if maze_changed : 
                path = agent.fs('d')
                print(path)                
                path_color(gameBoard, path)  
                maze_changed = False
                                
            
            gameBoard.draw_world(WIN)

    pygame.quit() 


main()