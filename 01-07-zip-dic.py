# []: list = java array랑 같음
# {}: dic = object랑 비슷함
# (): tuple = Array랑 비슷함. parameter으로 던지거나 return 받을 수 있음
# zip의 역할은 여러개의 array를 index에 따라 그룹화 시켜서 object 형식의 list로 만듬
name = ['merona', 'gugucon', 'werd']
price = [500, 1000]
tag = ['df', 'ad', 'de']

z = zip(name, price, tag)
print(z)
print(list(z))

for n, p, o in zip(name, price, tag):
    print(n, p, o)
    
iceCream1 = {"메로나": 500, "구구콘": 1000}

iceCream2 = dict(메로나=500, 구구콘=1000)

print(iceCream1)
print(iceCream2)

iceCream3 = dict([("메로나", 500), ("구구콘", 1000)])

print(iceCream3)

data = {}

# key로 'a'를 추가학 value 0을 설정함, setdefault는 현재 value 값을 리턴
ret = data.setdefault('a', 0)
print(ret, data)
print(ret)
print(data)

# 이미 key가 있는 경우 setdefault 현재 value 값을 리턴
ret = data.setdefault('a', 1)
print(ret)
print(data)

data1 = ["BTC", "BTC", "XRP", "ETH", "ETH", "ETH"]

# set으로 중복 데이터 줄여주고 data1의 데이터는 그대로 보존
# 그대로 보존된 data1에 count 함수를 통해 해당 파라미터가 몇개가 있는지 확인 후 출력
for k in set(data1):
    count = data1.count(k)
    print(k, count)