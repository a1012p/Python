#온도 변환기 클래스
class Converters:
    def __init__(self,unit_from,unit_to,factor,offset):
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.factor = factor
        self.offset = offset

    def convert(self,value):
        return self.factor * value + self.offset

if __name__=="__main__":
    conv = Converters("C","F",1.8,32)
    print(conv.convert(40) , conv.unit_to)