import math
def getpage(x,y):
    return math.ceil(x / y)

print("""게시글의      페이지당 보여줄 
총 건수        게시글 수            페이지 번호""")
for i in range(5,36,10):
    print("%2d               %2d                   %.0f" % (i,10,getpage(i,10)))