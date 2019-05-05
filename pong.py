# pong game in python 3 using tutrtle
import turtle
import os
import time

# Class for paddle
class Paddle():

    # Create a paddle with square shape and white color
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)

    # Set position of paddle on screen
    def set_position(self, x, y):
        self.paddle.penup()
        self.paddle.goto(x, y)

    # Return x and y co-ordinates
    def get_x_cor(self):
        return self.paddle.xcor()

    def get_y_cor(self):
        return self.paddle.ycor()    

    # Move paddle up and down
    def move_up(self):
        ycor = self.paddle.ycor()
        ycor += 20
        self.paddle.sety(ycor)

    def move_down(self):
        ycor = self.paddle.ycor()
        ycor -= 20
        self.paddle.sety(ycor)


# Class for ball
class Ball():
    
    # Crate ball
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('green')
        self.collisions = 0

    # set position of ball on screen
    def set_position(self, x, y):
        self.ball.penup()
        self.ball.goto(x, y)

    # get x co-ordinate of ball
    def get_x_cor(self):
        return self.ball.xcor()

    # get y co-ordinate of ball
    def get_y_cor(self):
        return self.ball.ycor()     

    # set x-directional speed of ball
    def set_dx(self, dx):
        self.ball.dx = dx

    # set y-directional speed of ball
    def set_dy(self, dy):
        self.ball.dy = dy

    # get x-directional speed of ball
    def get_dx(self):
        return self.ball.dx

    # get y-directional speed of ball
    def get_dy(self):
        return self.ball.dy

    # number of collisions with paddle            
    def set_collisions(self, collisions):
        self.collisions = collisions

    def get_collisions(self):
        return self.collisions    

# Class for palyers
class Player():
    
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score    


def init():
    # Create and initialized screen object
    wn = turtle.Screen()
    wn.title('Pong')                    # Set title of screen
    wn.bgcolor('black')                 # Set background color
    wn.setup(width=800, height=600)     # Set width and height
    wn.tracer(0)
    return wn                        # Set tracer


# keyboard bindings
def set_key_listeners(wn, paddle_a, paddle_b):
    wn.listen()
    wn.onkeypress(paddle_a.move_up, "w")
    wn.onkeypress(paddle_a.move_down, "s")
    wn.onkeypress(paddle_b.move_up, "Up")
    wn.onkeypress(paddle_b.move_down, "Down")


# Pen to write player scores
def create_pen():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color('yellow')
    pen.penup()
    pen.hideturtle()                    # Hide turtle so that it does not show up on screen
    pen.goto(0, 260)
    return pen



# Create and set window
wn = init()

# Show main title for 5 seconds
main_title = create_pen()
main_title.goto(0, 0)
main_title.write("Welcome to the Pong Game!!!", align="center", font=("Courier", 24, "bold"))
main_title.goto(0, -40)
main_title.write("**Developed by Abhijeet Gurle**", align="center", font=("Courier", 10, "italic"))
time.sleep(5)
main_title.clear()

# Paddle A
paddle_a = Paddle()
paddle_a.set_position(-350, 0)

# Paddle B
paddle_b = Paddle()
paddle_b.set_position(350, 0)

# set keyboard listeners
set_key_listeners(wn, paddle_a, paddle_b)

# Ball
ball = Ball()
ball.set_position(0, 0)
ball.set_dx(0.3)
ball.set_dy(0.3) 

# Players
player_a = Player("Player A")
player_b = Player("Player B")

# Create and write using pen
pen = create_pen()
pen.write("{}: {}   {}: {}".format(player_a.get_name(), player_a.get_score(), player_b.get_name(), player_b.get_score()), align="center", font=("Courier", 24, "normal"))

            
# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.set_position(ball.get_x_cor() + ball.get_dx(), ball.get_y_cor() + ball.get_dy())

    # Border checking

    # Top and bottom
    if(ball.get_y_cor() > 290):
        ball.set_position(ball.get_x_cor(), 290)
        ball.set_dy(-1 * ball.get_dy())
        os.system("aplay bounce.wav&")

    elif(ball.get_y_cor() < -290):
        ball.set_position(ball.get_x_cor(), -290)
        ball.set_dy(-1 * ball.get_dy())
        os.system("aplay bounce.wav&")

    # Right and Left
    if(ball.get_x_cor() > 350):
        player_a.set_score(player_a.get_score() + 1)
        pen.clear()
        pen.write("{}: {}   {}: {}".format(player_a.get_name(), player_a.get_score(), player_b.get_name(), player_b.get_score()), align="center", font=("Courier", 24, "normal"))
        ball.set_position(0, 0)
        ball.set_dx(-0.3)
        ball.set_dy(0.3)
        ball.set_collisions(0)

    elif(ball.get_x_cor() < -350):
        player_b.set_score(player_b.get_score() + 1)   
        pen.clear()
        pen.write("{}: {}   {}: {}".format(player_a.get_name(), player_a.get_score(), player_b.get_name(), player_b.get_score()), align="center", font=("Courier", 24, "normal"))
        ball.set_position(0, 0)
        ball.set_dx(0.3)
        ball.set_dy(0.3)
        ball.set_collisions(0)

    # Paddle and ball collision
    if(ball.get_x_cor() > 340 and ball.get_y_cor() > paddle_b.get_y_cor() - 50 and ball.get_y_cor() < paddle_b.get_y_cor() + 50):
        ball.set_dx(-1 * ball.get_dx())
        os.system("aplay bounce.wav&")
        ball.set_collisions(ball.get_collisions() + 1)

        # increase speed when collision happens
        if(ball.get_collisions() % 10 == 0):
            ball.set_dx(ball.get_dx() * 1.01)
            ball.set_dy(ball.get_dy() * 1.01)

    elif(ball.get_x_cor() < -340 and ball.get_y_cor() > paddle_a.get_y_cor() - 50 and ball.get_y_cor() < paddle_a.get_y_cor() + 50):
        ball.set_dx(-1 * ball.get_dx())
        os.system("aplay bounce.wav&")
        ball.set_collisions(ball.get_collisions() + 1)

        # increase speed when collision happens
        if(ball.get_collisions() % 10 == 0):
            ball.set_dx(ball.get_dx() * 1.01)
            ball.set_dy(ball.get_dy() * 1.01)

    # Paddle and boundry collision
    if(paddle_a.get_y_cor() + 50 > 300):
        paddle_a.set_position(paddle_a.get_x_cor(), 250)

    if(paddle_b.get_y_cor() + 50 > 300):
        paddle_b.set_position(paddle_b.get_x_cor(), 250)    

    if(paddle_a.get_y_cor() - 50 < -300):
        paddle_a.set_position(paddle_a.get_x_cor(), -250)

    if(paddle_b.get_y_cor() - 50 < -300):
        paddle_b.set_position(paddle_b.get_x_cor(), -250)
           


