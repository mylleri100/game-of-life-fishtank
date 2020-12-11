#grid info (passed to show-module)
GRID_SIZE=160
HUNTER_SIZE=6
PREYCOLOR=(0,0,255) #BLUE
HUNTERCOLOR=(220,20,0) #RED
HOWMANYHUNTER = 20

#system modules
from random import randint
from time import sleep

#project modules
import hunt
import flee

class Lifeform(object):
    _registry = set()
    def __init__(self, name, x, y,color):
        self.name = name    # serial number for now
        self.x = x
        self.y = y
        self.color = color
         
class Hunter(Lifeform):   
    def __init__(self, name, x, y, color):
        super().__init__(name, x, y, color)
        self._registry.add(self)

class Prey(Lifeform):   
    def __init__(self, x, y):
        super().__init__("Roadrunner", x, y, PREYCOLOR)
        
def create_hunter(amount):
    for x in range(amount):
        #hunter is assigned serial number and location on grid
        summon_hunter = Hunter(x+1, randint(10, 125), randint(5,125), HUNTERCOLOR)

create_hunter(HOWMANYHUNTER)
#list of all hunters
hunters=Hunter._registry
#list of all lifeforms to display
lf=hunters.copy()

prey=Prey((GRID_SIZE/2),(GRID_SIZE/2))
#print("uusi paisti kohdassa x:{x} y:{y}".format(x=prey.x, y=prey.y))
lf.add(prey)    #add prey to lifeforms for visual display

import show
screen=show.init_tank(lf, GRID_SIZE, HUNTER_SIZE)
while(True):
    sleep(0.2)
    hunt.move(hunters,1)
    badguys=flee.stalkers(hunters, prey.x, prey.y)
    
    show.run_tank(screen,lf, GRID_SIZE, HUNTER_SIZE)
    
