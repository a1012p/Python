#도형의 면적 계산기
def square(w,h):
    area = w*h
    return area

def triangle(w,h = 0):
    if h != 0:
        area2 = w*h /2.0
    else:
        area2 = w / 2.0
    return area2

print('사각형의 면적 : ' ,square(5,4))
print('삼각형의 면적 : ', triangle(4,7))
print('삼각형의 면적 : ', triangle(24))
