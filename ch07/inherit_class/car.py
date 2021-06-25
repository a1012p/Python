#Car 부모 클래스 - Bus , Taxi 자식 클래스
#메서드 재정의(overriding) 상속의 경우
class Car:
    def drive(self):
        print("차가 움직인다")

class Taxi(Car):
    def drive(self):
        print("택시가 움직인다")

class Bus(Car):
    def drive(self):
        print("버스가 움직인다")



c = Car()
c.drive()
t = Taxi()
t.drive()
b = Bus()
b.drive()