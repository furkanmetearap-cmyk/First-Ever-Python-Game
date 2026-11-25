#first ever python game!

import turtle
import random

score = 0
lives = 3

screen = turtle.Screen()
screen.title("hi")
screen.bgcolor("black")
screen.setup(width=600, height=600)

basket = turtle.Turtle()
basket.shape("square")
basket.color("yellow")
basket.shapesize(stretch_wid=1, stretch_len=10)
basket.penup()
basket.goto(0, -250)

def move_left():
    x = basket.xcor() - 40
    if x < -270:
        x = -270
    basket.setx(x)

def move_right():
    screen.update()
    x = basket.xcor() + 40
    if x > 270:
        x = 270
    basket.setx(x)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

drop = turtle.Turtle()
drop.shape("circle")
drop.color("red")
drop.penup()
drop.goto(random.randint(-270, 270), 270)

screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write("Score: 0   Lives: 3", align="center", font=("Poppins", 20, "normal"))

while True:
    screen.update()

    drop.sety(drop.ycor() - 4)

    caught = abs(drop.xcor() - basket.xcor()) < 60 and drop.ycor() < -236

    if caught:
        score += 1
        drop.goto(random.randint(-270, 270), 270)
        pen.clear()
        pen.write("Score: " + str(score) + "   Lives: " + str(lives),
                  align="center", font=("Poppins", 20, "normal"))

    if drop.ycor() < -280:
        lives -= 1
        drop.goto(random.randint(-270, 270), 270)
        pen.clear()
        pen.write("Score: " + str(score) + "   Lives: " + str(lives),
                  align="center", font=("Poppins", 20, "normal"))
    if lives <= 0:
        pen.clear()
        pen.goto(0, 0)
        pen.write("GAME OVER\nScore: " + str(score),
                  align="center", font=("Arial", 40, "bold"))
        screen.update()

screen.mainloop()
