RED=(255,0,0)
LIME=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(127,255,212)

from random import randint

def colorgen():
    color=randint(1,5)
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
        print("this cannot be happening...")
        exit("this cannot be happening...")

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

