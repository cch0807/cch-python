# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Choi
    Date: 2022.08.26
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0


    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1
    
    # 비공식적인 즉 print문으로 문자열을 출력하는 사용자 입장의 출력을 원할 때는 str 메서드 사용
    def __str__(self):
        return f'str : {self._company} - {self._details}'
    
    # 객체, 이 자료형의 타입에 따른 객체를 그대로 표시해줄 때 사용
    def __repr__(self):
        return f'repr : {self._company} - {self._details}'
    
    def detail_info(self):
        print(f'Current ID : {id(self)}')
        # print(f'Car Detail Info : {self._company} {self._details.}')
        print('Car Detail Info : {} {}'.format(self._company,self._details.get('price')))

    def __del__(self):
        print('del 호출 확인')
        Car.car_count -= 1
# Self 의미
car1 = Car('Ferrari', {'color': 'White', 'horse': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horse': 250, 'price': 5000})
car3 = Car('Forshe', {'color': 'Red', 'horse': 330, 'price': 6000})

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
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info()
car2.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))

print()
print()

# # 에러
# Car.detail_info()

# 공유확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

del car2

# 삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수))