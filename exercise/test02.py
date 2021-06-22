#1번 문제

korean = 80
english = 75
math = 55

SubjectSum = korean + english + math;
avg = SubjectSum /3 

print("모든 과목의 평균은 %.2f입니다" % avg)

#2번 문제

n = 13
if n % 2 == 0:
    print("짝수")
else:
    print("홀수")

#3번 문제

pin = "881120-1068234"
yyyymmdd ="19"+pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#4번 문제

gender = pin[7:8]
if gender == '1':
    print("남자")
else:
    print("여자")

#5번 문제

a = "a:b:c:d"
b = a.replace(":","#")
print(b)

#6번 문제

a = [1,3,4,5,2]
a.sort()    #오름차순 정렬
a.reverse() #내림차순으로 정렬
print(a)

#7번 문제
a = ['Life','is','too','short']
result = " ".join(a);
print(result)

#split() 예제
s = "Life is too short"
a = s.split()
print(a)

s = "a:b:c:d"
s = s.split(':')
print(s)

#8번 문제
a = (1,2,3)
a = a + (4,)
print(a)

#9번 문제
a = {}

a['name'] = 'python'
a[('a',)] = 'python'
##a[[1]] = 'python'
a[250] = 'python'

#10번 문제

a={'A':90,'B':80,'C':70}
result = a.pop('B')
print(a)
print(result)

#11번 문제

a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)
