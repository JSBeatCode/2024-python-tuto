for element in [1,2,3]:
    print(element)
    
print('---------------------------------------')

for element in (1,2,3):
    print(element)
    
print('---------------------------------------')

for key in {'one': 1, 'two': 2}:
    print(key)
    
print('---------------------------------------')
    
for char in "고마워":
    print(char)

for line in open("workfile.txt"):
    print(line, end="")
    

print('---------------------------------------')

s = 'abc'
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

print('---------------------------------------')

# Reverse 클래스는 이터레이터(Iterator)를 구현하는 클래스입니다. 문자열이나 리스트 같은 시퀀스를 역순으로 반복할 수 있도록 설계되었습니다.
# __init__ 메서드는 data를 저장하고, index를 시퀀스의 길이로 설정합니다. 이는 역순으로 접근하기 위함입니다.
# __iter__ 메서드는 이터레이터 객체를 반환하는데, 이 메서드가 있어야 for 루프에서 이 객체를 사용할 수 있습니다.
# __next__ 메서드는 이터레이터의 다음 요소를 반환합니다. 모든 요소를 다 반환하면 StopIteration 예외를 발생시켜 반복을 종료합니다.
class Reverse:
    """시퀀스를 역순으로 반복(iterate)하기 위한 이터레이터 클래스입니다."""

    # 초기화 메서드: 객체 생성 시 호출됩니다.
    def __init__(self, data):
        self.data = data  # 반복할 시퀀스를 저장합니다.
        self.index = len(data)  # 시퀀스의 길이를 인덱스로 설정하여 마지막 요소부터 접근합니다.

    # __iter__ 메서드: 이터레이터 객체 자체를 반환합니다.
    # 이 메서드는 이터레이터 프로토콜을 준수하기 위해 필요합니다.
    def __iter__(self):
        return self  # 자기 자신을 반환합니다.

    # __next__ 메서드: 이터레이터의 다음 요소를 반환합니다.
    def __next__(self):
        if self.index == 0:  # 인덱스가 0이 되면 시퀀스의 모든 요소를 다 반복한 것이므로
            raise StopIteration  # StopIteration 예외를 발생시켜 반복을 종료합니다.
        self.index = self.index - 1  # 인덱스를 1 감소시킵니다.
        return self.data[self.index]  # 현재 인덱스에 해당하는 요소를 반환합니다.

# Reverse 클래스의 객체 생성
rev = Reverse('spam')  # 'spam' 문자열을 역순으로 반복할 이터레이터 객체 생성
iter(rev)  # iter() 함수로 이터레이터를 초기화합니다. (실제로는 필요하지 않지만 이터레이터 프로토콜에 포함)

# for 루프를 사용하여 이터레이터의 각 요소를 출력합니다.
for char in rev:
    print(char)  # 'm', 'a', 'p', 's' 순서로 출력됩니다.
