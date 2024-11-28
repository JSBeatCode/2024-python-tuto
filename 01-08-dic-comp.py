name = ['merona', 'gugucon']
price = [500, 1000]

icecream = {k:v for k, v in zip(name, price)}
print(icecream)

icecream2 = {k:v*2 for k, v in zip(name, price)}
print(icecream2)

name1 = ['merona', 'gugucon', 'dfes']
price1 = [500, 1000, 600]

icecream3 = {k:v for k, v in zip(name1, price1) if v < 1000}
print(icecream3)