
# 1. *args
# 설명: *args는 **위치 인자(positional arguments)**를 여러 개 받을 때 사용합니다.
# *args는 튜플 형태로 전달됩니다.
# 인자의 개수가 가변적일 때, 여러 개의 인자를 함수에 전달할 수 있습니다.
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1,2,3,4,5)

# 2. **kwargs
# 설명: **kwargs는 **키워드 인자(keyword arguments)**를 여러 개 받을 때 사용합니다.
# **kwargs는 딕셔너리 형태로 전달됩니다.
# 인자의 이름과 값을 함께 지정해 여러 개의 키워드 인자를 전달할 수 있습니다.
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_key_values(name="Alices", age=30, city="seoul")

