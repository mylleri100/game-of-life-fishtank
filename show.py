## produces visual of Fishtank

import random
import pygame
import os
import time

TITLE = "Fish Tank"
WINDOWS_LOCATION = '100,100'
WIDTH = 800
HEIGHT = 700
FPS = 5

SEAWATER = (0, 200, 255)
BLACK = (0, 195, 250)

LINES=200
COLUMNS=200

SIZE=10
MARGIN= 2

def swim_nemo_swim(fishes):
    for fish in fishes:
        dir=random.randint(1,4)
        if(dir==1):
            fish.x+=2    #right
        elif(dir==2):
            fish.x-=2    #left
        elif(dir==3):
            fish.y+=2    #up
        elif(dir==4):
            fish.y-=2    #down
        else:
            exit("shithappens")

## grid code
def main(fishes):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    running = True
    cell_size=SIZE
    
    while running:
    
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(SEAWATER)

        for line in range(LINES):
            pos = MARGIN + line * cell_size
            pygame.draw.line(screen, BLACK, (MARGIN, pos), (WIDTH, pos))
        for col in range(COLUMNS):
            pos = MARGIN + col * cell_size
            pygame.draw.line(screen, BLACK, (pos,MARGIN), (pos, HEIGHT))
        
        ##filling fish
        for fish in fishes:
            pygame.draw.rect(screen,fish.color,(fish.x*cell_size+MARGIN, fish.y*cell_size+MARGIN, cell_size, cell_size))

        # *after* drawing everything, flip the display
        pygame.display.flip()
        #move all little fish each FPS
        swim_nemo_swim(fishes)
        
        
    pygame.quit()
