from Ex_15_CircleWithCustomException import Circle
from Ex_14_InvalidRadiusException import InvalidRadiusException 

try:
    c1 = Circle(5)
    print("c1's area is", c1.getArea())
    c2 = Circle(-5)
    print("c2's area is", c2.getArea())
    c3 = Circle(0)
    print("c3's area is", c3.getArea())
except InvalidRadiusException as ex: # Catch invalid radius
    print("The radius", ex.getRadius(), "is invalid")
except Exception:
    print("Something is wrong")
