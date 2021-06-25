#Calculatorf를 확장한 MoreCalculator 클래스 만들기
from ch07.MyClass.calculator import Calculator

class MoreCalculator(Calculator):
    def pow(self):
        print("x=",self.x**2 , "y=",self.y**2)
    def div(self):
        if self.y == 0:
            return "0으로 나눌 수 없습니다"
        else:
            return super().div()




c = MoreCalculator(2,0)
c.pow()
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())
