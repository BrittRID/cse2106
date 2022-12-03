import turtle as t
# Score
player_a_score = 0
player_b_score = 0

# Window
window = t.Screen()
window.title("Ping Pong")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Left Paddle
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right Paddle
right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("blue")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5, 5)
ball_x_direction = 1.8
ball_y_direction = 1.8

# Pen for score
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0      Player B: 0", align="center", font=("Arial", 24, "normal"))

# Left Paddle Movements
def left_paddle_up():
    y = left_paddle.ycor()
    y = y + 15
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y = y - 15
    left_paddle.sety(y)

# Right Paddle Movements
def right_paddle_up():
    y = right_paddle.ycor()
    y = y + 15
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y = y - 15
    right_paddle.sety(y)

# Assigning Keyboard Keys
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "i")
window.onkeypress(right_paddle_down, "k")

while True:
    window.update()

    # Ball Movements
    ball.setx(ball.xcor() + ball_x_direction)
    ball.sety(ball.ycor() + ball_y_direction)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y_direction = ball_y_direction * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_y_direction = ball_y_direction * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_x_direction = ball_x_direction * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(player_a_score, player_b_score), align="center", font=("Arial", 24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_x_direction = ball_x_direction * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(player_a_score, player_b_score), align="center", font=("Arial", 24,"normal"))

    # Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40:
        ball.setx(340)
        ball_x_direction = ball_x_direction * -1

    if ball.xcor() < -340 and ball.xcor() < -350 and ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40:
        ball.setx(-340)
        ball_x_direction = ball_x_direction * -1
