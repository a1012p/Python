import re

#'*'는 앞 문자가 0개 이상 반복(없어도 가능)
p = re.compile('ca*t')
m = re.findall(p,"caat")
print(m)

m = re.findall(p,"ct")
print(m)

p2 = re.compile('ca+t')
m2 = re.findall(p2,"caat")
print(m2)

m2 = re.findall(p2,"ct")
print(m2)