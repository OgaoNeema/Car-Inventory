import tkinter as tk
import turtle
import random

def random_color():
    #Generates a random hex color.
    return "#" + ''.join(random.choices('0123456789ABCDEF', k=6))

class Roses:
    def __init__(self, root):
        self.root = root
        
        self.canvas = tk.Canvas(root, width=700, height=200, bd=0) 
        self.canvas.pack()

        self.screen = turtle.TurtleScreen(self.canvas) #Converts the Canvas into a Turtle drawing area
        self.screen.bgcolor("white")
        self.screen.tracer(False)  # Disables real-time drawing for faster rendering

        self.rose_turtle = turtle.RawTurtle(self.screen)
        self.rose_turtle.hideturtle() #Hides cursor
        self.rose_turtle.speed(0) #Fastest speed

        self.draw_roses()
        self.screen.update()  # Function below that refreshes the screen after drawing all roses

    def draw_roses(self): #7 roses
        positions = [(-300, -30), (-200, -30), (-100, -30), (0, -30), (100, -30), (200, -30), (300, -30)] #Rose positions
        for pos in positions:
            petal_color = random_color()  # Generate a unique random color for each
            self.rose_turtle.penup()
            self.rose_turtle.goto(pos)
            self.rose_turtle.pendown()
            self.draw_single_rose(scale=0.2, petal_color=petal_color)  # Apply dynamic color

    def draw_single_rose(self, scale=0.3, petal_color=random_color()):
        t = self.rose_turtle
        t.penup()
        t.left(90)
        t.fd(50 * scale) 
        t.pendown()
        t.right(90)

        t.fillcolor(petal_color)
        t.begin_fill()
        t.circle(5 * scale, 180)
        t.circle(12 * scale, 110)
        t.left(50)
        t.circle(30 * scale, 45)
        t.circle(10 * scale, 170)
        t.right(24)
        t.fd(15 * scale)
        t.left(10)
        t.circle(15 * scale, 110)
        t.fd(10 * scale)
        t.left(40)
        t.circle(45 * scale, 70)
        t.circle(15 * scale, 150)
        t.right(30)
        t.fd(25 * scale)
        t.circle(40 * scale, 90)
        t.left(15)
        t.fd(22 * scale)
        t.right(165)
        t.fd(10 * scale)
        t.left(155)
        t.circle(75 * scale, 80)
        t.left(50)
        t.circle(75 * scale, 90)
        t.end_fill()

        # Leaves remain green
        t.left(150)
        t.circle(-45 * scale, 70)
        t.left(20)
        t.circle(37 * scale, 105)
        t.setheading(60)
        t.circle(40 * scale, 98)
        t.circle(-45 * scale, 40)

        t.left(180)
        t.circle(45 * scale, 40)
        t.circle(-40 * scale, 98)
        t.setheading(-83)

        t.fd(15 * scale)
        t.left(90)
        t.fd(12 * scale)
        t.left(45)
        t.fillcolor('darkgreen') 
        t.begin_fill()
        t.circle(-40 * scale, 90)
        t.right(90)
        t.circle(-40 * scale, 90)
        t.end_fill()
        t.right(135)
        t.fd(30 * scale)
        t.left(180)
        t.fd(42 * scale)
        t.left(90)
        t.fd(40 * scale)

        t.right(90)
        t.right(45)
        t.fillcolor('darkgreen')
        t.begin_fill()
        t.circle(40 * scale, 90)
        t.left(90)
        t.circle(40 * scale, 90)
        t.end_fill()
        t.left(135)
        t.fd(30 * scale)
        t.left(180)
        t.fd(30 * scale)
        t.right(90)
        t.circle(100 * scale, 60)

    def update_roses(self):
        #Clears and redraws roses with new random colors.
        self.rose_turtle.clear()
        self.draw_roses()
        self.screen.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = Roses(root)
    root.mainloop()
