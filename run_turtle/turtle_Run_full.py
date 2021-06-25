import turtle as t
import random

score = 0
playing = False

def turn_right(): #오른쪽 화살키
    t.setheading(0)

def turn_up(): #위쪽 화살키
    t.setheading(90)

def turn_left(): #왼쪽 화살키
    t.setheading(180)

def turn_down():    #아래쪽 화살키
    t.setheading(270)

def start():
    global playing

    if playing == False:
        playing = True
        t.clear()
        play()

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("",20))
    t.home()

def play():
    global playing
    global score

    t.forward(10)

    if t.xcor() > 260:
        t.setx(t.xcor()- 500)
    if t.xcor() < -260:
        t.setx(t.xcor() +500)
    if t.ycor() > 260:
        t.sety(t.ycor() -500)
    if t.ycor() < -260:
        t.sety(t.ycor() + 500)

    if random.randint(1,5) == 3:
        angle = enermy.towards(t.pos())
        enermy.setheading(angle)

    enermy.forward(5 + score)

    if t.distance(tf.pos()) <= 12:
        tf.goto(random.randint(-230,230),random.randint(-230,230))
        score += 1
        t.write("{}".format(score),False,"center",("",10))

    if t.distance(enermy.pos()) <= 12:
        text = "Score : " + str(score)
        message("Game Over" , text)
        playing = False
        score = 0

    if playing:
        t.ontimer(play,100)




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
t.onkeypress(start,'space')

t.listen()

message("Turtle Run","[Space]")


t.mainloop()