import math
import random 

def which_side(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

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
            if d < 0 or (d == 0 and math.dist(t0, t1) > math.dist(p, t1)):
                t1 = p
        
        t0 = t1    
        if(t1 == H[0]):
            break
        H.append(t1)
        
    return H


#testing:
#points = [1, 2.4, 2.5, 2, 1.5, 34.5, 5.5, 6, 6, 2.4, 5.5, 9]
#coords = [(points[i],points[i+1]) for i in range(0,len(points)-1,2)]
#coords = [(2.13, 5.29),(4.83, 3.9), (9.16, 8.09),(7.08, 5.16), (0.57, 9.92), (1,1)]
#coords = [[1.0, 1.0], [5.0, 2.0], [6.0, 4.0], [5.0, 6.0], [3.0, 6.0], [1.0, 3.0]]
coords = [[5.0, 2.0], [1.0, 1.0], [4.0, 2.0], [6.0, 4.0], [4.0, 3.0] ,[5.0, 6.0], [2.0, 4.0], [3.0, 6.0], [1.0, 3.0]]
convex_hull = getConvexHull(coords)
#convex_hull = getConvexHull(sample)
print(convex_hull)

