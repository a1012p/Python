#Person 클래스 생성과 사용

class Person:

    def __init__(self):
        self.__name = "홍길동"
        self.__age = 30

    def getname(self):
        return self.__name
    def getage(self):
        return self.__age

p1 = Person() #객체변수 - 인스턴스(instance)
print(p1.getname())
print(p1.getage())