import re

# 그룹핑된 문자열에 이름 붙이기
#?<그룹이름>
p = re.compile("(?P<name>\w+)\s(?P<Phone>\d+[-]\d+[-]\d+)")
m = p.search("jang 010-1234-5678")
print(m.group("name"))
print(m.group(1))
print(m.group("Phone"))
print(m.group(2))