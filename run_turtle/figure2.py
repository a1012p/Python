#도형 그리기

import turtle as t
import random as r

t.shape("turtle")

#사각형 그리기
n = 4

for i in range(n):
    t.forward(100)
    t.right(360/n)


#삼각형 그리기
t.color('red')
t.pensize(2)
n = 3
for i in range(n):
    t.forward(100)
    t.left(360/n)

#원 그리기
t.color('blue')
t.pensize(3)
t.speed(20)
for i in range(10):
    t.left(36)
    t.circle(50)
    

t.mainloop()