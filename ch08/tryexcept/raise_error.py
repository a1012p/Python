# raise -> 에러를 미뤄둔다. 사용하는 쪽에서 발생하도록 함
class Bird:
    def fly(self):
        print("새가 날아갑니다.")
        raise NotImplementedError

class Eagle(Bird):
    #pass
    def fly(self):
        print("독수리가 날아 오릅니다")

# bird = Bird()
# bird.fly()
eagle = Eagle()
eagle.fly()

li = list(i * 3 for i in [1,2,3,4] if i % 2 == 0)
print(sum(li))
print(li)

li = list(filter(lambda x: x>=0,[1,-2,3,-5,8,-3]))
print(li)