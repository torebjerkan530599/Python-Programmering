from tkinter import *


class KochSnowflake:
    def __init__(self):
        window = Tk()
        window.title("Koch Snowflake")

        self.width = 400
        self.height = 400
        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        Label(frame1, text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()
        entry = Entry(frame1, textvariable=self.order,
                      justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display Koch Snowflake",
               command=self.display).pack(side=LEFT)

        window.mainloop()

    def display(self):
        self.canvas.delete("line")
        # Initial points of an equilateral triangle
        p1 = [self.width / 2, 50]
        p2 = [50, self.height - 50]
        p3 = [self.width - 50, self.height - 50]
        self.displayKochSnowflake(int(self.order.get()), p1, p2, p3)

    def displayKochSnowflake(self, order, p1, p2, p3):
        # Koch snowflake is created by repeating the Koch curve on each side of the equilateral triangle
        self.displayKochCurve(order, p1, p2)
        self.displayKochCurve(order, p2, p3)
        self.displayKochCurve(order, p3, p1)

    def displayKochCurve(self, order, p1, p2):
        if order == 0:
            self.drawLine(p1, p2)
        else:
            # Divide the line into three equal segments
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            # Calculate the points for dividing the line
            pA = [p1[0] + dx / 3, p1[1] + dy / 3]
            pC = [p2[0] - dx / 3, p2[1] - dy / 3]
            pB = [(pA[0] + pC[0]) / 2 + (pC[1] - pA[1]) * (3 ** 0.5) / 2,
                  (pA[1] + pC[1]) / 2 + (pA[0] - pC[0]) * (3 ** 0.5) / 2]

            # Recursively draw the Koch curve on each of the segments
            self.displayKochCurve(order - 1, p1, pA)
            self.displayKochCurve(order - 1, pA, pB)
            self.displayKochCurve(order - 1, pB, pC)
            self.displayKochCurve(order - 1, pC, p2)

    def drawLine(self, p1, p2):
        self.canvas.create_line(
            p1[0], p1[1], p2[0], p2[1], tags="line")


KochSnowflake()
