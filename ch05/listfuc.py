# 리스트를 매개변수로 전달하기
# 점수의 평균 계산하기

def avg(a):
    sum = 0
    global c
    c = len(a)
    for i in a:
        sum += i
    return float(sum / len(a))

kor = [70,80,60,90,100]
avg = avg(kor)

print("학생 수:",c)
print("평균 점수 :",avg)
