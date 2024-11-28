# 파이썬에서 객체는 수정 가능한 타입도 있고 수정 불가능한 타입도 있습니다. 여기서 수정 불가능한 객체를 immutable 객체라고 부르고 수정 가능한 객체를 mutable 객체라고 부릅니다. 우리가 알고 있는 파이썬 기본 데이터 타입 중 정수, 실수, 문자열, 튜플이 대표적인 immutable 객체이고 리스트와 딕셔너리가 mutable 객체입니다.
a = "hello"
b = ["hello", "python"]

print(id(a))
print(id(b))

print(id(b[0]))

print("-----------------------------------------------")
# 1) 'python2'라는 문자열 객체가 메모리의 4399272816 번지에 할당되고 해당 객체를 a라는 변수가 바인딩합니다.
# 2) 'python3'라는 문자열 객체가 메모리의 4399272880 번지에 할당되고 해당 객체를 a라는 변수가 바인딩합니다. 
# 3) 'python2'라는 문자열 객체는 아무도 자신을 참조하지 않기 때문에 가비지 컬렉터에 의해 자동으로 메모리에서 소멸됩니다. 
a = "python2"
print(id(a))
a = "python3"
print(id(a))

print("-----------------------------------------------")
a = ["python2", "python3"]
print(id(a))

a.append("python4")
print(a)

print(id(a))

print(id(a[0]))

print(id(a[1]))

print(id(a[2]))
