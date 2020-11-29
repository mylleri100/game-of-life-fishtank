#grid info (passed to show-module)
GRID_SIZE=200
FISH_SIZE=6
HOWMANYFISH = 500

#system modules
from random import randint
from time import sleep

#project modules
import swim
import color1
         

class Fish(object):
    _registry = set()
    
    def __init__(self, name, x, y,color):
        self._registry.add(self)
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        
def create_fish(amount):
    for x in range(amount):
        #fish is assigned serial number, location on grid 0-49, and random color
        summon_fish = Fish(x+1, randint(10, 125), randint(5,125), color1.colorgen())
    
create_fish(HOWMANYFISH)
#list of all fish
fishes=Fish._registry
#list of lists with same color fish a.k.a friends
friends=color1.sort_fish_by_color(Fish._registry)

import show
screen=show.init_tank(fishes, GRID_SIZE, FISH_SIZE)
while(True):
    sleep(0.1)
    swim.meetfriends(friends)
    swim.swim_nemo_swim(fishes)
    show.run_tank(screen,fishes, GRID_SIZE, FISH_SIZE)
    
