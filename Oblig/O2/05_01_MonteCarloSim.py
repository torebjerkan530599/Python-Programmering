import random

numberOfHits = 0

for i in range(0,1000000):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    OP = (x**2)**0.5 + (y**2)**0.5
    #print(OP)
    if(OP <= 1 and OP>=-1):
        numberOfHits += 1

print(numberOfHits)