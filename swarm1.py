import random
HOWMANYFISH = 50

def colorgen():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    #check that fish doesnt mix with seawater color
    if (255-blue < 5 and green > 175 and green < 225 and red < 25):
        print("varafisu. Color: Spring green (0,255,127)")
        return (0,255,127)
    newtuple = (red, green, blue)
    return newtuple

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
        summon_fish = Fish(x+1, random.randint(15, 60), random.randint(10,50), colorgen())
    

create_fish(HOWMANYFISH)

import show
show.main(Fish._registry)

'''

for p in Fish._registry:
    print(p)

    print("fisu: {ser}, väritys: {color} !!!".format(ser=p.name, color=p.color))
    print("\n goodjobdickboy!")


'''
