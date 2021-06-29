# 파일 열기(open()) -> 파일쓰기(fwrite()) -> 파일 닫기(close())
f = open("c:\pyfile\hello.txt",'w')
f.write("Hello python~\n")
f.write(str(40))
f.write(chr(70))
f.write("\n%.1f" % 7.3)
f.write("안녕~ 파이썬")
#숫자는 입력불가 - 포맷 방식으로 입력 가능
f.close()