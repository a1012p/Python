import re

str = "park 010-1234-5678"
p = re.compile('(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')

#m = re.search(p,str)
#print(m.group(0)) #전체 문자열 반환
#print(m.group(1))
#print(m.group(2))

p = re.compile('(\w+)\s+(\d+[-]\d+[-]\d+)')
#s = p.sub("이름:\g<name> 번호:\g<phone>",str)  #이름을 사용
s = p.sub("이름:\g<1> 번호:\g<2>",str)          #참조 번호를 사용
print(s)
print(str)

