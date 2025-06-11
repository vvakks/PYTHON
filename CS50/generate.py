import random 
import sys
import statistics
coin = random.choice(["heads","tails"])
ligma=[ 1,2,3,4,5,6,7]
random.shuffle(ligma)
print(ligma)
print(statistics.mean(ligma))
print("hello my name is ", sys.argv[1])
