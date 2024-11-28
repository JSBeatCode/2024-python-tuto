# 내장 함수의 인자로 넘겨주는 문자열 타입의 이름이 객체에 존재하면 True이고 그렇지 않으면 False입니다.

class Car:
    def __init__(self):
        self.wheels = 4
        
    def drive(self):
        print("drive")
        
mycar = Car()

print(hasattr(mycar, "wheels"))
print(hasattr(mycar, "drive"))

# mycar 객체에 'wheels'는 변수이고 'drive'는 메소드입니다. 따라서 둘 다 True 입니다.

getattr(mycar, "wheels")

# drive라는 메소드나 객채가 있으면 가져온다.
method = getattr(mycar, "drive")
method()