
def gugu(dan):
    li = []
    for i in range(1,10):
        li.append(i*dan)
    return li


dan = int(input("구구단을 출력할 숫자를 입력하세요(2~9)"))
lis = gugu(dan)
print(lis)