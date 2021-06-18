# 놀이 공원 입장료 계산

age = int(input("나이 입력 : "))
charge = 0;

if 8 > age:
    print("미취학 아동입니다")
    charge = 1000
elif 14 > age:
    print("초등학생입니다")
    charge = 1500
elif 20 > age:
    print("중,고등학생입니다")
    charge =2000
else:
    print("성인입니다")
    charge = 2500

print("입장료는 %d원 입니다." % charge)
