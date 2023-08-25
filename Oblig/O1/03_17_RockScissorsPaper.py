import random 

choice = int(input("Enter choice of weapon: Scissor == 0, Rock == 1, Paper == 2: "))
 
# Generate 
generated = random.randint(0, 2)

if choice == 0 and generated == 0:
    print("The computer is scissor. You are scissor too. it's a draw.")
elif choice == 0 and generated == 1:
    print("The computer is rock. You are scissor. You lost.")
elif choice == 0 and generated == 2:
    print("The computer is paper. You are scissor. You won.")
elif choice == 1 and generated == 0:
    print("The computer is scissor. You are rock. You won.")
elif choice == 1 and generated == 1:
    print("The computer is rock. You are rock too. It is a draw.")
elif choice == 1 and generated == 2:
    print("The computer is paper. You are rock. You lost.")
elif choice == 2 and generated == 0:
    print("The computer is scissor. You are paper. You lost.")
elif choice == 2 and generated == 1:
    print("The computer is rock. You are paper. You won.")
elif choice == 2 and generated == 2:
    print("The computer is paper. You are paper too. It is a draw.")
else:
    print("Not a valid input")