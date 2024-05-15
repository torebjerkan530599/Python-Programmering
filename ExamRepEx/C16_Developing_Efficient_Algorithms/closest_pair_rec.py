import math

def dist(p1, p2):
    return math.sqrt(((p2[1]-p1[1])**2)+((p2[0]-p1[0])**2))
    '''
    other ways of calculating:
    formula_1 = ((x2 - x1) **2 + (y2 - y1) ** 2)**0.5
    formula_2 = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
    '''

def closest_brute_force(points): # 9
    min_dist = float("inf")
    p1 = None
    p2 = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = dist(points[i], points[j])
            
            if d < min_dist:
                min_dist = d
                p1  = points[i]
                p2 = points[j]
    return p1, p2, min_dist


# den rekursive metoden fra undervisningen
def rec(xsorted, ysorted): #2: rekursiv funksjon, deler opp problemet
    n = len(xsorted)
    if n <= 3:
        return closest_brute_force(xsorted) # 3, base case
    else:
        midpoint = xsorted[n//2]
        xsorted_left = xsorted[:n//2]
        xsorted_right = xsorted[n//2:]
        ysorted_left = []
        ysorted_right = []
    
    #10: finn ut hvilke punkter, sortert etter Y som tilhører hver halvdel
    for point in ysorted: 
        if point[0] <= midpoint[0]:
            ysorted_left.append(point)  
        else:
            ysorted_right.append(point)
        
    (p1_left, p2_left, delta_left) = rec(xsorted_left, ysorted_left) # 4:rekursive kall, vil til slutt fanges opp av base case
    (p1_right, p2_right, delta_right) = rec(xsorted_right, ysorted_right)#5:rekursive kall, vil til slutt fanges opp av base case
    
    #11: minste avstand mellom de to halvdelene velges 
    if delta_left <delta_right:
        (p1, p2, delta) = (p1_left, p2_left, delta_left)  
    else: 
        (p1, p2, delta) = (p1_right, p2_right, delta_right) 
    
    #6: velg ut hvilke koordinater som ligger i «the strip»
    in_band = [point for point in ysorted if midpoint[0]-delta < point[0] < midpoint[0]+delta] 

    #7: sjekk om det finnes punkter i «the strip» som danner en ny minste d
    for i in range(len(in_band)): 
        for j in range(i+1, min(i+7, len(in_band))):
            d = dist(in_band[i], in_band[j])
            if d < delta:
                #print(in_band[i], in_band[j])
                (p1, p2, delta) = (in_band[i], in_band[j], d)
    return p1, p2, delta #8: returner resultat

def closest(points): #1: Sortering på X og Y koordinat, kall til rekursiv hjelperutine
    xsorted = sorted(points, key=lambda point: point[0])
    ysorted = sorted(points, key=lambda point: point[1])
    return rec(xsorted, ysorted)

def main():
    points = [[5.2,2.4],[1.7,1.2],[4.1,2.6],
              [6.5,4.9],[4.3,3.5],[5.4,6.7],
              [2.6,4.1],[3.0,6.3],[1.7,3.2]]
    
    p1, p2, dist = closest(points)
    
    print(f"The nearest points are \
    {p1} and {p2}, with distance {dist:0.3f}")

if __name__ == "__main__":
    main()

# alternative approach, printing distance and points

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    n = len(points)
    if n <= 3:
        min_distance = float('inf')
        closest_points = ()
        for i in range(n):
            for j in range(i+1, n):
                dist = euclidean_distance(points[i], points[j])
                if dist < min_distance:
                    min_distance = dist
                    closest_points = (points[i], points[j])
        return min_distance, closest_points
    
    points.sort(key=lambda x: x[0])
    mid = n // 2
    left_half = points[:mid]
    right_half = points[mid:]
    
    min_dist_left, closest_left = closest_pair(left_half)
    min_dist_right, closest_right = closest_pair(right_half)
    
    if min_dist_left < min_dist_right:
        min_dist = min_dist_left
        closest_result = closest_left
    else:
        min_dist = min_dist_right
        closest_result = closest_right
    
    strip = [point for point in points if abs(point[0] - points[mid][0]) < min_dist]
    strip.sort(key=lambda x: x[1])
    
    min_strip = float('inf')
    closest_strip = ()
    for i in range(len(strip)):
        for j in range(i+1, min(i+8, len(strip))):
            dist = euclidean_distance(strip[i], strip[j])
            if dist < min_strip:
                min_strip = dist
                closest_strip = (strip[i], strip[j])
    
    if min_strip < min_dist:
        return min_strip, closest_strip
    else:
        return min_dist, closest_result

# Example usage:
points = [(5.2, 2.4), (1.7, 1.2), (4.1, 2.6), (6.5, 4.9), (4.3, 3.5), (5.4, 6.7), (2.6, 4.1), (3.0, 6.3), (1.7, 3.2)]
closest_distance, closest_points = closest_pair(points)
print("Closest distance:", closest_distance)
print("Closest points:", closest_points)
