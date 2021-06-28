from ch07.MyClass.converter import ScaleCoverter
#단위 변환 클래스 확장
#온도 변환 : 화씨온도(F) = 섭씨온도(C) x 1.8 + 32
class Converters(ScaleCoverter):
    def __init__(self,unit_from,unit_to,factor,offset):
        super().__init__(unit_from,unit_to,factor)
        self.offset = offset

    def convert(self,value):        #부모 메서드 이름이 같고 내용이 다르다 : 오버라이딩(재정의)
        return value * self.factor + self.offset

con = Converters('C','F',1.8,32)
print("Converting 23C")
print(str(con.convert(23))+ con.unit_to)