
class ConvexHullGrahamScan():
    
    def __init__(self,points):
        self.points = points
        
    def whichSide(self,x0, y0, x1, y1, x2, y2):
        return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    
    def scan(self):
        stack = list()
		
		# bottom most, left most point is guaranteed to be on the hull
  
        minYPoint = min(self.points, key= lambda point: point[1])[1]# point with lowest y value
		sortByAngle(points, minYPoint) # sort by angle with respect to minYPoint
		
		stack.push(self.points.get(0)) # 1st point is guaranteed to be on the hull
		stack.push(self.points.get(1)) # don't know about this one yet
		
		for i in range(i+2, len(self.points)):#int i = 2, size = points.size(); i < size; i++:
			next = points.get(i)
			p = stack.pop()		
			
			while stack.peek() != null and GraphUtils.ccw(stack.peek(), p, next) <= 0:
				p = stack.pop(); # delete points that create clockwise turn
			
						
			stack.push(p)
			stack.push(points.get(i))
		# the very last point pushed in could have been collinear, so we check for that

		p = stack.pop()
		if GraphUtils.ccw(stack.peek(), p, minYPoint) > 0:
			stack.push(p) #put it back, everything is fine
		
		
		return stack
	

if __name__ == "__main__":
    points = {(2, 2), (-2, 3), (1, 1)}
    print(type(points))
    hull = ConvexHullGrahamScan()
    print(f'Graham Scan: {hull.scan(points)}')