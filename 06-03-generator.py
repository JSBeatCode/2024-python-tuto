# 제너레이터의 동작
# yield 사용: 제너레이터 함수는 yield 키워드를 만나면 값을 반환하고, 함수의 실행 상태를 "중단"합니다. 이후 next() 또는 for문에서 계속해서 호출되면 그 지점부터 실행을 이어나갑니다.
# 메모리 절약: 모든 값을 한 번에 메모리에 저장하는 대신, 제너레이터는 값을 필요할 때마다 하나씩 생성합니다. 그래서 대량의 데이터 처리에서 매우 효율적입니다.

# 실행 흐름
# generate_numbers(5)를 호출하면 제너레이터 객체가 반환됩니다.
# for문을 통해 제너레이터 객체가 순차적으로 실행됩니다. 첫 번째 호출에서 count = 1이 반환되고, 이후 yield를 만나면 함수는 중단됩니다.
# 다시 next()나 for문이 호출되면, 함수는 마지막 yield 이후부터 실행을 계속합니다. 이 과정이 반복되어 1부터 5까지의 숫자를 차례로 출력합니다.

# 제너레이터의 장점
# 메모리 효율적: 한 번에 모든 값을 메모리에 로드하지 않고 필요한 값만 생성합니다.
# 성능 향상: 큰 데이터셋을 다룰 때 성능 향상 효과가 있습니다.
# 무한 시퀀스 생성 가능: 제너레이터는 끝없이 값을 생성할 수 있기 때문에, 무한한 시퀀스도 처리할 수 있습니다.

# 제너레이터 함수 정의: 1부터 n까지의 숫자를 반환하는 제너레이터
def generate_numbers(n):
    count = 1  # 숫자를 셀 변수 count 초기화 (1부터 시작)
    
    # n보다 작거나 같을 때까지 반복
    while count <= n:
        yield count  # 현재 count 값을 반환하고 함수의 상태를 기억함
        count += 1  # count 값을 1씩 증가시킴
    
# 제너레이터 함수 호출
gen = generate_numbers(5)  # 1부터 5까지의 숫자를 생성하는 제너레이터 객체 생성

# 제너레이터에서 값을 하나씩 가져오기
# for 문을 통해 제너레이터에서 반환되는 값들을 순차적으로 처리
for num in gen:
    print(num)  # 1, 2, 3, 4, 5가 순차적으로 출력됨
print('-------------------------------')
# 무한히 숫자를 생성하는 제너레이터
def infinite_numbers():
    count = 0
    while True:
        yield count  # 0부터 시작해 계속 숫자를 생성
        count += 1

# 제너레이터 객체 생성
gen = infinite_numbers()

# 무한히 숫자를 생성하고 출력하는 예시 (10개까지만 출력)
for i in range(10):
    print(next(gen))  # 0부터 9까지 출력됨

print('-------------------------------')
# 값을 받아서 다시 값을 하나씩 처리합니다.
# 그때 그때 준비된 값을 리턴하고 다시 돌아와서 함수 내 코드를 실행하고 다시 준비되면 리턴할 수 있다면 좋을 것 같습니다.

# yield가 사용된 함수는 ( )를 붙여도 코드가 바로 실행되지 않습니다. 대신 제너레이터라는 객체가 생성되고 코드가 실행될 준비를 합니다.
def num_gen():
    for i in range(3):
        yield i
        
g = num_gen()

num1 = next(g)
num2 = next(g)
num3 = next(g)

print(num1, num2, num3)

print('-------------------------------')
# 빵 100개를 담은 파이썬 리스트가 리턴되는데 이 값은 모두 메모리에 로드됩니다.
def createBread(n):
    tray = []
    for i in range(n):
        bread = "bread" + str(i)
        tray.append(bread)
    return tray

def packBread(bread):
    print("{} package completed".format(bread))
    
for i in createBread(5):
    packBread(i)
    
print('-------------------------------')
# 제너레이터 함수를 사용
def createBread1(n):
    for i in range(n):
        bread = "bread" + str(i)
        yield bread
    

def packBread1(bread):
    print("{} package completed".format(bread))
    
for i in createBread1(5):
    packBread1(i)

print('-------------------------------')
