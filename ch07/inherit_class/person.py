class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    pass


if __name__ == "__main__":
    p1 = Person("황태환", 27)
    print(p1.name, p1.age)

    e1 = Employee("남한강", 30)
    print(e1.name, e1.age)
