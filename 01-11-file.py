fs1 = open('workfile.txt', 'w', encoding="utf-8")
fs2 = open('workfile2.txt', 'w', encoding="utf-8")

fs1.close()
fs1.closed
fs2.close()
fs2.closed

with open('workfile.txt', encoding="utf-8") as f1:
    read_data = f1.read()
    print(read_data)
    # read_data1 = f1.readline()
    # read_data2 = f1.readline() 
    # read_data3 = f1.readline() 
    # print('1:', read_data1)
    # print('2:', read_data2)
    # print('3:', read_data3)
    f1.closed
    f1.close()

f1.close()
f1.closed

f = open('workfile.txt', 'w', encoding="utf-8")
f.write('this is test\ntest\nhaha')


value = ('this answer', 343)
s = str(value)
f.write(s)

f.close()
f.closed

# json
import json
x = [1, 'simple', 'list']
res = json.dumps(x)
print(res)

f2 = open('workfile2.txt', 'r+', encoding="utf-8")
f2.write(json.dumps(x))
f2.read()

f2.close()
f2.closed