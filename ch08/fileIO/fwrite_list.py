import random

f = open("c:/pyfile/2021kbo.txt",'w')
team = ['기아','삼성','한화','LG','NC','키움','KT','SSG','롯데']
for i in team:
    f.write(i + " ")
    '''
f.write("\n")
f.write(" ".join(team))
f.write("\n")
for i in range(len(team)):
    f.write(team[i] + " ")
f.close()
'''

f = open("c:/pyfile/2021kbo.txt",'r')

data = f.read()
print(data)
f.close()

