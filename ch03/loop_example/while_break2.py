#while ~ break

while True:
    print("반복을 계속할까요 [Y/N] : ")
    answer = input()
    if answer == 'n' or answer == 'N':
        print("반복을 중단합니다")
        break
    elif answer == 'y' or answer == 'Y':
        print("반복을 계속 합니다")
    else:
        print("잘못된 입력입니다")
