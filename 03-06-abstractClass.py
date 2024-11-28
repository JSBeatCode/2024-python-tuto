# 부모 클래스에 메서드만을 정의하고 이를 상속 받은 클래스가 해당 메서드를 반드시 구현하도록 강제하기 위해서 사용합니다.

from abc import ABC, abstractmethod

# 추상 클래스 정의: Animal
class Animal(ABC):
    # 추상 메서드: 모든 자식 클래스에서 반드시 구현해야 합니다.
    @abstractmethod
    def make_sound(self):
        pass  # 구현 없이 선언만 합니다.

# 추상 클래스를 상속받는 구체적인 클래스: Dog
class Dog(Animal):
    # 추상 메서드를 구현합니다.
    def make_sound(self):
        return "멍멍"

# 추상 클래스를 상속받는 구체적인 클래스: Cat
class Cat(Animal):
    # 추상 메서드를 구현합니다.
    def make_sound(self):
        return "야옹"

# 객체 생성 및 메서드 호출
dog = Dog()
cat = Cat()

# 각 동물의 소리를 출력합니다.
print(dog.make_sound())  # 출력: 멍멍
print(cat.make_sound())  # 출력: 야옹
