#grid info (passed to show-module)
GRID_SIZE=160
HUNTER_SIZE=6
PREYCOLOR=(0,0,255) #BLUE
HUNTERCOLOR=(220,20,0) #RED
HOWMANYHUNTER = 200

PREY_SPEED=3
LW=5 # Long-range scanner weight for AI
RADIUS=40
WIMPY=5 # should be at least 5 to work
WW=7 # Shortest scanner (WIMPY) weight for AI

#system modules
from random import randint
from time import sleep

#project modules
import hunt
import flee
import appz

class Lifeform(object):
    _registry = set()
    def __init__(self, name, x, y,color):
        self.name = name    # serial number for now
        self.x = x
        self.y = y
        self.color = color
        # votes for where to move next (AI)
        self.votes = {'nw':0, 'n':0, 'ne':0, 'e':0, 'se':0, 's':0, 'sw':0, 'w':0}

         
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
        Hunter(x+1, randint(10, 125), randint(5,125), HUNTERCOLOR)

create_hunter(HOWMANYHUNTER)
hunters = Hunter._registry
#list of all lifeforms to display
lf = hunters.copy()

prey = Prey((GRID_SIZE/2),(GRID_SIZE/2))
lf.add(prey)    #add prey to lifeforms for visual display

import show
screen = show.init_tank(lf, GRID_SIZE, HUNTER_SIZE)
while(True):
    for i in range(PREY_SPEED):
        radius=RADIUS  
        stalkers=flee.stalkers(hunters, prey.x, prey.y, radius)
        for j in range(LW):         ## LONG RANGE SCANNER ROUNDS, LW times
            flee.find_dir(stalkers, prey.x, prey.y, prey)
        #print(prey.votes)
        radius/=2
        while(radius > WIMPY):      ## MID-RANGE SCANNER ROUNDS, fixed weight 1 
            stalkers=flee.stalkers(hunters, prey.x, prey.y, radius)
            flee.find_dir(stalkers, prey.x, prey.y, prey)        
            #print(prey.votes)
            radius-=2
        for j in range(WW):         ## VERY SHORT RANGE SCANNER ROUNDS, WW times
            stalkers=flee.stalkers(hunters, prey.x, prey.y, radius)
            flee.find_dir(stalkers, prey.x, prey.y, prey)    
        
        
        hunt.move(prey, appz.high_key(prey.votes))    
        for k in prey.votes:
            prey.votes[k] = 0    
        show.run_tank(screen,lf, GRID_SIZE, HUNTER_SIZE)
        sleep(0.1)
    
    hunt.random_move(hunters) 
        
    show.run_tank(screen,lf, GRID_SIZE, HUNTER_SIZE)


    #print("mun mesta x:{x} y:{y}".format(x=prey.x, y=prey.y))
    #print("meen jos jaksan x:{x} y:{y}".format(x=new_x, y=new_y))