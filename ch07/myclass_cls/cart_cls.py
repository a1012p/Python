# Cart 클래스 - 클래스 리스트

class Cart:

    li = []

    def __init__(self,goods):
        Cart.li.append(goods)

    def showinfo(self):
        print(Cart.li)



c1 = Cart("양파")
c1.showinfo()
c2 = Cart("커피")
c2.showinfo()
c3 = Cart("우유")
c3.showinfo()