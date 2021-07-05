import sys
import time
#1번 문제

class Calculator:
    def __init__(self):
        self.value = 0


    def add(self,val):
        self.value += val
        return self.value


class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val
        return self.value

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# 2번 문제

class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value

cal = MaxLimitCalculator()
print(cal.add(50))
print(cal.add(60))

print(cal.value)

# 3번 문제

# 4번 문제

li = [1,-2,3,-5,8,-3]
def plus(x):
    if x >= 0: return True
print(list(filter(plus ,li)))

def positive(a):
    a2 = []
    for i in a:
        if i >= 0:
            a2.append(i)
    return a2
li = [1,-2,3,-5,8,-3]
li2 = positive(li)
print(li2)

# 5번 문제

print(int(0xea))

# 6번 문제
def times(x):
    a2 = []
    for i in x:
        a2.append(i*3)
    return a2

li = [1,2,3,4]

li2 = times(li)
print(li2)

li = [1,2,3,4]

li = list(map(lambda x:x*3, li))
print(li)

# 7번 문제

def find_max(li):
    max = li[0]
    '''
    for i in range(len(li)):
        if li[i] > max:
            max = li[i]
    return max
    '''
    for i in li:
        if i > max:
            max = i
    return max


def find_min(li):
    min = li[0]
    for i in range(len(li)):
        if li[i] < min:
            min = li[i]
    return min

d1 = [-8,2,7,-3,5,0,-1]
result = max(d1) + min(d1)
print(result)

d1.sort()
result = d1[0] + d1[-1]
print(result)

max2 = find_max(d1)
min2 = find_min(d1)
print(max2 + min2)
# 8번 문제

print("%.4f" % (17 /3.0))

# # 9번 문제
#
# args = sys.argv[1:]
# list="+".join(args)
# print(eval(list))

# 12번 문제

print(time.strftime("%Y/%m/%d %H:%M:%S"))

import datetime
now = datetime.datetime.now()
print(now)
print(now.strftime("%Y/%m/%d %H:%M:%S"))

# 13번 문제
import random

#주사위 10번 던지기

dice = []
for i in range(10):
    n = random.randint(1,6)
    dice.append(n)

print(dice)

#로또 복권 생성기

lotto = []
while len(lotto) < 6:
    Rn = random.randint(1,45)
    print(Rn)
    if Rn not in lotto:     #중복 숫자 방지
        lotto.append(Rn)

print(lotto)