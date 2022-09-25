# x0 = float(input("Enter the x-coordinate of Point 0:")) # sample values 123.1 
# y0 = float(input("Enter the y-coordinate of Point 0:")) # sample values 9.82 
# x1 = float(input("Enter the x-coordinate of Point 1:")) # sample values 9.3
# y1 = float(input("Enter the y-coordinate of Point 1:")) # sample values -29.3
# x2 = float(input("Enter the x-coordinate of Point 2:")) # sample values 2.5
# y2 = float(input("Enter the y-coordinate of Point 2:")) # sample values 6.9

x0 = 123.1
y0 = 9.82 
x1 = 9.3
y1 = -29.3
x2 = 2.5
y2 = 6.9

x0 = 1
y0 = 1
x1 = 3
y1 = 1
x2 = 4
y2 = 1


def leftOfTheLine(x0,y0,x1,y1,x2,y2) :
    return ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) ) > 0

def onSameLine(x0,y0,x1,y1,x2,y2) :
    return ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) ) == 0

def onLineSegment(x0,y0,x1,y1,x2,y2) : #on the extension of the vector
    return
    
def rightOfTheLine(x0, y0, x1, y1, x2, y2) :
    return ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) ) < 0


if(leftOfTheLine(x0,y0,x1,y1,x2,y2)) :
    print((x2,y2),"is on the left side of the line from",(x0,y0),"to",(x1,y1))

if(onSameLine(x0,y0,x1,y1,x2,y2)) :
    print((x2,y2),"is on same line from",(x0,y0),"to",(x1,y1))

if(rightOfTheLine(x0,y0,x1,y1,x2,y2)) :
    print((x2,y2),"is on the right side of the line from",(x0,y0),"to",(x1,y1))