#전역변수(정적변수) - 누적 공유되는 변수
# global 키워드 사용

def one_up():
    global x    #x를 전역변수로 사용
    x = x+1
    return x

x = 0

def ak():
    global c
    c = 2
    print(id(c))

print(one_up())

ak()
ak()
