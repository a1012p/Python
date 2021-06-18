currentYear = 2021

birthYear = int(input("태어난 연도를 입력하세요 : "))

age = currentYear - birthYear + 1

print(birthYear , "년에 태어난 사람의 나이는",age,"세입니다")
print("{0}년에 태어난 사람의 나이는 {1}세입니다".format(birthYear,age))
