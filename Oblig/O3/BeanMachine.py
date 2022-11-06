import random
def main():
  path = []
  balls = int(input("Enter amount of balls: "))
  slots = int(input("Enter amount of slots: "))
  
  for i in range(balls):
    for j in range(slots-2):
      row = 1
      for k in range(row):
        outcome = random.randint(0,1)
        if(outcome <= 0.5):
          path.append("L")
        else:
          path.append("R")
        row +=1
    print("Ball "+str(i+1) + ": "+ str(path)) 
    path.clear()
      
  
main()