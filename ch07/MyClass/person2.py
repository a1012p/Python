

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def ShowInfo(self):
        print(self.name , self.age)


p1 = Person("박대양",40)
p2 = Person("최상우",42)

print(p1.name, p1.age)
print(p2.name, p2.age)

p1.ShowInfo()
p2.ShowInfo()