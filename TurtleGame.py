import turtle
turtle.title("Flowers") ## title of turtle
turtle.Screen().bgcolor("red") ##bg color
def square(x,y,length): ##makes squares
    turtle.pu()
    turtle.goto (x,y)
    turtle.pd()
    turtle.speed(0)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
def flower(x, y): ##rotates and turns into flowers
    turn = 20
    for scube in range(18):
        square(x,y,50)
        turtle.left(turn)


flower(-300,200)##positions for flowers to be drawn 
flower(-200,200)
flower(-100,200)
flower(0,200)
flower(100,200)
flower(200,200)
flower(300,200)


flower(-300,100)
flower(-200,100)
flower(-100,100)
flower(0,100)
flower(100,100)
flower(200,100)
flower(300,100)

flower(-300,0)
flower(-200,0)
flower(-100,0)
flower(0,0)
flower(100,0)
flower(200,0)
flower(300,0)

flower(-300,-100)
flower(-200,-100)
flower(-100,-100)
flower(0,-100)
flower(100,-100)
flower(200,-100)
flower(300,-100)

flower(-300,-200)
flower(-200,-200)
flower(-100,-200)
flower(0,-200)
flower(100,-200)
flower(200,-200)
flower(300,-200)





