import re

str = "12345yy7890 hi 999 Hello"

m = re.findall('\w{1,3}',str)
print(m)

m2 = re.search("^(123)[\w ]+[llo]$",str)
print(m2)