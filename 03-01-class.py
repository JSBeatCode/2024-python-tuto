# 메모리에 두 개의 객체가 생성됩니다. 
class Person:
    pass

p = Person()

# 객체 이름 공간에 변수 생성
p.data=3

# 클래스 공간에 데이터 저장하기

class Person1:
    data = 4
    
p1 = Person1()

# 코드를 실행하면 당연히 각 객체에 balance(잔고)라는 이름으로 각각 1,000원과 100원이 저장됩니다
class Person2:
    pass

p2 = Person2()
p3 = Person2()
p2.balance = 10000
p3.balance = 100

