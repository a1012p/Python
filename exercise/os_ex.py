import os
"""
os.chdir("C:/pyworks/exercise")
dir = os.popen("dir")
print(dir.read())
dir.close()
"""

#디렉터리 이름 - 리스트 반환

dirnams = os.listdir("c:/pyworks/exercise")

print(dirnams)          #리스트 출력
print(dirnams[0])
print(dirnams[-1])

#요소의 값 출력
for dirname in dirnams:
    print(dirname)

