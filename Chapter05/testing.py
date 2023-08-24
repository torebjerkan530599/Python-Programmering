x = float(input("Enter the x-coordinate of a rectangle: "))
y = float(input("Enter the y-coordinate of a rectangle: "))

if (x <= width/2.0) and (y <= height/2.0) :
    print(f"Point ({x}, {y}) is in the rectangle")
else:
    print(f"Point ({x}, {y}) is not in the rectangle")