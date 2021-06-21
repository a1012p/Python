#자리 배치도 프로그램

customer_num = int(input("입장객 수 입력 : "))
col_num = int(input("좌석 열의 수 입력 : "))

row_num = customer_num // col_num;
if customer_num % col_num != 0:
    row_num += 1

#print("%d개의 줄이 필요합니다." % row_num)

print("자리 배치도")

for i in range(0,row_num):
    for j in range(1,col_num+1):
        if(customer_num <i*col_num +j): break
        print("%d자리" % (i*col_num + j) ,end=' ')
    print()
