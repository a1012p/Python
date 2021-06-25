import turtle as t
import random

def turn_right(): #오른쪽 화살키
    t.setheading(0)

def turn_up(): #위쪽 화살키
    t.setheading(90)

def turn_left(): #왼쪽 화살키
    t.setheading(180)

def turn_down():    #아래쪽 화살키
    t.setheading(270)


def play():
    t.forward(speed)
    enermy.setheading(enermy.towards(t.pos()))
    enermy.forward(9)
    if t.distance(tf.pos()) < 12:
        tf.goto(random.randint(-230,230),random.randint(-230,230))

    if t.distance(enermy.pos()) >= 12:      #12보다 작으면 잡혀서 게임종료
        t.ontimer(play,10)                  #0.1초

speed = 10;

t.setup(500,500)
t.bgcolor('orange')
t.shape('turtle')
t.speed(0)
t.up()
t.color('white')
t.title("달려라 거북이")

enermy = t.Turtle('turtle')
enermy.speed(0)
enermy.up()
enermy.color('red')
enermy.goto(200,200)

#먹이

tf = t.Turtle('circle')
tf.color('green')
tf.up()
tf.speed(0)
tf.goto(100,-100)

t.onkeypress(turn_right,'Right')
t.onkeypress(turn_left,'Left')
t.onkeypress(turn_up,'Up')
t.onkeypress(turn_down,'Down')
t.listen()

play()

t.mainloop()