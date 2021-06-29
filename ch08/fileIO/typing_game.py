
import time
import random

f = open("word.txt",'r')
quiz = f.read().split()
random.shuffle(quiz)

f.close()

n = 0 #문제 번호
print('[타자 게임]준비되면 엔터')
input()
start = time.time() #단어 랜덤 선택
wrong = 0

while n < len(quiz):
    print("문제",n+1,"번")
    print(quiz[n])
    x = input() #사용자가 단어를 따라 입력
    if x == quiz[n]:
        print("정확합니다")
        n += 1
    else:
        wrong += 1
        print("오타입니다!다시 입력하세요")

end = time.time()
result = end - start;
print("시간: %.2f초" % result)
print("오타횟수:%d"% wrong)
print('게임 종료')