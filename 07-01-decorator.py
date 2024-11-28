def hello():
    print("hello")
    
hello()
hello

print("----------------------------------------------")
def deco(fn):
    def deco_hello():
        print('*' * 20)
        fn()
        print('*' * 20)
    return deco_hello
        
deco_hello = deco(hello)
deco_hello()

print("----------------------------------------------")

@deco
def hello2():
    print("hello 2")
    
    
hello2()