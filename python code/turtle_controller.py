import tkinter as tk
import turtle

def goUp():
    tess.sety(tess.ycor() + 5)

def goDown():
    tess.sety(tess.ycor() - 5)

def goRight():
    tess.setx(tess.xcor() + 5)

def goLeft():
    tess.setx(tess.xcor() - 5)

def penUp():
    tess.penup()

def penDown():
    tess.pendown()
root = tk.Tk()
#LAUNCHCODE 101 INSPIRED WORK
#LAUNCHCODE 101 INSPIRED WORK
#LAUNCHCODE 101 INSPIRED WORK
#LAUNCHCODE 101 INSPIRED WORK
#DANNY THOMPSON
#DANNY THOMPSON!
canvas = tk.Canvas(root, width=150, height=100)
canvas.pack()

wn = turtle.Screen()
wn.bgcolor("yellow")
tess = turtle.Turtle()
tess.color("green")

topFrame = tk.Frame(root)
topFrame.pack()
middleFrame = tk.Frame(root)
middleFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack()

tk.Button(topFrame, text="Up", fg="red", command=goUp).pack()
tk.Button(middleFrame, text="Left", fg="red", command=goLeft).pack(side=tk.LEFT)
tk.Button(middleFrame, text="Right", fg="red", command=goRight).pack(side=tk.RIGHT)
tk.Button(middleFrame, text="Down", fg="red", command=goDown).pack()
tk.Button(bottomFrame, text="Pen Up", fg="red", command=penUp).pack()
tk.Button(bottomFrame, text="Pen Down", fg="red", command=penDown).pack()
wn.mainloop()
