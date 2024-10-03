x0 = int(input("Enter the x-coordinate of Point 0:"))
y0 = int(input("Enter the y-coordinate of Point 0:"))
x1 = int(input("Enter the x-coordinate of Point 1:"))
y1 = int(input("Enter the y-coordinate of Point 1:"))
x2 = int(input("Enter the x-coordinate of Point 2:"))
y2 = int(input("Enter the y-coordinate of Point 2:"))


def leftOfTheLine(x0,y0,x1,y1,x2,y2) :
    return ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) ) > 0

def onSameLine(x0,y0,x1,y1,x2,y2) :
    return ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)) == 0
    #slope = (y1 - y0) / (x1 - x0) # p - p1 = k(t - t1)
    #constant =  y1 - slope * x1 # y = ax + c
    #testValue = slope * x2 + constant
    #return testValue == y2

def onLineSegment(x0,y0,x1,y1,x2,y2) : #on the line between (x0,y0) and (x1,y1)
    if(onSameLine(x0,y0,x1,y1,x2,y2)): 
        dotProduct = (x2 - x0) * (x1 - x0) + (y2 - y0)*(y1 - y0)
        if dotProduct < 0:
            return False
        distSq = (x1 - x0)*(x1 - x0) + (y1 - y0)*(y1 - y0)
        if dotProduct > distSq:
            return False
    return True


def rightOfTheLine(x0, y0, x1, y1, x2, y2) :
    return ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) ) < 0

if(onLineSegment(x0,y0,x1,y1,x2,y2)):
    print("{x2},{y2} is on the same segment")
if(onSameLine(x0,y0,x1,y1,x2,y2)) :
    print("{x2},{y2} is on the same line")
if(leftOfTheLine(x0, y0, x1, y1, x2, y2)):
    print("{x2},{y2} is to the left of the line")
if(rightOfTheLine(x0, y0, x1, y1, x2, y2)):
    print("{x2},{y2} is to the right of the line")