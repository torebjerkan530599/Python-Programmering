import random

numballs = int(input("Enter amount of balls: "))
numslots = int(input("Enter amount of slots: "))
path = []
slotnr = 0
slots_list = [0] * numballs
test_list = [0] * (numslots + 1)

for i in range(numballs):
  for j in range(numslots):
    outcome = random.randint(0, 1)
    if outcome <= 0.5 :
      path.append("L")
    else:
      path.append("R")
      slotnr += 1 # move right

  print(f"Ball {i+1}: {path} , slotnr: {str(slotnr)}")
  slots_list[i] += slotnr  # number of balls in each slot
  test_list[slotnr] += 1
  slotnr = 0
  path.clear()

# end_location = [0] * (numslots + 1)
# for k in range(len(slots_list)):
#   end_location[slots_list[k]] += 1

# print(end_location)
#print(test_list)
#print(max(end_location))

# for n in range(numslots+1):
#   print( '|'+(str(n)) , end = '|')
  
# print()
# for m in reversed(range(1, max(end_location) + 1)):
#   print(''.join('|O|' if x >= m else '| |' for x in end_location))
  
  
#my own pedigree...

print("Own version")

for n in range(numslots+1):
  print( '|'+(str(n)) , end = '|')
  
print()
for m in reversed(range(1, max(test_list) + 1)):
  print(''.join('|O|' if x >= m else '| |' for x in test_list))
