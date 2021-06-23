#리스트의 최댓값,최솟값 정렬

score = [70,80,50,60,90,45]

max = score[0]
n = len(score)

for i in range(1,n):
    if max < score[i]: max = score[i]

print("최고점수 %d점" % max)

#오름 차순 정렬
for i in range(0,n):
    for j in range(0,n-1):
        if score[j] > score[j+1]:
            score[j] , score[j+1] = score[j+1],score[j]
    print(score)

for i in score:
    print(i,end=' ')
