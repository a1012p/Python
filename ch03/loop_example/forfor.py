#중첩 for문 

for i in range(1,6):
    for j in range(1,6):
        print('가',end=' ')
    print()
    
#1부터 1씩 증가하기
for i in range(0,5):
    for j in range(1,6):
        num = i*len(range(1,6))+j
        print(num,end='  ') if(num < 10) else print(num,end=' ')
    print()
