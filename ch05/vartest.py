# vartest.py

a = 1 #전역 변수
def vartest(a): # call by value
    #global a
    a += 1      # a : 지역 변수(매개 변수)

vartest(a)
print(a)
