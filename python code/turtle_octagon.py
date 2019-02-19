import turtle

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    
    tess = turtle.Turtle()
    tess.color("hotpink")
    tess.speed(10)
    tess.pensize(2)
    draw_poly(tess, 8, 50)
    
def draw_poly(t, sides, side_length):
    angle = 360/sides
    for i in range(sides):
        t.forward(side_length)
        t.left(angle)
    
    
if __name__ == "__main__":
    main()
