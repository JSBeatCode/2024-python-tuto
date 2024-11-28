class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
mybook = Book("title1", 21341)
print(mybook.title, mybook.price)
# 아래 오류
# print(mybook[0], mybook[1])

mybook2 = ("파이썬을 \/\/\자동매매", 12324)
print(mybook2[0], mybook2[1])
# 아래 오류
# print(mybook2.title, mybook2.price)

# namedtuple 함수를 통해서 title, price 속성을 갖는 Book 클래스를 간단히 생성할 수 있고 이를 통해 객체를 생성할 수 있습니다.
# namedtuple을 통해 생성한 객체는 결국 튜플처럼 immutable하기 때문에 클래스와 달리 값을 수정할 수 없습니다. 그리고 튜플처럼 정수 값을 통해서 인덱싱할 수 있습니다.
from collections import namedtuple;

Book = namedtuple('Book', ['title', 'price'])
mybook3 = Book("파이썬을 이용한 비트코인 자동매매", 27000)
print(mybook3.title, mybook3.price)

print(mybook3[0], mybook3[1])

# namedtuple 언패킹
def printBook(title, price):
    print(title, price)
    
printBook(*mybook3)