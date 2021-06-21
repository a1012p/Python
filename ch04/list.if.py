#리스트의 합격 판정
#점수가 60점 이상이면 합격,불합격

print("for - in문 사용")
score = [70,80,50,60,90,45]

result=''
index=0;
for i in score:
    index +=1;
    if i >= 60:
        result='합격'
    else:
        result='불합격'
    print("%d번 학생은 %s입니다" %(index,result))
    

print('=' * 40)

print("for in range() 구문")

n = len(score)

for i in range(0,n):
    if score[i] >= 60:
        result='합격'
    else:
        result='불합격'
    print("%d번 학생은 %s입니다" %(i+1,result))
