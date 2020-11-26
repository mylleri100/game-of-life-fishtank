RED=(255,0,0)
LIME=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(127,255,212)

HOWMANYFISH = 500
import random

def colorgen():
    color=random.randint(1,5)
    if (color==1):
        return RED
    elif (color==2):
        return LIME
    elif (color==3):
        return BLUE
    elif (color==4):
        return YELLOW
    elif (color==5):
        return CYAN
    else:
        print("shit happens...")
        exit("shit happens")

## refine a new list of lists based on fish color
##stackoverflow.com/questions/17620537/making-an-array-of-sets-in-python
def sort_fish_by_color(fishes):
    sorted = [set() for i in range(5)]
    for fish in fishes:
        if fish.color == RED:
            sorted[0].add(fish)
        elif fish.color == LIME:
            sorted[1].add(fish)            
        elif fish.color == BLUE:
            sorted[2].add(fish)
        elif fish.color == YELLOW:
            sorted[3].add(fish)
        elif fish.color == CYAN:
            sorted[4].add(fish)
        else:
            print("no such color, what went wrong...")
    return sorted
    #amount=len(sorted[0])
    #print("number of red: {n}".format(n=amount))
            

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
        #fish is assigned serial number, which square on grid 0-49, and random color
        summon_fish = Fish(x+1, random.randint(10, 125), random.randint(5,125), colorgen())
    
create_fish(HOWMANYFISH)
all_fish=Fish._registry
color_sorted=sort_fish_by_color(Fish._registry)

import show
show.main(all_fish, color_sorted)

'''

for p in Fish._registry:
    print(p)

    print("fisu: {ser}, väritys: {color} !!!".format(ser=p.name, color=p.color))
    print("\n goodjobdickboy!")


'''
