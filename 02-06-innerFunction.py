# inner function (내부 함수)
def outer():  
    # 외부 함수: 내부 함수(inner)를 정의하고 반환
    def inner():  
        # 내부 함수: "inner" 문자열을 출력
        print("inner")  
    return inner  # 내부 함수를 반환

# outer 함수를 호출하여 내부 함수(inner)를 반환받음
f = outer()  # inner 함수를 반환받아 변수 f에 저장
f()  # 내부 함수 호출 -> 출력: "inner"

print("--------------------------------------------------")

# 간단한 값 반환 함수
def outer1():  
    # 외부 함수: 내부적으로 변수를 정의하고 반환
    inner = 3  # 변수 inner에 숫자 3 저장
    return inner  # inner 변수 값을 반환

f1 = outer1()  # outer1 호출 -> 변수 inner 값(3)을 반환받음
print(f1)  # 출력: 3

print("--------------------------------------------------")

# 클로저를 이용한 변수 캡처 예제
def outer2():
    num = 4  # 외부 함수에서 정의된 변수
    def inner():
        # 내부 함수: 외부 함수의 변수 num을 출력
        print(num)  
    return inner  # 내부 함수를 반환

f2 = outer2()  # outer2 호출 -> inner 함수를 반환받음
f2()  # inner 함수 호출 -> num 값(4)을 출력

# inner 함수가 외부 함수의 변수 num을 클로저로 캡처한 것을 확인
print(f2.__closure__[0].cell_contents)  # 출력: 4 (캡처된 num 값)
print(f2.__closure__)  # 클로저 정보 출력
print(f2.__closure__[0])  # 클로저의 첫 번째 셀 객체 출력

# 클로저 관련 객체 타입 및 속성 정보 확인
print(type(f2.__closure__))  # 출력: <class 'tuple'> (클로저는 튜플 형태)
print(type(f2.__closure__[0]))  # 출력: <class 'cell'> (클로저 셀 객체)
print(dir(f2.__closure__[0]))  # 셀 객체의 사용 가능한 메서드와 속성 출력
print("--------------------------------------------------")

# 매개변수 값 변경을 보여주는 함수
def outer3(num):  
    # 외부 함수: 매개변수 num 출력 및 내부 변경
    print(num)  # 전달받은 num 값을 출력
    num = 5  # num 값을 5로 변경
    print(num)  # 변경된 num 값을 출력
    def inner():  
        # 내부 함수: 외부 함수의 num 값을 출력
        print(num)  
    return inner  # 내부 함수를 반환

f3 = outer3(6)  # outer3 호출, num 값으로 6 전달 -> 내부 함수(inner)를 반환
f3()  # inner 함수 호출 -> num 값(변경된 5)을 출력
