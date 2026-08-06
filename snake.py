import turtle

screen = turtle.Screen()
screen.title("Mini Snake Game")
screen.bgcolor("black")
screen.setup(600, 600)

snake = turtle.Turtle()
snake.shape("square")
snake.color("lime")
snake.penup()
snake.speed(0)

def up():
    snake.setheading(90)

def down():
    snake.setheading(270)

def left():
    snake.setheading(180)

def right():
    snake.setheading(0)

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

try:
    while True:
        screen.update()
        snake.forward(20)
except turtle.Terminator:
    print("Game closed.")
