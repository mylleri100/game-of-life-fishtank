import random
import math

#random movement
def move(guys, speed):
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
                    
                    

