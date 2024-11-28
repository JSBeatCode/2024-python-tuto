# inner function

def outer():
    def inner():
        print("inner")
    return inner


f = outer()
f()

print("--------------------------------------------------")

def outer1():
    inner = 3
    return inner

f1 = outer1()
print(f1)


print("--------------------------------------------------")

def outer2():
    num = 4
    def inner():
        print(num)
    return inner

f2 = outer2()
f2()

# to show the variables from inner def
print(f2.__closure__[0].cell_contents)
print(f2.__closure__)
print(f2.__closure__[0])

print(type(f2.__closure__))
print(type(f2.__closure__[0]))
print(dir(f2.__closure__[0]))
print("--------------------------------------------------")

# param value has changed in the calling function 
def outer3(num):
    print(num)
    num = 5
    print(num)
    def inner():
        print(num)
    return inner

f3 = outer3(6)
f3()