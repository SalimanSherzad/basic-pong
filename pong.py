import turtle
import os

window = turtle.Screen()
window.title("Pong 1st project rn")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)



#score
player_1_score = 0
player_2_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2: 0", align= "center", font=("Courier", 24, "normal"))


#player 1 
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("white")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

#player_2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("white")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)


#ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 
ball.dy = 2
#my functions 

def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)
def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)


def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)
def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)


window.listen()
window.onkeypress(player_1_up, "w")
window.onkeypress(player_1_down, "s")
window.onkeypress(player_2_up, "Up")
window.onkeypress(player_2_down, "Down")


while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_1_score += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(player_1_score, player_2_score), align= "center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_2_score += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(player_1_score, player_2_score), align= "center", font=("Courier", 24, "normal"))
    
    if ball.xcor() > 340 and (ball.xcor() < 350 ) and (ball.ycor() < player_2.ycor() + 40 and ball.ycor() > player_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if ball.xcor() < -340 and (ball.xcor() > -350 ) and (ball.ycor() < player_1.ycor() + 40 and ball.ycor() > player_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1