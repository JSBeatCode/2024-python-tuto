# 함수 호출시 args라는 변수는 여러 개의 입력에 대해 튜플로 저장한 후 이 튜플 객체를 바인딩합니다.
def foo(*args):
    print(args)
    
foo(1,2,3)

foo(1,2,3,4)

print("-------------------------------------------")

# kwargs라는 변수가 딕셔너리 객체를 바인딩함을 알 수 있습니다. 
def foo1(**kwargs):
    print(kwargs)
    
foo1(a=1, b=2, c=3)

print("-------------------------------------------")

def len(*args, **kwrgs):
    """ Return the number of items in a container. """
    pass

def foo3(*args, **kwrgs):
    print(args)
    print(kwrgs)


foo3(1,2,3,a=1, b=2, c=3)

print("-------------------------------------------")
# 보통 데이터는 리스트나 튜플과 같은 자료구조에 저장됩니다. 자료구조에 저장된 데이터를 함수 호출부에 전달하기 위해서 다음과 같이 인덱싱을 수행한 후 각각 전달할 수 있습니다.
def foo4(a,b,c):
    print(a,b,c)
    print(a)
    print(b)
    print(c)
    
data=[1,2,3]
foo(data[0],data[1],data[2])

print("----------")

def foo5(a):
    print(a)
    
data1=[1,2,3]
print(data1)
foo5(data1)

print("----------")

def foo6(a,b,c):
    print(a,b,c)
    print(a)
    print(b)
    print(c)
    
data3=[1,2,3]
foo6(*data)

print("-------------------------------------------")
def foo7(**kwargs):
    print(kwargs)
    
foo7(a=1, b=2)

params = {'c':3,'d':4}
foo7(**params)