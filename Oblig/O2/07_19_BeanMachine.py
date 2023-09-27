import random

numballs = int(input("Enter amount of balls: "))
numslots = int(input("Enter amount of slots: "))
path = []
slotnr = 0
ballsInSlot = [0] * numballs

for i in range(numballs):
  for j in range(numslots):
    outcome = random.randint(0, 1)
    if outcome <= 0.5 :
      path.append("L")
    else:
      path.append("R")
      slotnr += 1 # move right

  print(f"Ball {i+1}: {path} , slotnr: {str(slotnr)}")
  ballsInSlot[i] += slotnr  # number of balls in each slot
  slotnr = 0
  path.clear()

end_location = [0] * numslots
for k in range(len(ballsInSlot)):
  end_location[ballsInSlot[k]] += 1

for n in range(numslots):
  print( '|'+(str(n)) , end = '|')
  
print()
for m in reversed(range(1, max(end_location) + 1)):
  print(''.join('|O|' if x >= m else '| |' for x in end_location))
