# abs() 직접 정의해보자
# 절댓값 알고리즘1
import math #math 모듈 호출

def abs_sign(x):
    if x<0 : x = -x
    return x
# 절댓값2
def abs_square(x):
    x = x**2
    return int(math.sqrt(x)) #제곱근 함수 sqrt()

n1 = abs_sign(-3)
n2 = abs_square(-4)

print(n1)
print(n2)
