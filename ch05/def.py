# 함수의 정의 및 호출
# return이 없고, 매개변수 없는 함수

def say_Hello():
    print("안녕하세요")
    
say_Hello() #호출

# return이 없고 , 매개변수 있는 함수
print("="*30)

def say_hello(name):
    str(name)
    print("%s님 반갑습니다."% name)


say_hello("장그래")
say_hello("Elsa")
say_hello(4)

