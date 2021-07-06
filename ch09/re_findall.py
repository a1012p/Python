#정규 표현식 예제
import re
str= "Two is too"
f1 = re.findall('T[ow]o',str)
print(f1)

f2 = re.findall('T[ow]o',str,re.IGNORECASE)
print(f2)

f3 = re.findall("t[^w]o",str,re.IGNORECASE)
print(f3)

p = re.compile('a.b')
m = p.match('a3b')
print(m)