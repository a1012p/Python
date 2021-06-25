# Cart 클래스 - 인스턴스 리스트

class Cart:
    def __init__(self,goods):
        self.li = []
        self.li.append(goods)

    def showinfo(self):
        print(self.li)


c1 = Cart("양파")
c1.showinfo()
c2 = Cart("커피")
c2.showinfo()
c3 = Cart("우유")
c3.showinfo()