import turtle as t

#다른 곳에 도형 그리기
t.shape('turtle')

def polygon(n , size = 100):
    for x in range(n):
        t.forward(size)
        t.left(360/n)

def polygon2(n,d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)

polygon(5)
polygon(3)

t.up() #펜 올리기

t.back(100) # 100px 뒤로 이동

t.down() #펜 내리기

polygon2(4,80)
polygon2(5,100)
