def reverse(data):
    # 데이터의 인덱스를 역순으로 반복하기 위한 루프입니다.
    # range(len(data) - 1, -1, -1): len(data) - 1에서 시작해 -1까지 (포함하지 않음) 1씩 감소합니다.
    for index in range(len(data) - 1, -1, -1):
        yield data[index]  # 현재 인덱스의 데이터를 반환합니다. 'yield'는 제너레이터를 생성합니다.

# 'golf' 문자열을 역순으로 반복하며 각 문자를 출력합니다.
for char in reverse('golf'):
    print(char)  # 'f', 'l', 'o', 'g' 순서로 출력됩니다.
    
    
print('---------------------------------------------')
a = sum(i*i for i in range(10))
print(a)

xvec = [10,20,30]
yvec = [7,5,3]
print(zip(xvec, yvec))

b = sum(x*y for x,y in zip(xvec, yvec))
print(b)

print('---------------------------------------------')
# 예제 데이터: page는 여러 줄의 텍스트가 포함된 리스트입니다.
page = [
    "This is the first line",
    "This is the second line",
    "And this is the third line"
]

# uniqueWords는 page의 각 줄을 순회하면서, 줄을 단어별로 분할(split)하고,
# 모든 단어를 집합(set)으로 모아 중복을 제거한 결과를 저장합니다.
uniqueWords = set(word for line in page for word in line.split())

# uniqueWords 출력 (결과: 중복이 제거된 단어들의 집합)
print(uniqueWords)

print('---------------------------------------------')

# 졸업생 정보를 저장하는 클래스 정의
class Student:
    def __init__(self, name, gpa):
        self.name = name  # 학생의 이름
        self.gpa = gpa    # 학생의 GPA (평균 학점)

# 예제 데이터: graduates 리스트에 여러 Student 객체 추가
graduates = [
    Student("Alice", 3.9),
    Student("Bob", 3.7),
    Student("Charlie", 3.8)
]
# valedictorian 변수는 graduates 리스트에서 가장 높은 GPA를 가진 학생의 이름을 찾습니다.
# max() 함수를 사용하여 GPA를 기준으로 최고 점수를 가진 학생을 찾습니다.
# 각 학생에 대해 (student.gpa, student.name) 튜플을 생성하고, GPA가 가장 높은 튜플을 반환합니다.
valedictorian = max((student.gpa, student.name) for student in graduates)

# valedictorian 출력 (결과: (3.9, 'Alice'))
print(valedictorian)

print('---------------------------------------------')

data = 'golf'
c = list(data[i] for i in range(len(data)-1, -1, -1))
print(c)