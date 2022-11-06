def distance(x1,y1,x2,y2):
  return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
  
def findCapitol(points):
  scores = []
  p1,p2 = 0,1
  
  for i in range(len(points)):
    totalDist = 0 #reset
    for j in range(len(points)):
      d = distance(points[i][0],points[i][1],points[j][0],points[j][1])
      totalDist += d
      
    if(len(scores) == 0 or totalDist < min(scores)):
      p1,p2 = points[i][0], points[i][1]
    scores.append(totalDist)
        
  return p1,p2
def main():
  cities = []
  numCities =  int(input("Enter the number of cities you wish to compare: "))
  for i in range(numCities):
    s = input("Enter x- and y-coordinates of city " + str(i) + ": ")
    point = [float(x) for x in s.split()]
    cities.append(point)
  p1, p2 = findCapitol(cities)
  print("The coordinates of the capitol: "+ str(p1) +" "+ str(p2))
main()
#Testing purposes
#p1, p2 = findCapitol([[5.1,3],[1,9],[2.5,5],[5.4,54],[5.5,2.2]])
#p1, p2 = findCapitol([[-1,-1],[2,-1],[2,0.5],]) #,[3,3],[4,2],[-1,3]])