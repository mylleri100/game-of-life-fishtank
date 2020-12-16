import random
import math

#move single lifeform
def move(guy, dir):        
        if(dir=='e'):
            guy.x+=1    #east
        elif(dir=='w'):
            guy.x-=1    #west
        elif(dir=='s'):
            guy.y+=1    #south
        elif(dir=='n'):
            guy.y-=1    #north
        elif(dir=='se'):
            guy.y+=1    #se
            guy.x+=1
        elif(dir=='ne'):
            guy.y-=1    #ne
            guy.x+=1
        elif(dir=='nw'):
            guy.y-=1    #nw
            guy.x-=1
        elif(dir=='sw'):
            guy.y+=1    #sw
            guy.x-=1
        else:
            exit("shithappens")

#random movement
def random_move(guys):
    for guy in guys:
        dir=random.randint(1,8)
        if(dir==1):
            guy.x+=1    #east
        elif(dir==2):
            guy.x-=1    #west
        elif(dir==3):
            guy.y+=1    #south
        elif(dir==4):
            guy.y-=1    #north
        elif(dir==5):
            guy.y+=1    #se
            guy.x+=1
        elif(dir==6):
            guy.y-=1    #ne
            guy.x+=1
        elif(dir==7):
            guy.y-=1    #nw
            guy.x-=1
        elif(dir==8):
            guy.y+=1    #sw
            guy.x-=1
        else:
            exit("shithappens")
'''

#fishes here is list of lists (of fish objects)
#returns the coordinates for closest fish friend (same color)
def meetfriends(fishes):    
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
                    
                    
'''
