import random
import math

#fishes here is list of fish objects
def swim_nemo_swim(fishes):
    for fish in fishes:
        dir=random.randint(1,4)
        if(dir==1):
            fish.x+=1    #right
        elif(dir==2):
            fish.x-=1    #left
        elif(dir==3):
            fish.y+=1    #up
        elif(dir==4):
            fish.y-=1    #down
        else:
            exit("shithappens")

#fishes here is list of lists (of fish objects)
#returns the coordinates for closest fish friend (same color)
def meetfriends(fishes):    
    for group in fishes:
        for fish in group:
            friend_loc = [50,50]
            shortest=1000
            for friend in group:
                distance=math.sqrt((fish.x-friend.x)**2 + (fish.y-friend.y)**2)
                if (distance < shortest and distance != 0):
                    shortest=distance
                    friend_loc[0]=friend.x
                    friend_loc[1]=friend.y
            if(shortest > 3 and shortest!=1000):
                if(fish.x < friend_loc[0]):
                    fish.x+=2
                if(fish.x > friend_loc[0]):
                    fish.x-=2
                if(fish.y < friend_loc[1]):
                    fish.y+=2
                if(fish.y > friend_loc[1]):
                    fish.y-=2
                #print("my color is: {c} and my friend {p} km away".format(p=shortest,c=fish.color))
                    
                    

