class Car:
    def __init__(self, model):
        self.model = model
    
    def get_model(self):
        return self.model
    
c = Car("GV80")
print(c.get_model())

print("----------------------------------------------")

class Car:
    def __init__(self, model):
        self.model = model
    
    @property
    def get_model(self):
        return self.model
    
c = Car("GV80")
print(c.get_model)

print("----------------------------------------------")

def outer(out1):
    def inner(in1):
        print('inner function called')
        print('outer arguments: ', out1)
        print('inner arguments: ', in1)
    return inner

f = outer(1)
f(10)

print("----------------------------------------------")

def outer(out1):
    def inner(in1):
        print("inner function called")
        print("inner argument", in1)
        out1()
    return inner

def hello():
    print("hello")
    
f = outer(hello)
f(10)