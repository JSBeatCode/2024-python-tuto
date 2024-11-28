# 특별한 이름(__init__)을 갖기만 하면 객체가 생성될 때 자동으로 호출되는 함수가 있는 이를 생성자라고 합니다.
class Person:
    def __init__(self):
        print('start')
        

p = Person()

# 클래스로부터 생성된 인스턴스의 개수를 세어보겠습니다.
class MyClass:
    count = 0
    
    def __init__(self):
        MyClass.count += 1
        
    def getCount(self):
        return MyClass.count
    
a = MyClass()
b = MyClass()
c = MyClass()

print(MyClass.count)
print(a.count)
print(b.count)
print(c.count)

# __로 시작해서 __로 끝나는 메소드들이 있는데 이를 매직 메소드 또는 특별 메소드(special method)라고 부릅니다.
print('-------------------------------------')

class Car:
    def __init__(self):
        print("build completed")
        
class Stock:
    # 생성자 메서드: Stock 객체를 생성할 때 호출되며, 'value' 속성을 초기화합니다.
    def __init__(self, value):
        self.value = value

    # __add__ 메서드: '+' 연산자가 사용될 때 호출됩니다.
    # 두 Stock 객체의 value 속성을 더한 새로운 Stock 객체를 반환합니다.
    def __add__(self, other):
        # 'other'가 Stock 클래스의 인스턴스인지 확인합니다.
        if isinstance(other, Stock):
            # 두 객체의 value 속성을 더한 결과로 새로운 Stock 객체를 반환합니다.
            return Stock(self.value + other.value)
        # 'other'가 Stock 인스턴스가 아닌 경우, 연산을 지원하지 않음을 명시합니다.
        return NotImplemented

    # __repr__ 메서드: 객체를 출력할 때 또는 repr() 함수가 호출될 때 반환할 문자열을 정의합니다.
    # 여기서는 객체의 value 속성을 보기 쉽게 출력하도록 설정합니다.
    def __repr__(self):
        return f"Stock(value={self.value})"

# Stock 클래스의 객체 a와 b를 생성합니다.
a = Stock(100)  # value 속성이 100인 Stock 객체 생성
b = Stock(200)  # value 속성이 200인 Stock 객체 생성

# 두 Stock 객체를 더한 결과를 c에 저장합니다.
c = a + b  # a와 b의 value 속성을 더한 새로운 Stock 객체가 생성됩니다.

# c 객체를 출력합니다. __repr__ 메서드에 의해 보기 좋은 형태로 출력됩니다.
print(c)  # 출력: Stock(value=300)

print('---------------------------------------------')
# 우리는 ( )를 함수 호출할 때 사용한다고 생각했지만 사실은 클래스 내에 정의된 __call__ 메소드를 호출하는 방법입니다.
class MyFunc:
    def __call__(self, *args, **kwds):
        print('called!')
        
f = MyFunc()
f()

def func():
    print("hello")

func()

print('---------------------------------------------')
# 점(.)을 찍으면 클래스의 __getattribute__ 라는 이름의 매직 메소드를 호출해줍니다.
# . s.data라고 코딩하면 매직 메소드인 __getattribute__가 자동으로 호출되고 data라는 이름 item이라는 파라미터로 전달됨을 확인할 수 있습니다.

class Stock1:
    def __getattribute__(self, name):
        print(name, "accessed")
        
s = Stock1()
s.data

print('---------------------------------------------')
# Now f, g and h are all attributes of class C that refer to function objects, and consequently they are all methods of instances of C

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    
    def g(self):
        return 'hello world'
    
    h = g

print('-------------------------------')
# 부모 클래스 정의
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}이(가) 소리를 냅니다."

# 자식 클래스 정의 (부모 클래스 Animal을 상속받음)
class Dog(Animal):
    def speak(self):
        return f"{self.name}이(가) 멍멍 짖습니다."

# 자식 클래스 정의 (부모 클래스 Animal을 상속받음)
class Cat(Animal):
    def speak(self):
        return f"{self.name}이(가) 야옹 소리를 냅니다."

# 객체 생성 및 메서드 호출
dog = Dog("바둑이")
cat = Cat("나비")

print(dog.speak())  # 출력: 바둑이가 멍멍 짖습니다.
print(cat.speak())  # 출력: 나비가 야옹 소리를 냅니다.

