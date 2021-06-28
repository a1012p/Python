#숫자 추측 게임
import random as r

com = r.randint(1,30)  #컴퓨터가 정한 숫자

while True:
    try:
        guess =int(input("맞혀보세요(1~30):")) #사용자가 추측하는 숫자
        if guess > 30 or guess <1:
            print("추측 값이 게임 범위를 벗어났습니다")
        elif com < guess :
            print("너무 커요!!")
        elif com > guess:
            print("너무 작아요!!")
        else:
            print("정답!!")
            break
    except ValueError:
        print("숫자가 아닙니다.다시 입력해주세요")
