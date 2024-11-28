# int 타입의 객체는 iterable하지 않음을 알 수 있습니다.
# a = 1
# print(iter(a))

# for i in a:
#     print(i)
    
    
a = [1,2,3]
print(iter(a))

for i in a:
    print(i)
    
print('------------------------------------------')

class MyIterator:
    def __init__(self):
        self.current = 0  # 값을 저장할 변수 초기화, 0부터 시작

    def __next__(self):
        self.current += 1  # current 값을 1씩 증가시킴
        return self.current  # 증가된 current 값을 반환

class MyIterable:
    def __iter__(self):
        return MyIterator()  # MyIterator 객체를 반환하여 반복 가능 객체로 설정

# MyIterable 클래스의 인스턴스 생성
m = MyIterable()
r = iter(m)  # iter()를 사용하여 MyIterable 객체에서 이터레이터 생성

# next() 함수를 호출할 때마다 __next__ 메서드가 실행되어 값이 순차적으로 증가
print(next(r))  # 출력: 1 (self.current가 1로 증가)
print(next(r))  # 출력: 2 (self.current가 2로 증가)
print(next(r))  # 출력: 3 (self.current가 3로 증가)


print('------------------------------------------')

# 파이썬에서 언더바 두 개(__init__, __iter__, __next__ 등)로 묶인 메서드는 
# 매직 메서드(Magic Method) 또는 특수 메서드(Dunder Method, Double Underscore Method)라고 불립니다. 
# 이 메서드들은 파이썬의 내부 동작과 관련된 특별한 기능을 수행하며, 
# 일반적으로 사용자가 직접 호출하는 것이 아니라 특정 상황에서 자동으로
# 호출됩니다.

class Season:
    def __init__(self):
        # __init__ 메서드:
        # 객체가 생성될 때 자동으로 호출됩니다.
        # season 리스트에는 '봄', '여름', '가을', '겨울'의 4개 계절이 저장됩니다.
        self.season = ['봄', '여름', '가을', '겨울']
        
        # count 변수는 반복이 진행될 때마다 현재 위치를 추적하는 역할을 합니다.
        # 초기값은 0으로 설정되며, 반복이 진행될 때마다 1씩 증가합니다.
        self.count = 0

    def __iter__(self):
        # __iter__ 메서드:
        # 이 메서드는 Season 객체가 반복 가능하도록 만들어주는 메서드입니다.
        # Season 객체 자체가 이터레이터 역할을 하도록 자기 자신을 반환합니다.
        # 이 메서드는 반드시 __next__ 메서드를 함께 정의해야 합니다.
        return self

    def __next__(self):
        # __next__ 메서드:
        # 이 메서드는 반복자가 호출될 때마다 하나씩 데이터를 반환하는 역할을 합니다.
        # count가 season 리스트의 길이보다 작을 때만 요소를 반환하며,
        # season 리스트의 길이를 초과하면 StopIteration 예외를 발생시켜 반복을 종료합니다.
        if self.count < len(self.season):
            # 현재 count 값에 해당하는 계절을 season 리스트에서 가져옵니다.
            rtVal = self.season[self.count]
            
            # count 값을 1 증가시켜 다음 값을 준비합니다.
            self.count += 1
            return rtVal  # 가져온 계절 값을 반환
        else:
            # 리스트의 모든 요소를 순회했을 때 StopIteration 예외를 발생시켜 반복을 종료합니다.
            raise StopIteration

# Season 클래스의 인스턴스를 생성합니다.
s = Season()

# s.season 리스트를 순회하면서 각 계절을 출력합니다.
for i in s.season:
    print(i)  # 출력: '봄', '여름', '가을', '겨울' 순으로 출력됩니다.

print('---------------------------------------')

# Season 객체를 이터레이터로 변환합니다.
ir = iter(s)

# next() 함수를 호출하여 이터레이터에서 각 계절을 순차적으로 가져와 출력합니다.
print(next(ir))  # 출력: '봄'
print(next(ir))  # 출력: '여름'
print(next(ir))  # 출력: '가을'
print(next(ir))  # 출력: '겨울'
