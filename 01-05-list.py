even_num = []

for i in range(10):
    if i % 2 == 0:
        even_num.append(i)
        
print(even_num)


even_num1 = [i for i in range(10) if i % 2 == 0]

print(even_num1)

pow2_num = [i*i for i in range(10)]

print(pow2_num)