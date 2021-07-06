import re

#()로 구분해서 이름과 전화번호를 분리해서 추출
p = re.compile("(\w+)\s(\d+[-]\d+[-]\d+)")
m = p.search("jang 010-1234-5678")
print(m.group(1))
print(m.group(2))