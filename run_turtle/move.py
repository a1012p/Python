import turtle as t
import random as r
t.shape("turtle")

t.speed(0)
t.up()
#시작시 랜덤하게 나타나기
t.goto(r.randint(-200,200),r.randint(-200,200))
x ,y =t.pos()









t.mainloop()