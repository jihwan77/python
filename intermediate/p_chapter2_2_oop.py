# 객체 지향 프로그래밍 (OOP) -> 코드의 재사용, 코드의 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트 (프로그램) -> 함수 중심 -> 데이타 방대 -> 복잡
# 클래스 중심 -> 데이타 중심 -> 객체로 관리

class Car():
    """
    Car Class
    Author : Seo
    Date : 2020.02.28
    """
    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details): # self를 받는건 인스턴스 메소드
        self._company = company
        self._details = details
        # self.car_count = 10 동일한 변수명 가능
        Car.car_count += 1
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    def __del__(self):
        Car.car_count -= 1
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price'))) # self._details['price']

# self 의미 (인스턴스 내부에 고유의 값을 저장하기의한 예약된 지시어)
car1 = Car('Ferrai', {'color':'White', 'horsepower':400, 'price':8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270, 'price':5000})
car3 = Car('Audi', {'color':'Silver', 'horsepower':300, 'price':6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info()
Car.detail_info(car1) 
car2.detail_info()
Car.detail_info(car2) 

# 에러 클래스로 호출하면 self 를 넘겨줘야 함
# Car.detail_info() # TypeError: detail_info() missing 1 required positional argument: 'self'

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))

# 공유확인
print(car1.__dict__) ## 인스턴스만 출력
print(car1.car_count)
print(car2.__dict__)
print(car2.car_count)

print(dir(car1)) # 클래스 변수도 출력

# 접근
print(car1.car_count)
print(Car.car_count) # 정석

del car2
# 삭제확인
print(car1.car_count)
print(Car.car_count) # 정석

# 인스턴스 네임스페이스(dir, __dict__)에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위 (클래스 변수, 부모클래스 변수)