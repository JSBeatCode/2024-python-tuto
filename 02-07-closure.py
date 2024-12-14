# 함수 외부에 정의된 값을 내부 함수에서 사용하는 클로저(closure) 예제
def outer(num):  
    # 외부 함수: 매개변수 num을 내부 함수에서 사용할 수 있도록 캡처합니다.
    def inner():  
        # 내부 함수: 외부 함수의 num 값을 출력
        print(num)  
    return inner  # 내부 함수를 반환하여 외부에서도 호출 가능하게 함

# outer 함수 호출 시 클로저 함수 inner를 생성하고 반환
f1 = outer(3)  # num 값이 3인 클로저 생성
f2 = outer(4)  # num 값이 4인 클로저 생성

# 클로저 호출: 각각의 num 값을 출력
f1()  # 출력: 3
f2()  # 출력: 4


# 클래스 기반 클로저와 함수 호출 모사 (__call__ 메서드 사용)
class Outer:
    def __init__(self, num):
        # 클래스 생성자: 객체 생성 시 매개변수 num을 저장
        print('debug1')  # 디버그 메시지
        self.num = num  # 인스턴스 변수에 num 값 저장

    def __call__(self, *args, **kwds):
        # __call__ 메서드: 객체를 함수처럼 호출할 때 실행됨
        print('debug2')  # 디버그 메시지
        print(self.num)  # 저장된 num 값을 출력

# Outer 클래스의 인스턴스 생성
f3 = Outer(5)  # 생성자 호출, debug1 출력
# f3 객체를 함수처럼 호출
f3()  # __call__ 메서드 실행, debug2 출력 후 num 값 5 출력
