#정사각형의 넓이

size = int(input("한변의 길이 : "))
area = size**2

#print("정사각형의 넓이 : ",area,"cm²")
print("정사각형의 넓이 : %dcm²" % area)


#삼각형의 넓이
width = int(input("밑변의 길이 : "))
height = int(input("높이 : "))

area = width * height * 0.5

print("삼각형의 넓이 : %fcm²" % area)
