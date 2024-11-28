# 데코레이터는 파이썬에서 함수를 수정하거나 기능을 추가하기 위해 사용되는 함수입니다. 
# 데코레이터는 보통 다른 함수를 감싸는 형태로 구현되며, 코드의 재사용성을 높이고, 
# 특정 작업(예: 로깅, 성능 측정, 권한 검사 등)을 손쉽게 추가할 수 있게 해줍니다.
def inner():
    print("inner function is called1")
    
inner()

def deco(f):
    def wrapper():
        print('-' * 20)
        f()
        print('-' * 20)
    return wrapper

decorated_inner = deco(inner)

decorated_inner()


@deco
def inner():
    print('inner function called2')
    
inner()

print('----------------------------------------------')

# 데코레이터 함수 정의
def my_decorator(func):
    # 전달받은 함수를 감싸는 새로운 함수를 정의합니다.
    def wrapper():
        print("함수 실행 전 작업 수행")  # func 함수가 실행되기 전에 수행할 작업
        func()  # 전달된 함수를 실행합니다.
        print("함수 실행 후 작업 수행")  # func 함수가 실행된 후에 수행할 작업
    return wrapper  # 감싼 함수를 반환하여 데코레이터 기능을 적용합니다.

# 데코레이터를 사용하여 기존 함수를 감쌉니다.
# @my_decorator는 say_hello 함수를 my_decorator로 감싸겠다는 의미입니다.
@my_decorator
def say_hello():
    print("안녕하세요!")  # 원래 함수의 본래 동작

# 데코레이터가 적용된 함수 호출
say_hello()

print('----------------------------------------------')

# 데코레이터 함수 정의 (매개변수가 있는 경우)
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("함수 실행 전 작업 수행")  # func 함수가 실행되기 전에 수행할 작업
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)  # 전달된 함수 실행 및 결과 저장
        print("함수 실행 후 작업 수행")  # func 함수가 실행된 후에 수행할 작업
        return result  # 함수의 결과를 반환합니다.
    return wrapper  # 감싼 함수를 반환하여 데코레이터 기능을 적용합니다.

# 데코레이터를 사용하여 매개변수가 있는 함수를 감쌉니다.
@my_decorator
def add(a, b):
    return a + b  # 두 매개변수의 합을 반환합니다.

# 데코레이터가 적용된 함수 호출
result = add(5, 3)  # add 함수 실행
print("결과:", result)  # 결과: 8 출력
