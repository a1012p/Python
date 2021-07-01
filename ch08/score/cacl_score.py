
with open("scorelist.txt",'r') as f:
    d2 = [] #이차원리스트
    for i in range(3):
        d2.append(f.readline().split())
        # d2[i].append(int(d2[i][1]) + int(d2[i][2]))
        # d2[i].append( int(d2[i][3]) / 2)

    for i in range(len(d2)):
        d2[i][1] = int(d2[i][1])            #국어 (숫자형 변경) = 2열
        d2[i][2] = int(d2[i][2])            #수학 (숫자형 변경) = 3열
        d2[i].append(d2[i][1] + d2[i][2])   #총점             = 4열
        d2[i].append(d2[i][3] / 2)          #평균             = 5열

    print(('*' *10) + "성 적 표" +('*' *10))
    print('=' *27)
    print("이름   국어  수학   총점  평균")
    for i in range(len(d2)):
        print("{0}  {1}   {2}    {3}  {4}".format(d2[i][0],d2[i][1],d2[i][2],d2[i][3],d2[i][4]))
    print('='*27)
    print(('*' *9) + "과목별 평균" +('*' *9))
    kor_sum = 0
    math_sum = 0
    for i in range(len(d2)):
        kor_sum += d2[i][1]
        math_sum += d2[i][2]
    print("국어 평균: %.1f 수학 평균: %.1f" % (kor_sum / len(d2) , math_sum / len(d2)))