# 결국 함수 객체가 메모리에 할당되어 있고 hello와 f라는 이름은 그 함수 객체를 가리키는 이름표일 뿐입니다.
def hello():
    print("hello")
    
print(id(hello))

f = hello;
f()

class Func:
    def __call__(self, *args, **kwds):
        print("호출됨")
        pass
    
f1 = Func()
f1()