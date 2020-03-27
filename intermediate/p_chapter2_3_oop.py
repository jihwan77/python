# 객체 지향 프로그래밍 (OOP) -> 코드의 재사용, 코드의 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트 (프로그램) -> 함수 중심 -> 데이타 방대 -> 복잡
# 클래스 중심 -> 데이타 중심 -> 객체로 관리

class Car():
    """
    Car Class
    Author : Seo
    Date : 2020.02.28
    Description : Class, Static, Instance Method
    """
    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
    # Instance Method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self): # self가 들어가 있으면 인스턴스 메소드
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price'))) # self._details['price']

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per): # cls가 들어가 있으면 클래스 메소드
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Successed! price increased.')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'

# self 의미 (인스턴스 내부에 고유의 값을 저장하기의한 예약된 지시어)
car1 = Car('Ferrai', {'color':'White', 'horsepower':400, 'price':8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270, 'price':5000})

# 전체정보
car1.detail_info()
car2.detail_info()

# 가격정보 (직접접근)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보 (인상전)
print(car1.get_price())
print(car2.get_price())

''''''''''''''''''
# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보 (인상후)
print(car1.get_price_culc())
print(car2.get_price_culc())
''''''''''''''''''
# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격정보 (인상후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 인스턴스로 호출(스테이틱)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출(스테이틱)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))