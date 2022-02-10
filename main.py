import turtle
import time
import random

screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.tracer(0)


placar = turtle.Turtle()
placar.hideturtle()
placar.penup()
placar.goto(249,259)
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
bot = False     #variable that defines if bot is active or not
distance = 0    #variable that defines the margin of error of the bot

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
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
player2.write(" Player 2", align="right", font=("Bodoni MT Black", 24, "normal"))

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
    if bot == False:
        if y < 250:
            y += 30
        else:
            y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    global bot
    if bot == False:
        if y > -250:
            y += -30
        else:
            y = -250
    paddle_2.sety(y)


def start_game():
    global start_p
    start_p = True
    print("2 Players")


def IA_difficulty_easy():
    global start_p, distance, bot
    if start_p == False:
        distance = 75
        bot = True
        print("Easy")
    start_p = True

def IA_difficulty_medium():
    global start_p, distance, bot
    if start_p == False:
        distance = 70
        bot = True
        print("Medium")
    start_p = True

def IA_difficulty_hard():
    global start_p, distance, bot
    if start_p == False:
        distance = 65
        bot = True
        print("Hard")
    start_p = True

def IA_difficulty_insane():
    global start_p, distance, bot
    if start_p == False:
        distance = 59   #the smallest possible margin of error, below that, AI becomes impossible
        bot = True
        print("insane")
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


while True:
    screen.update()

    while not start_p:
        score_1 = 0
        score_2 = 0
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        start_screen.goto(0,100)
        start_screen.color("yellow")
        start_screen.write(" MY PONG GAME", align="center", font=("Bodoni MT Black", 33, "normal"))
        start_screen.goto(0,-94)
        start_screen.color("white")
        start_screen.write("(Space) - Multiplayer\n(1) - Easy\n(2) - Medium\n(3) - Hard\n(4) - Insane", align="center", font=("Bodoni MT Black", 24, "normal"))
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
        # os.system("afplay bounce.wav&")
        ball.sety(250)
        ball.dy *= -1

    # Colision with the lower wall
    if ball.ycor() < -280:
        # os.system("afplay bounce.wav&")
        ball.sety(-280)
        ball.dy *= -1

    # Colision with the paddle 1
    if ball.xcor() < -330 and ball.ycor() < paddle_1.ycor() + 55 and ball.ycor() > paddle_1.ycor() - 55 and Right == False:
        Right = True  # variable becomes "True" when it collides with the left wall
        hspeed *= -1  # reverses speed to be compatible with "ball.dx"
        hspeed += 0.5  # increases the speed to the corect direction after reverse the speed
        ball.dx *= -1
        if ball.dy < 0:
            ball.dy = -random.choice([1, 2, 3, 4]) # chooses a "ball.dy" randomly
        else:
            ball.dy = random.choice([1, 2, 3, 4])

    # Colision with the paddle 2
    if ball.xcor() > 330 and ball.ycor() < paddle_2.ycor() + 55 and ball.ycor() > paddle_2.ycor() - 55 and Right == True:
        Right = False  # variable becomes "False" when it collides with the right wall
        hspeed *= -1  # reverses speed to be compatible with "ball.dx"
        hspeed -= 0.5  # increases the speed to the corect direction after reverse the speed
        ball.dx *= -1
        if ball.dy < 0:
            ball.dy = -random.choice([1, 2, 3, 4])
        else:
            ball.dy = random.choice([1, 2, 3, 4])

    # Colision with the left wall
    if ball.xcor() < -390:
        Right = True
        hspeed = 0
        ball.dx = -4
        ball.dy = -random.choice([1, 2, 3, 4])
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        # Showing that player 2 won
        if score_2 > 5:
            p2win = turtle.Turtle()
            p2win.hideturtle()
            p2win.goto(0, 0)
            p2win.pencolor("yellow")
            p2win.write("Player 2 wins", align="center", font=("Bodoni MT Black", 35))
            time.sleep(3)
            p2win.clear()
            ball.clear()
            start_p = False  # Reset the game

    # Colision with the right wall
    if ball.xcor() > 390:
        Right = False
        hspeed = 0
        ball.dx = 4
        ball.dy = random.choice([1, 2, 3, 4])
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        # Showing that player 1 won
        if score_1 > 5:
            p1win = turtle.Turtle()
            p1win.hideturtle()
            p1win.goto(0, 0)
            p1win.pencolor("yellow")
            p1win.write("Player 1 wins", align="center", font=("Bodoni MT Black", 35))
            time.sleep(3)
            p1win.clear()
            ball.clear()
            start_p = False # Reset the game 

    # Bot IA
    if Right == True and bot == True:
        if ball.ycor() > paddle_2.ycor() + distance:
                paddle_2.sety(paddle_2.ycor() + 30)
        elif ball.ycor() < paddle_2.ycor() - distance:
                paddle_2.sety(paddle_2.ycor() - 30)

turtle.done()