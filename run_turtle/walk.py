# 랜덤하게 거북이가 걸어가기

import turtle as t
import random as r

t.shape("turtle")
t.speed(0)
t.bgcolor('pink')
#t.setup(500,500)

for x in range(300):    # 거북이가 100번 움직임
    angle = r.randint(1,360)
    t.setheading(angle) #거북이의 머리 방향
    t.forward(10)


t.mainloop()