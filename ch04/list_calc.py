# 리스트의 연산

score = [70,80,50,60,90,45]

count = len(score)
avg = 0.0
sum = 0

# 합계
for i in score:
    sum += i;
    print("i = %d , sum = %d" %(i , sum))

print("합계 : %d" % sum)
print("개수 : %d개" % count)

# 평균
avg = sum / count

print("평균 : %.1f" % avg)
