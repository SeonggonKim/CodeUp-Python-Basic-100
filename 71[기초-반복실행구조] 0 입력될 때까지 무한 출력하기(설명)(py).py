list = []
while True:
    a = int(input())
    list.append(a)
    if a == 0:
        list.pop()
        break
for i in list:
    print(i)
