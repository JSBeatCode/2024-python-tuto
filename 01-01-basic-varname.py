a = 3
# get variable id
id = id(a)
print(id)

# get reference count of objects: if a variable, 'a' binds object, '3' then it increases reference count
import sys
refCnt = sys.getrefcount(a)
print(refCnt)

b = 3
c = 3
refCnt1 = sys.getrefcount(3)
print(refCnt1)

# sys.refCount 1 at the first place
a = [0, 1, 2]
# sys.refCount 2 because it used throw the method sys.getrefcount 
refCnt2 = sys.getrefcount(a)
print(refCnt2)

# if its count goes down 0, python will remove its memory.
# that's how reference count and grabage collection work in python