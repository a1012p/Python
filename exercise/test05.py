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