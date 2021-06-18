# 조건 : 현금 또는 카드가 있으면 택시를 타고, 없으면 걸어간다.

money = 3000;
card = True;

if money > 4000 or not card:
    print("택시를 탄다")
else:
    print("걸어 간다")

pocket = ['paper','스마트폰','money']

if 'paper' in pocket:
    print("택시를 탄다")
else:
    print("걸어 간다")
