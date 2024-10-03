import random

numballs = int(input("Enter amount of balls: "))
numslots = int(input("Enter amount of slots: "))
path = []
slotnr = 0
slots_list = [0] * (numslots)

for i in range(numballs): # queue of balls
  for j in range(numslots-1): # drop one ball
    outcome = random.randint(0, 1)
    if outcome <= 0.5 :
      path.append("L")
    else:
      path.append("R")
      slotnr += 1 # move one slot to the right

  print(f"Ball {i+1}: {path} , slotnr: {str(slotnr)}") # result of one ball-drop
  slots_list[slotnr] += 1 # increase balls in where the ball settles
  slotnr = 0
  path.clear()

# print("reversed: ")
#reverse = slots_list[1:max(slots_list) + 1:-1]
#print(reverse)

for n in range(numslots):
  print( '|'+(str(n)) , end = '|')
  
print()
result = ''
for p in reversed(range(1, max(slots_list) + 1)):
  # print(''.join('|O|' if q >= p else '| |' for q in slots_list)) # hard to read
  for x in slots_list:
    if x >= p:
      result += '|O|'
    else:
      result += '| |'
  print(result)
  result = ''