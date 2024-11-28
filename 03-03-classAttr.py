class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

car = Car("toyota", "calibri")
# hasattr를 사용하여 속성 존재 여부 확인
print(hasattr(car, "brand"))
print(hasattr(car, "year"))
# getattr를 사용하여 속성 값 가져오기
print(getattr(car, "brand"))
print(getattr(car, "model"))
# 출력: N/A (속성이 없을 때 기본값 반환)
print(getattr(car, "year", "N/A"))