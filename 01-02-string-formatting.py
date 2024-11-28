name = "minsu"
score = 90
print("%s 의 점수는 %d 점입니다. " % (name, score))

name = "minsu"
score = 90
print("{} 의 점수는 {} 점입니다. " .format(name, score))

name = "minsu"
score = 90
print(f"{name}'s score is {score}.")

# special characters
data = 3
print("{{ {} }}".format(data))
print(f"{{ {data} }}")
print(f"'/{data}'")

# fill numbers within variables at front
a = 3
mystr = f"{a:03d}"
print(mystr)

# fill blank within variables at back
symbol = "BTCUSDT"
print(f"{symbol:10}")

# real number 
# # mystr = "   3.14"
a = 3.141592
mystr = f"{a:6.2f}"
print(mystr)
mystr = f"{a:0.2f}"
print(mystr)
mystr = f"{a:0.3f}"
print(mystr)