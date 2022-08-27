class Car():
    """
    Car class
    Author : Choi
    Date: 2022.08.27
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    # 비공식적인 즉 print문으로 문자열을 출력하는 사용자 입장의 출력을 원할 때는 str 메서드 사용
    def __str__(self):
        return f'str : {self._company} - {self._details}'
    
    # 객체, 이 자료형의 타입에 따른 객체를 그대로 표시해줄 때 사용
    def __repr__(self):
        return f'repr : {self._company} - {self._details}'
    
    # Instance Method
    # Self: 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print('Car Detail Info : {} {}'.format(self._company,self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'

# Self 의미
car1 = Car('Ferrari', {'color': 'White', 'horse': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horse': 250, 'price': 5000})
car3 = Car('Forshe', {'color': 'Red', 'horse': 330, 'price': 6000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
# 직접 접근해서 수정하는건 좋지 않음.
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 인스턴스 호출(static method)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스 호출(static method)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))