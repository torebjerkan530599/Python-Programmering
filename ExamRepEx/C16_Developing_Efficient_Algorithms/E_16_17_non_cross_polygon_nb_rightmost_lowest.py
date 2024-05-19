'''
To solve the problem of constructing a noncrossing polygon using Turtle graphics in Python, we'll follow these steps:

* Read Points from the User: We'll prompt the user to input a series of points.
* Select the Rightmost Lowest Point: This point will be used as the reference point (p0).
* Sort the Points Angularly: We'll sort the points around p0 based on their angles with respect to the x-axis. 
    If two points have the same angle, the closer one to p0 will be considered greater.
* Draw the Polygon: Use Turtle graphics to draw the noncrossing polygon by connecting the points in the sorted order.
'''

import turtle
import math

def get_rightmost_lowest_point(points):
    rightmost_lowest = points[0]
    for point in points[1:]:
        if (point[1] < rightmost_lowest[1]) or (point[1] == rightmost_lowest[1] and point[0] > rightmost_lowest[0]):
            rightmost_lowest = point
    return rightmost_lowest

def angle_with_p0(p0, p):
    return math.atan2(p[1] - p0[1], p[0] - p0[0])

def distance(p0, p):
    return math.sqrt((p[0] - p0[0])**2 + (p[1] - p0[1])**2)

def sort_points(points, p0):
    return sorted(points, key=lambda p: (angle_with_p0(p0, p), distance(p0, p)))

def draw_polygon(points):
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    for point in points:
        turtle.goto(point)
    turtle.goto(points[0])  # Close the polygon
    turtle.done()

def main():
    # Step 1: Get points from the user
    points = []
    print("Enter points in the format 'x y' (without quotes), one per line. Enter 'done' when finished:")
    '''
    for convenience and testing, copy paste this:
    100 100
    200 100
    200 200
    100 200
    150 150
    done
    '''
    while True:
        input_str = input()
        if input_str.lower() == 'done':
            break
        try:
            x, y = map(float, input_str.split())
            points.append((x, y))
        except ValueError:
            print("Invalid input. Please enter coordinates in 'x y' format or 'done' to finish.")

    if len(points) < 3:
        print("A polygon requires at least 3 points.")
        return

    # Step 2: Select the rightmost lowest point
    p0 = get_rightmost_lowest_point(points)
    points.remove(p0)

    # Step 3: Sort the points angularly around p0
    sorted_points = sort_points(points, p0)

    # Insert p0 at the beginning of the sorted points list
    sorted_points.insert(0, p0)

    # Step 4: Draw the polygon using Turtle graphics
    draw_polygon(sorted_points)

if __name__ == "__main__":
    main()
