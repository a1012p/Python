#정규 표현식 예제
import re

p1 = re.compile('[a-z]+')       #+는 반복을 의미하는 메타 문자
result = p1.match('afternoon')
print(result)

#p = re.compile('a.b') # .은 임의의 문자1개 메타 문자
p = re.compile('a+b') #+는 앞문자 1개 이상인 메타 문자
m = p.match("aab aaab aaaab")
m2 = p.findall("aabb aaabbbb aaaabbbbb")
print(m2)
print(m)