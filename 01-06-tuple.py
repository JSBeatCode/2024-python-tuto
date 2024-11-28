a = 1, 2
b = (1, 2)

print(a, type(a))
print(b, type(b))

data = (1, 2, 3)
n1, n2, n3 = data
print(n1, n2, n3)

data1 = (1, 2, 3)
n11 = data1[0]
n21 = data1[1]
n31 = data1[2]
print(n11, n21, n31)

scores = (1, 2, 3, 4, 5, 6)
low, *others, high = scores
print(others)
print(low)
print(high)

def foo():
    return 1, 2, 3

val = foo()
print(val)
print(type(val))

def hap(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

scores = (1, 2, 3, 4)
result = hap(*scores)
print(result)

# result1 = hap(scores)
# print(result1)