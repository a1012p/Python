
while True:
    select = input("성적을 저장할까요(y/n) 3:출력")
    if select == 'y' or select == 'Y':
        with open("scorelist.txt",'a') as f:
            name =input("이름을 입력하세요: ")
            kor = int(input("국어 성적을 입력하세요: "))
            math = int(input("수학 성적을 입력하세요: "))
            avg = (kor + math) / 2.0

            f.write(name+' ')
            f.write(str(kor)+' ')
            f.write(str(math)+' ')
            f.write(str(avg)+'\n')
    elif select == 'n' or select == 'N':
        print("프로그램을 종료합니다.")
        break;
    elif select == '3':
        with open("scorelist.txt",'r') as f:
            data = f.read()
            print(data)
    else:
        print("잘못된 입력입니다. 다시 입력해주세요")
