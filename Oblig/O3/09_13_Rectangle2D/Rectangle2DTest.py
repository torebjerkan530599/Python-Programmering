from Rectangle2D import Rectangle2D

# testene forutsetter at koorinatsystemet er i skjermkoordinater der X øker mot høyre, og Y øker nedover

# # Enter the center x-coordinate of r1: 9
# x1 = float(input("Enter the center x-coordinate of r1:")) 
# # Enter the center y-coordinate of r1: 1.3
# y1 = float(input("Enter the center y-coordinate of r1:"))   
# # Enter the width of r1: 10
# width1 = float(input("Enter the width of r1:"))
# # Enter the height of r1: 35.3 
# height1 = float(input("Enter the height of r1:"))

x1 = 9
y1 = 1.3
width1 = 10
height1 = 35.3 
r1 = Rectangle2D(x1,y1,width1,height1)

print(f'Area for r1 is {r1.getArea()}')
print(f'Perimeter for r1 is {r1.getPerimeter()}')

# testpointX = 5
# testpointY = 4
# print(f'x: {testpointX} and y: {testpointY} is inside r1: {r1.containsPoint(testpointX,testpointY)}')



# # Enter the center x-coordinate of r2: 1.3
# x2 = float(input("Enter the center x-coordinate of r2:")) 
# # Enter the center y-coordinate of r2: 4.3
# y2 = float(input("Enter the center y-coordinate of r2:"))     
# # Enter the width of r2: 4
# width2 = float(input("Enter the width of r2:"))  
# # Enter the height of r2: 5.3
# height2 = float(input("Enter the height of r2:"))

x2 = 1.3
y2 = 4.3
width2 = 4
height2 = 5.3 
r2 = Rectangle2D(x2,y2,width2,height2)

print(f'Area for r2 is {r2.getArea()}')
print(f'Perimeter for r2 is {r2.getPerimeter()}')
print(f'r1 contains the center of r2? {r1.containsPoint(r2.getX(), r2.getY())}')
print(f'r1 contains r2? {r1.contains(r2)}') 
print(f'r2 in r1? {r1.contains(r2)}') #hvilken metode refererer denne til? og hvordan er den forskjellig fra kallet over?
print(f'r1 overlaps r2? {r1.overlaps(r2)}' )

#output
# Area for r1 is 353.0
# Perimeter for r1 is 90.6
# Area for r2 is 21.2
# Perimeter for r2 is 18.6
# r1 contains the center of r2? False
# r1 contains r2? False
# r2 in r1? False
# r1 overlaps r2? False
# r1 < r2? False