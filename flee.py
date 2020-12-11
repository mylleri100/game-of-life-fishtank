import random
import math

WIMPY_RADIUS=25

#make a list of closest hunters of current x,y loc
def stalkers(hunters, x, y):
    stalkers=set()
    for h in hunters:
        distance=math.sqrt((x-h.x)**2 + (y-h.y)**2)
        if (distance < WIMPY_RADIUS):
            stalkers.add(h)
    #print("mua ahdistaa näin moni: " + str(len(stalkers)))
    return stalkers


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

                    

