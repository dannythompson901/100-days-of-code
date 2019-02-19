def drawsquare(x, size):   #making a function so we can call it with 
    for i in range(4):     #the values we need inside of a for loop
        x.forward(size)    #these options will make A SQUARE (just one square)
        x.left(90)

for i in range(20):   # The range will make the number of squares. 
    tess.left(20)     # this is the angle needed to replicate the pic provided.
    drawsquare(tess, 100) #we are adding the function callback to the for loop so it can call it 20 times. Making 20 squares.
    
def erase_square(x, size):   #making a function so we can call it with 
    tess.color("lightgreen")
    tess.fillcolor('lightgreen') 
    tess.pencolor('lightgreen')
    tess.pensize(4)
    for i in range(4):     #the values we need inside of a for loop
        x.forward(size)    #these options will make A SQUARE (just one square)
        x.left(90)

for i in range(20):   # The range will make the number of squares. 
    tess.left(20)     # this is the angle needed to replicate the pic provided.
    erase_square(tess, 100) #we are adding the function callback to the for loop so it can call it 20 times. Making 20 squares.
    
def drawsquare(x, size):   #making a function so we can call it with 
    tess.fillcolor('blue') 
    tess.pencolor('blue')
    tess.pensize(2)
    for i in range(4):     #the values we need inside of a for loop
        x.forward(size)    #these options will make A SQUARE (just one square)
        x.left(90)

for i in range(20):   # The range will make the number of squares. 
    tess.left(20)     # this is the angle needed to replicate the pic provided.
    drawsquare(tess, 100) #we are adding the function callback to the for loop so it can call it 20 times. Making 20 squares.
