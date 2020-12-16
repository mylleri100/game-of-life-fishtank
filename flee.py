import random
import math

D_MULT=10

#make a list of closest hunters of current x,y loc
def stalkers(hunters, x, y, radius):
    stalkers=set()
    for h in hunters:
        distance=math.sqrt((x-h.x)**2 + (y-h.y)**2)
        if (distance < radius):
            stalkers.add(h)
    #print("mua ahdistaa näin moni: " + str(len(stalkers)))
    return stalkers

def probe(stalkers, x, y):
    dangerlvl=D_MULT*len(stalkers)
    for s in stalkers:
        distance=math.sqrt((x-s.x)**2 + (y-s.y)**2)
        dangerlvl-=distance     ## add if for WW treshold
    return dangerlvl

def find_dir(stalkers, x, y, prey):
    joy1=probe(stalkers, x-1, y-1)
    joy2=probe(stalkers, x, y-1)
    joy3=probe(stalkers, x+1, y-1)
    joy4=probe(stalkers, x+1, y)
    joy5=probe(stalkers, x+1, y+1)
    joy6=probe(stalkers, x, y+1)
    joy7=probe(stalkers, x-1, y+1)
    joy8=probe(stalkers, x-1, y)
    bestlvl=min(joy1,joy2,joy3,joy4,joy5,joy6,joy7,joy8)
    #add worstlvl/dir later
    if probe(stalkers, x-1, y-1) <= bestlvl:
        prey.votes["nw"] = 1 + prey.votes["nw"]        
    if probe(stalkers, x, y-1) <= bestlvl:
        prey.votes["n"] = 1 + prey.votes["n"]
    if probe(stalkers, x+1, y-1) <= bestlvl:
        prey.votes["ne"] = 1 + prey.votes["ne"]
    if probe(stalkers, x+1, y) <= bestlvl:
        prey.votes["e"] = 1 + prey.votes["e"]
    if probe(stalkers, x+1, y+1) <= bestlvl:
        prey.votes["se"] = 1 + prey.votes["se"]
    if probe(stalkers, x, y+1) <= bestlvl:
        prey.votes["s"] = 1 + prey.votes["s"]
    if probe(stalkers, x-1, y+1) <= bestlvl:
        prey.votes["sw"] = 1 + prey.votes["sw"]
    if probe(stalkers, x-1, y) <= bestlvl:
        prey.votes["w"] = 1 + prey.votes["w"]    
        

'''
#roadrunner flee logic
def run_away(rr, 10-radiushunters, direction):
    #3 steps

    #if a hunter closer than 1 empty square, move away 2, 1 original dir

    # prevent move to square 1 empty away from any hunter






for group in fishes:
        for fish in group:
            friend_loc = [50,50]    #init dummy value, can be removed?
            shortest=1000
            for friend in group:
                distance=math.sqrt((guy.x-friend.x)**2 + (guy.y-friend.y)**2)
                if (distance < shortest and distance != 0):
                    shortest=distance
                    friend_loc[0]=friend.x
                    friend_loc[1]=friend.y
            if(shortest > 3 and shortest!=1000):
                if(guy.x < friend_loc[0]):
                    guy.x+=1
                if(guy.x > friend_loc[0]):
                    guy.x-=1
                if(guy.y < friend_loc[1]):
                    guy.y+=1
                if(guy.y > friend_loc[1]):
                    guy.y-=1
                #print("my color is: {c} and my friend {p} km away".format(p=shortest,c=fish.color))




    
    for guy in guys:
        dir=random.randint(1,8)
        if(dir==1):
            guy.x+=speed    #east
        elif(dir==2):
            guy.x-=speed    #west
        elif(dir==3):
            guy.y+=speed    #north
        elif(dir==4):
            guy.y-=speed    #south
        elif(dir==5):
            guy.y+=speed    #ne
            guy.x+=speed
        elif(dir==6):
            guy.y-=speed    #se
            guy.x+=speed
        elif(dir==7):
            guy.y-=speed    #sw
            guy.x-=speed
        elif(dir==8):
            guy.y+=speed    #nw
            guy.x-=speed
        else:
            exit("shithappens")

    
'''

                    

