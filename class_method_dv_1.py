# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩


# 차량1
car_company_1 = "Ferrari"
car_detail_1 = [{"color": "White"}, {"horse": 400}, {"price": 8000}]

# 차량2
car_company_2 = "Bmw"
car_detail_2 = [{"color": "Black"}, {"horse": 270}, {"price": 5000}]

# 차량3
car_company_3 = "Forshe"
car_detail_3 = [{"color": "Red"}, {"horse": 330}, {"price": 6000}]

# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ["Ferrari", "Bmw", "Audi"]
car_detail_list = [
    {"color": "White", "horse": 400, "price": 8000},
    {"color": "Black", "horse": 270, "price": 5000},
    {"color": "Red", "horse": 330, "price": 6000},
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()
# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
    {
        "cat_company": "Ferrari",
        "car_detail": {"color": "White", "horse": 400, "price": 8000},
    },
    {
        "cat_company": "Bmw",
        "car_detail": {"color": "Black", "horse": 270, "price": 5000},
    },
    {
        "cat_company": "Forshe",
        "car_detail": {"color": "Red", "horse": 330, "price": 6000},
    },
]

print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용


class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 비공식적인 즉 print문으로 문자열을 출력하는 사용자 입장의 출력을 원할 때는 str 메서드 사용
    def __str__(self):
        return f"str : {self._company} - {self._details}"

    # 객체, 이 자료형의 타입에 따른 객체를 그대로 표시해줄 때 사용
    def __repr__(self):
        return f"repr : {self._company} - {self._details}"


car1 = Car("Ferrari", {"color": "White", "horse": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horse": 250, "price": 5000})
car3 = Car("Forshe", {"color": "Red", "horse": 330, "price": 6000})


print(car1)
print(car2)
print(car3)

# 속성(attribute)를 직접 조회 가능
# 클래스 안에 뭐가 들었지? 할 때 사용하면 좋음
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 사용 가능한 메타 정보 보여줌
print(dir(car1))

print()
print()

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    # print(repr(x)) #명시적 호출
    print(x)
