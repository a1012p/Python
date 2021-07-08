import re

#태그를 추출하고 싶을 때
string = "abcd<hr>Thank you<head>"

#p = re.compile("<(.*)>") #태그를 제외하고 괄호 안의 내용
#p = re.compile("(<.*>)")    #태그를 포함한 내용
p = re.compile("<\w*>")
m = re.findall(p,string)
print(m)