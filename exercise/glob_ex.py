import glob

#data를 리스트형으로 반환
data = glob.glob("c:/pyworks/exercise/*.py")

print(data[0])
print(data[-1])
print(data)

for i in data:
    print(i)