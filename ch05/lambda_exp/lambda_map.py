# map() - 값을 매핑
# filter() - 어떤 조건으로 값을 필터링
li = [1,2,3,4,5]

li2 = list(map(lambda x : x *3,li))
print(li2)
print(list(map(lambda x : x *3 ,li)))

#4보다 작은 요소 추출
li3 = list(filter(lambda n : n < 4 , li))
print(li3)
print(list(filter(lambda n : n < 4 , li)))

