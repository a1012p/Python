# 여러개의 원 만들기
import turtle as t

n = 120
t.bgcolor('black')
t.color('yellow')

t.speed(0) #1~9


for i in range(n):
    t.circle(80)
    t.left(360/n)


t.mainloop()