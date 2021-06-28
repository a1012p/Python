# 멤버 매개변수가 있는 상속
from person import Person

class Employee(Person):
    def __init__(self,name,age,empid):
        super().__init__(name,age) #부모 멤버는 super()를 사용
        self.empid = empid

    def getname(self):              #캡슐화(정보은닉) - get() 메서드 접근자사용
        return self.name

    def getage(self):
        return self.age

    def getempid(self):
        return self.empid



e1 = Employee("북한산",20,222)
print("이름 : " , e1.getname())
print("나이 : " , e1.getage())
print("사원번호 : " , e1.getempid())

e2 = Employee("금강",30,202)
print("이름 : ",e2.getname())
print("나이 : ",e2.getage())
print("사원번호 : ",e2.getempid())
