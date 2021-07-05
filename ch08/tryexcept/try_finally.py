#try ~ except ~ finally

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError as z:
        print(z)
        print("0으로 나눌수 없습니다")
    else:
        print(result , "입니다")
    finally:
        print("여기는 무조건 실행되는 구문입니다.")

#divide(3,5)
divide(3,0)