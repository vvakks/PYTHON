import random

while True:
    try:
        levellist=[]
        level= int(input("Enter level"))
        for levelnums in range(level):
            levellist.append(levelnums)
        randomnum=random.choice(levellist)
        while True:
            guess= int(input("Enter guess"))
            if(guess==randomnum):
                print("Just right")
                break
            elif(guess<randomnum):
                print("too small")
            elif(guess>randomnum):
                print("too big")
        break
    except ValueError:
        continue