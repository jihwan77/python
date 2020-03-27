# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수
# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재
# 인스턴스 메소드 : self를 매개변수로 가지는 메소드
# Self 인스턴스화된 대상(메모리)
# 예제1
class Dog2: # object 상속  Dog, Dog(), Dog(object)

    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog2)

# 인스턴스화
a = Dog2('mikiy', 2)
b = Dog2('baby', 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

#  a.species = 'seconddog'
print(Dog2.species)
print(a.species)
print(b.species)

# 예제2
# self의 이해
class SelfTest:
    def func1(): # 클래스 메소드
        print('Func1 called')
    def func2(self): # 인스턴스 메소드
        print(id(self)) # 2156045339664
        print('Func2 called')

f = SelfTest()
print(id(f)) # 2156045339664
# print(dir(f))
# f.func1() # 예외 func1() takes 0 positional arguments but 1 was given
f.func2()

SelfTest.func1()
# SelfTest.func2() # 예외 func2() missing 1 required positional argument: 'self'
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')
# Warehouse.stock_num = 50
print(Warehouse.stock_num)
print(user1.name) # Lee
print(user2.name) # Cho
print(user1.__dict__) # {'name': 'Lee'}
print(user2.__dict__) # {'name': 'Cho'}
#인스턴스의 네임스페이스에 없으면 클래스 네임스페이스에서 찾는다
print(user1.stock_num) # 2
print(Warehouse.__dict__) # {'__module__': '__main__', 'stock_num': 2, ....}

print('>>>', user1.stock_num)
del user1 # 삭제하면 __del__를 호출하여 stock_num가 감소한다.
print('after', Warehouse.stock_num)

# 예제4
class Dog: # object 상속  Dog, Dog(), Dog(object)

    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))
