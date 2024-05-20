import turtle

def draw_H(x, y, size):
    turtle.penup()
    turtle.goto(x - size / 2, y)
    turtle.pendown()
    turtle.forward(size)
    turtle.penup()
    turtle.goto(x - size / 2, y - size / 2)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.backward(size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.backward(size)
    turtle.penup()

def draw_H_tree(x, y, size, depth):
    if depth == 0:
        return
    else:
        draw_H(x, y, size)
        new_size = size / 2
        new_depth = depth - 1
        draw_H_tree(x - new_size / 2, y + new_size / 2, new_size, new_depth)  # Upper left H
        draw_H_tree(x - new_size / 2, y - new_size / 2, new_size, new_depth)  # Lower left H
        draw_H_tree(x + new_size / 2, y + new_size / 2, new_size, new_depth)  # Upper right H
        draw_H_tree(x + new_size / 2, y - new_size / 2, new_size, new_depth)  # Lower right H

def main():
    screen = turtle.Screen()
    turtle.speed(0)  # Set the turtle's speed to the fastest
    size = 200
    depth = 3
    draw_H_tree(0, 0, size, depth)
    screen.mainloop()

if __name__ == "__main__":
    main()
