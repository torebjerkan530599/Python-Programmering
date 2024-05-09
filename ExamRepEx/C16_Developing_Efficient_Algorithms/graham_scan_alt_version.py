class ConvexHullGrahamScan:
    
    def __init__(self, points):
        self.points = points
        
    def whichSide(self, x0, y0, x1, y1, x2, y2):
        return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    
    def scan(self):
        stack = []
        
        # bottom most, left most point is guaranteed to be on the hull
        minYPoint = min(self.points, key=lambda point: point[1])[1]  # point with lowest y value
        sorted_points = sorted(self.points, key=lambda point: self.whichSide(minYPoint, minYPoint, point[0], point[1], 0, 0))  # sort by angle with respect to minYPoint
        
        stack.append(sorted_points[0])  # 1st point is guaranteed to be on the hull
        stack.append(sorted_points[1])  # don't know about this one yet
        
        for i in range(2, len(sorted_points)):  # start from the third point
            next_point = sorted_points[i]
            p = stack.pop()
            
            while stack and self.whichSide(stack[-1][0], stack[-1][1], p[0], p[1], next_point[0], next_point[1]) <= 0:
                p = stack.pop()  # delete points that create clockwise turn
            stack.append(p)
            stack.append(next_point)
        
        p = stack.pop()
        if stack and self.whichSide(stack[-1][0], stack[-1][1], p[0], p[1], minYPoint, minYPoint) > 0:
            stack.append(p)  # put it back, everything is fine
        
        return stack
	

if __name__ == "__main__":
    points = [(2, 2), (-2, 3), (1, 1)]
    hull = ConvexHullGrahamScan(points)
    print(f'Graham Scan: {hull.scan()}')
