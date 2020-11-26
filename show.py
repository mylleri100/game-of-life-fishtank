## produces visual of Fishtank

import swim
import pygame
import os
import time

TITLE = "Fish Tank"
WIDTH = 800
HEIGHT = 700
FPS = 100

SEAWATER = (0, 200, 255)
BLACK = (0, 195, 250)

LINES=200
COLUMNS=200

SIZE=6
MARGIN= 2


## grid code
def main(fishes, friends):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    running = True
    cell_size=SIZE
    sp=15
    
    while running:
        if(sp<0):  
            clock.tick(FPS)
        else:
            clock.tick(5)
            sp-=1
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
        swim.meetfriends(friends)
        swim.swim_nemo_swim(fishes)
        
        
        
    pygame.quit()
