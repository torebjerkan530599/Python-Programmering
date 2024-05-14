import random

balls = int(input("Enter the number of balls to drop: "))  
slots = int(input("Enter the number of slots: "))
path = []
right = 0
lst_slots = [0] * balls

for i in range(1, balls + 1):
    for j in range(1, slots + 1):
        outcome = random.randint(1, j * 2)
        if 1 <= outcome <= j:
            path.append("L")
        else:
            path.append("R")
            right += 1
    print(f"Ball {i}: {path} , slotnr: {str(right)}")
    lst_slots[i - 1] = right
    right = 0
    path.clear()

end_location = [0] * slots
for k in range(len(lst_slots)):
    end_location[lst_slots[k] - 1] += 1

for m in reversed(range(1, max(end_location) + 1)):
    print(''.join('O' if x >= m else ' ' for x in end_location))