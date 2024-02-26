import math

def jarvis_march(points):
    # find the leftmost point
    #a =  min(points, key = lambda point: point[0])
    rightmost_lowest_point = max(points, key=lambda t: sum(t))    
    #print(a)
    index = points.index(rightmost_lowest_point)
    
    # selection sort
    current = index
    result = []
    result.append(rightmost_lowest_point)
    while (True):
        next = (current + 1) % len(points)
        for p in range(len(points)):
            if p == current:
                continue
            # find the greatest left turn
            # in case of collinearity, consider the farthest point
            d = direction(points[current], points[next], points[p])
            if d < 0: #or (d == 0 and math.dist(points[p], points[current]) > math.dist(points[next], points[current])):
                next = p
        current = next
        if current == index:
            break
        result.append(points[next])

    return result

#def direction(x0, y0, x1, y1, x2, y2):
def direction(a,b,c):
    #return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])



points = [1, 2.4, 2.5, 2, 1.5, 34.5, 5.5, 6, 6, 2.4, 5.5, 9]
coords = [(points[i],points[i+1]) for i in range(0,len(points)-1,2)]
print(jarvis_march(coords))