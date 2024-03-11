from tkinter import * # Import tkinter
import math

def direction(a,b,c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

def getConvexHull(S):
    
    rightmost_lowest_point = max(S, key=lambda t: sum(t))    
    H = []
    H.append(rightmost_lowest_point)
    
    t0 = H[0]
    
    while True:
        next_index = (S.index(t0) + 1) % len(S)
        t1 = S[next_index]
    
        for p in S:
            if p == t0:
                continue
            
            d = direction(t0, t1, p)
            if d > 0 or (d == 0 and math.dist(t0, t1) > math.dist(p, t1)):
                t1 = p
        
        t0 = t1    
        if(t1 == H[0]):
            break
        H.append(t1)
        
    return H

def add(event):
    points.append([event.x, event.y])
    repaint()

def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
    repaint()

def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5

def repaint():
    canvas.delete("point")
    if len(points) > 0:
        #
        #
        #
        H = getConvexHull(points) # call GiftWrapping getConvexHull
        print(H)
        #
        #
        canvas.create_polygon(H, fill = "gray", tags = "point")

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags = "point")
    
def displayInstructions():
    instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20, text = instructions[0], justify = CENTER)
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text = instructions[i], justify = RIGHT)
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text = instructions[i + 1], justify = RIGHT)
        

window = Tk() # Create a window
window.title("Convex Hull") # Set title

width = 500
height = 150
radius = 2
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing points
points = []

displayInstructions()

canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)


window.mainloop() # Create an event loop
