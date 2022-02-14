import turtle
import time
import random
from random import randint
from pygame import mixer

mixer.init()
sound1 = "sounds/impact_snowball_hit_wall.mp3"
sound2 = "sounds/zapsplat_sport_squash_ball" \
    "_catch_in_hand_001_17896.mp3"
impact = mixer.Sound(sound1)
impact_2 = mixer.Sound(sound2)
mixer.music.load("ost/Epic battle between 2 paddles.ogg")
mixer.music.play(-1, 0.0, 0)
mixer.music.pause()

screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.tracer(0)

placar = turtle.Turtle()
placar.hideturtle()
placar.penup()
placar.goto(249, 259)
placar.pendown()
placar.pensize(3)
placar.color("white")
placar.right(180)
placar.forward(500)
placar.right(90)
placar.forward(38)
placar.right(90)
placar.forward(500)
placar.right(90)
placar.forward(38)

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("cyan")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

paddle_2 = turtle.Turtle()
paddle_2.speed(5)
paddle_2.shape("square")
paddle_2.color("cyan")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)
bot = False  # variable that defines if bot is active or not
distance = 0  # variable that defines the margin of error of the bot
adapt = False

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue violet")
ball.hideturtle()
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = random.choice([1, 2, 3, 4])
Right = True  # variable that defines whether the ball is going to the right
hspeed = 0  # sets the speed increase of the ball

hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Bodoni MT Black", 24, "normal"))

# Writing "Player 1" on the screen
player1 = turtle.Turtle()
player1.hideturtle()
player1.goto(-240, 260)
player1.pencolor("white")
player1.write("Player 1", align="left", font=("Bodoni MT Black", 24, "normal"))

# Writing "Player 2" on the screen
player2 = turtle.Turtle()
player2.hideturtle()
player2.goto(240, 260)
player2.pencolor("white")
player2.write(" Player 2", align="right", font=(
    "Bodoni MT Black", 24, "normal"))

start_screen = turtle.Turtle()
start_screen.speed(0)
start_screen.color("white")
start_screen.penup()
start_screen.hideturtle()
start_screen.goto(5, -65)

start_rec = turtle.Turtle()
start_rec.speed(100)
start_rec.goto(-230, -130)
start_rec.color("white")

start_rec.forward(460)
start_rec.left(90)
start_rec.forward(300)
start_rec.left(90)
start_rec.forward(460)
start_rec.left(90)
start_rec.forward(300)
start_rec.left(90)
start_rec.hideturtle()

start_p = False


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if not (bot):
        if y < 250:
            y += 30
        else:
            y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    global bot
    if not (bot):
        if y > -250:
            y += -30
        else:
            y = -250
    paddle_2.sety(y)


def start_game():
    global start_p
    if not (start_p):
        print("2 Players")
        mixer.music.rewind()
        mixer.music.unpause()
    start_p = True


def IA_difficulty_easy():
    global start_p, distance, bot
    if not (start_p):
        distance = 75
        bot = True
        print("Easy")
        mixer.music.rewind()
        mixer.music.unpause()
    start_p = True


def IA_difficulty_medium():
    global start_p, distance, bot
    if not (start_p):
        distance = 70
        bot = True
        print("Medium")
        mixer.music.rewind()
        mixer.music.unpause()
    start_p = True


def IA_difficulty_hard():
    global start_p, distance, bot
    if not (start_p):
        distance = 65
        bot = True
        print("Hard")
        mixer.music.rewind()
        mixer.music.unpause()
    start_p = True


def IA_difficulty_insane():
    global start_p, distance, bot
    if not (start_p):
        # the smallest possible margin of error,
        # below that, AI becomes impossible
        distance = 59
        bot = True
        print("insane")
        mixer.music.rewind()
        mixer.music.unpause()
    start_p = True


def IA_difficulty_adaptive():
    global start_p, distance, bot, adapt
    if not (start_p):
        distance = random.choice([60, 65, 70, 75, 80])
        adapt = True
        bot = True
        print("adaptive")
        mixer.music.rewind()
        mixer.music.unpause()
    start_p = True


screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")
screen.onkeypress(start_game, "space")
screen.onkeypress(IA_difficulty_easy, "1")
screen.onkeypress(IA_difficulty_medium, "2")
screen.onkeypress(IA_difficulty_hard, "3")
screen.onkeypress(IA_difficulty_insane, "4")
screen.onkeypress(IA_difficulty_adaptive, "5")

while True:
    screen.update()
    turtle.colormode(255)
    while not start_p:
        score_1 = 0
        score_2 = 0
        hud.clear()
        hud.write(
            "{} : {}".format(score_1, score_2),
            align="center",
            font=("Press Start 2P", 24, "normal"),
        )
        start_screen.goto(2, 115)
        start_screen.color(randint(0, 255), randint(0, 255), randint(0, 255))
        start_screen.write(
            "MY PONG GAME", align="center", font=(
                "Bodoni MT Black", 34, "normal")
        )
        start_screen.goto(0, -115)
        start_screen.color("white")
        start_screen.write(
            "(Space) - Multiplayer\n(1) - Easy\n(2) - "
            "Medium\n(3) - Hard\n(4) - Insane\n(5) - Adaptive",
            align="center",
            font=("Bodoni MT Black", 25, "normal"),
        )

        start_rec.goto(-230, -130)
        start_rec.color("white")

        start_rec.forward(460)
        start_rec.left(90)
        start_rec.forward(300)
        start_rec.left(90)
        start_rec.forward(460)
        start_rec.left(90)
        start_rec.forward(300)
        start_rec.left(90)
        start_rec.hideturtle()
    start_rec.clear()
    ball.showturtle()
    start_screen.clear()

    ball.setx(ball.xcor() + (ball.dx) + hspeed)
    ball.sety(ball.ycor() + (ball.dy))
    time.sleep(0.01)

    # speed limit
    if hspeed >= 6:
        hspeed = 6
    if hspeed <= -6:
        hspeed = -6

    # Colision with the upper wall
    if ball.ycor() > 250:
        impact.play()
        ball.sety(250)
        ball.dy *= -1

    # Colision with the lower wall
    if ball.ycor() < -280:
        impact.play()
        ball.sety(-280)
        ball.dy *= -1

    # Colision with the paddle 1
    if (
        ball.xcor() < -330
        and ball.ycor() < paddle_1.ycor() + 55
        and ball.ycor() > paddle_1.ycor() - 55
        and not (Right)
    ):
        impact_2.play()
        # variable becomes "True" when it collides with the left wall
        Right = True
        hspeed *= -1  # reverses speed to be compatible with "ball.dx"
        hspeed += (
            # increases the speed to the
            # corect direction after reverse the speed
            0.5
        )
        ball.dx *= -1
        if ball.dy < 0:
            # chooses a "ball.dy" randomly
            ball.dy = -random.choice([1, 2, 3, 4])
        else:
            ball.dy = random.choice([1, 2, 3, 4])

    # Colision with the paddle 2
    if (
        ball.xcor() > 330
        and ball.ycor() < paddle_2.ycor() + 55
        and ball.ycor() > paddle_2.ycor() - 55
        and Right
    ):
        impact_2.play()
        # variable becomes "False"
        # when it collides with the right wall
        Right = False
        hspeed *= -1  # reverses speed to be compatible with "ball.dx"
        hspeed -= (
            # increases the speed to the corect
            # direction after reverse the speed
            0.5
        )
        ball.dx *= -1
        if ball.dy < 0:
            ball.dy = -random.choice([1, 2, 3, 4])
        else:
            ball.dy = random.choice([1, 2, 3, 4])

    # Colision with the left wall
    if ball.xcor() < -390:
        paddle_1.goto(-350, 0)
        paddle_2.goto(350, 0)
        Right = True
        hspeed = 0
        ball.dx = -4
        ball.dy = -random.choice([1, 2, 3, 4])
        score_2 += 1
        if adapt:
            if distance == 80:
                distance = 59
            elif score_1 < score_2:
                distance += random.choice([1, 2, 3, 4, 5]) * (
                        score_2 - score_1
                )
            if distance > 80:
                distance = 80
        hud.clear()
        hud.write(
            "{} : {}".format(score_1, score_2),
            align="center",
            font=("Press Start 2P", 24, "normal"),
        )
        ball.goto(0, 0)
        ball.dx *= -1
        # Showing that player 2 won
        if score_2 > 5:
            bot = False
            adapt = False
            p2win = turtle.Turtle()
            p2win.hideturtle()
            p2win.goto(0, 0)
            p2win.pencolor("yellow")
            p2win.write("Player 2 wins", align="center", font=(
                "Bodoni MT Black", 35))
            time.sleep(3)
            p2win.clear()
            ball.clear()
            mixer.music.pause()
            paddle_1.goto(-350, 0)
            paddle_2.goto(350, 0)
            start_p = False  # Reset the game

    # Colision with the right wall
    if ball.xcor() > 390:
        paddle_1.goto(-350, 0)
        paddle_2.goto(350, 0)
        Right = False
        hspeed = 0
        ball.dx = 4
        ball.dy = random.choice([1, 2, 3, 4])
        score_1 += 1
        if adapt and score_1 > score_2:
            distance += random.choice([1, 2, 3, 4, 5]) * (
                score_2 - score_1
            )
            if distance < 59:
                distance = 59
        hud.clear()
        hud.write(
            "{} : {}".format(score_1, score_2),
            align="center",
            font=("Press Start 2P", 24, "normal"),
        )
        ball.goto(0, 0)
        ball.dx *= -1

        # Showing that player 1 won
        if score_1 > 5:
            bot = False
            adapt = False
            p1win = turtle.Turtle()
            p1win.hideturtle()
            p1win.goto(0, 0)
            p1win.pencolor("yellow")
            p1win.write("Player 1 wins", align="center", font=(
                "Bodoni MT Black", 35))
            time.sleep(3)
            p1win.clear()
            ball.clear()
            mixer.music.pause()
            paddle_1.goto(-350, 0)
            paddle_2.goto(350, 0)
            start_p = False  # Reset the game

    # Bot IA
    if Right and bot:
        if ball.ycor() > paddle_2.ycor() + distance:
            paddle_2.sety(paddle_2.ycor() + 30)
        elif ball.ycor() < paddle_2.ycor() - distance:
            paddle_2.sety(paddle_2.ycor() - 30)

    # Bot IA 2 (only delete the hashtags and enjoy :3)

#    if not Right and bot:
#        if ball.ycor() > paddle_1.ycor() + distance:
#            paddle_1.sety(paddle_1.ycor() + 30)
#        elif ball.ycor() < paddle_1.ycor() - distance:
#            paddle_1.sety(paddle_1.ycor() - 30)

turtle.done()
