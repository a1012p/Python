#with ~ as 구문은 변수명.close()를 생략

with open("data.txt",'w') as f:
    f.write("with ~ as 구문\n")
    f.write("test중입니다\n")
    f.write("%d\n" % 15000)
    unit = "1 inch는 %.2fcm입니다." % 2.54
    f.write(unit)

with open("data.txt",'r') as fr:
    data = fr.read()
    print(data)