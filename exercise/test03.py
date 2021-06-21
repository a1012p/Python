# 1번
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# 2번
result = 0
i = 1
while i <= 1000:
    if(i % 3==0):
        result += i
    i+= 1


print(result)


# 3번

i = 0
while True:
    i += 1
    if i > 5 :break
    print("*" * i)

#중첩 for문

for i in range(0,5):
    for j in range(0,i+1):
       print("*",end='')
    print()


# 4번

for i in range(0,100):
    print(i+1)

