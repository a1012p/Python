
while True:
    try:
        x = int(input("숫자를 입력하세요: "))
        print(x)
        break
    except ValueError as e:
        print("해당 문자는 int 자료형의 기본문자가 아닙니다.")