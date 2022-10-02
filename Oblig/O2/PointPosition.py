# x0 = float(input("Enter the x-coordinate of Point 0:")) # sample values 123.1 
# y0 = float(input("Enter the y-coordinate of Point 0:")) # sample values 9.82 
# x1 = float(input("Enter the x-coordinate of Point 1:")) # sample values 9.3
# y1 = float(input("Enter the y-coordinate of Point 1:")) # sample values -29.3
# x2 = float(input("Enter the x-coordinate of Point 2:")) # sample values 2.5
# y2 = float(input("Enter the y-coordinate of Point 2:")) # sample values 6.9

#x0 = 123.1
#y0 = 9.82 
#x1 = 9.3
#y1 = -29.3
#x2 = 2.5
#y2 = 6.9

#x0 = -4
#y0 = -6
#x1 = 4
#y1 = 2
#x2 = -1
#y2 = -3


#x0=1, 
#y0=1, 
#x1 = 4, 
#y1 = 1, 
#x2 = 3, 
#y2 = 1 #er på samme linjesegment

x0=1, 
y0=1, 
x1 = 3, 
y1 = 1, 
x2 = 4, 
y2 = 1 #er på samme linje


def leftOfTheLine(x0,y0,x1,y1,x2,y2) :
    return ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) ) > 0

def onSameLine(x0,y0,x1,y1,x2,y2) :
#    return ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) ) == 0
#    x0 = round(x0, 1) #var ikke oppgitt antall desimaler, bare eksempel med 1.
#    y0 = round(y0, 1)
#    x1 = round(x1, 1)
#    y1 = round(y1, 1)
#    x2 = round(x2, 1)
#    y2 = round(y2, 1)
#
    slope = (y1 - y0) / (x1 - x0) # p - p1 = k(t - t1)
    constant =  y1 - slope * x1 # y = ax + c

    testValue = slope * x2 + constant

    return testValue == y2

    

def onLineSegment(x0,y0,x1,y1,x2,y2) : #on the line between (x0,y0) and (x1,y1)
    return ((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)) == 0
    #distAB = ((x0 - x1)**2 + (y0 - y1)**2)**(1/2)
    #distAB = round(distAB)

    #distBC = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    #distBC = round(distBC)
    
    #distAC = ((x0 - x2)**2 + (x0 - y2)**2)**(1/2)
    #distAC = round(distAC)

    #return distAC + distBC == distAB
    
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