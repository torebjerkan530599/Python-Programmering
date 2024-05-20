import tkinter as tk

def hilbert_curve(canvas, x, y, size, order, direction):
    if order == 0:
        return
    else:
        # Rotate and draw sub-curve
        if direction == 'U':
            hilbert_curve(canvas, x, y, size, order - 1, 'L')
            draw_line(canvas, x, y, x, y + size)
            hilbert_curve(canvas, x, y + size, size, order - 1, 'U')
            draw_line(canvas, x, y + size, x + size, y + size)
            hilbert_curve(canvas, x + size, y + size, size, order - 1, 'U')
            draw_line(canvas, x + size, y + size, x + size, y)
            hilbert_curve(canvas, x + size, y, size, order - 1, 'R')
        elif direction == 'L':
            hilbert_curve(canvas, x, y, size, order - 1, 'U')
            draw_line(canvas, x, y, x + size, y)
            hilbert_curve(canvas, x + size, y, size, order - 1, 'L')
            draw_line(canvas, x + size, y, x + size, y + size)
            hilbert_curve(canvas, x + size, y + size, size, order - 1, 'L')
            draw_line(canvas, x + size, y + size, x, y + size)
            hilbert_curve(canvas, x, y + size, size, order - 1, 'D')
        elif direction == 'D':
            hilbert_curve(canvas, x, y + size, size, order - 1, 'R')
            draw_line(canvas, x, y + size, x + size, y + size)
            hilbert_curve(canvas, x + size, y + size, size, order - 1, 'D')
            draw_line(canvas, x + size, y + size, x + size, y)
            hilbert_curve(canvas, x + size, y, size, order - 1, 'D')
            draw_line(canvas, x + size, y, x, y)
            hilbert_curve(canvas, x, y, size, order - 1, 'L')
        elif direction == 'R':
            hilbert_curve(canvas, x + size, y, size, order - 1, 'D')
            draw_line(canvas, x + size, y, x + size, y + size)
            hilbert_curve(canvas, x + size, y + size, size, order - 1, 'R')
            draw_line(canvas, x + size, y + size, x, y + size)
            hilbert_curve(canvas, x, y + size, size, order - 1, 'R')
            draw_line(canvas, x, y + size, x, y)
            hilbert_curve(canvas, x, y, size, order - 1, 'U')

def draw_line(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2)

def main():
    root = tk.Tk()
    root.title("Hilbert Curve")

    canvas_width = 600
    canvas_height = 600
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    order = 4  # Change the order of the Hilbert curve here
    size = canvas_width / (2 ** order)
    start_x = (canvas_width - size) / 2
    start_y = (canvas_height - size) / 2
    hilbert_curve(canvas, start_x, start_y, size, order, 'U')

    root.mainloop()

if __name__ == "__main__":
    main()
