def outer(num):
    def inner():
        print(num)
    return inner

f1 = outer(3)
f2 = outer(4)

f1()
f2()

class Outer:
    def __init__(self, num):
        print('debug1')
        self.num = num
    def __call__(self, *args, **kwds):
        print('debug2')
        print(self.num)
        
f3 = Outer(5)
f3()