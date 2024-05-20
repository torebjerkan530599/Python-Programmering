import tkinter as tk

def draw_H(canvas, x, y, size):
    # Draw horizontal line
    canvas.create_line(x - size / 2, y, x + size / 2, y)
    # Draw left vertical line
    canvas.create_line(x - size / 2, y - size / 2, x - size / 2, y + size / 2)
    # Draw right vertical line
    canvas.create_line(x + size / 2, y - size / 2, x + size / 2, y + size / 2)

def draw_H_tree(canvas, x, y, size, depth):
    if depth == 0:
        return
    else:
        draw_H(canvas, x, y, size)
        new_size = size / 2
        new_depth = depth - 1
        draw_H_tree(canvas, x - new_size / 2, y + new_size / 2, new_size, new_depth)  # Upper left H
        draw_H_tree(canvas, x - new_size / 2, y - new_size / 2, new_size, new_depth)  # Lower left H
        draw_H_tree(canvas, x + new_size / 2, y + new_size / 2, new_size, new_depth)  # Upper right H
        draw_H_tree(canvas, x + new_size / 2, y - new_size / 2, new_size, new_depth)  # Lower right H

def main():
    root = tk.Tk()
    root.title("H-tree Fractal")

    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    size = 200
    depth = 3
    draw_H_tree(canvas, 200, 200, size, depth)

    root.mainloop()

if __name__ == "__main__":
    main()
