import re

p = re.compile("(\w+)\s(\d+[-]\d+[-]\d+)")
m = p.search("jang 010-1234-5678")
print(m.group(1))
print(m.group(2))