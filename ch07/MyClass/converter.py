
class ScaleCoverter:
    def __init__(self,unit_from,unit_to,factor):
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.factor = factor

    def convert(self,unit): #self.factor : 25.4
        return unit * self.factor





if __name__ == "__main__":
    s = ScaleCoverter("inches","mm",25.4)
    print("Converting 2 inches")
    print(str(s.convert(2)) + s.unit_to)