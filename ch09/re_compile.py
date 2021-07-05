#정규 표현식 예제
import re

p1 = re.compile('[a-z]+')       #+는 반복을 의미하는 메타 문자
result = p1.match('afternoon')
print(result)