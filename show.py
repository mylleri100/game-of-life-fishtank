## produces visual of Fishtank

import pygame

TITLE = "Fish Tank"
WIDTH = 800
HEIGHT = 700
FPS = 100
SEAWATER = (0, 200, 255)
#BLACK = (0, 195, 250)   
BLACK = (0, 0, 0)   

## grid code
def init_tank(fishes, grid_size, cell_size):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    screen.fill(SEAWATER)

    for line in range(grid_size):
        pos = line * cell_size
        pygame.draw.line(screen, BLACK, (0, pos), (WIDTH, pos))
    for col in range(grid_size):
        pos = col * cell_size
        pygame.draw.line(screen, BLACK, (pos,0), (pos, HEIGHT))
    
    ##filling fish
    for fish in fishes:
        pygame.draw.rect(screen,fish.color,(fish.x*cell_size, fish.y*cell_size, cell_size, cell_size))
    pygame.display.flip()
    return screen

def run_tank(screen, fishes, grid_size, cell_size):
    screen.fill(SEAWATER)
    for line in range(grid_size):
        pos = line * cell_size
        pygame.draw.line(screen, BLACK, (0, pos), (WIDTH, pos))
    for col in range(grid_size):
        pos = col * cell_size
        pygame.draw.line(screen, BLACK, (pos,0), (pos, HEIGHT))
    
    ##filling fish
    for fish in fishes:
        pygame.draw.rect(screen,fish.color,(fish.x*cell_size, fish.y*cell_size, cell_size, cell_size))

    # *after* drawing everything, flip the display
    pygame.display.flip()
