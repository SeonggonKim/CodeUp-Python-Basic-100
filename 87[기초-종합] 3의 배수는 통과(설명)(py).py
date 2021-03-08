a = int(input())
b = 0

while True:
    b += 1
    if b>a:
        break
    if b%3 != 0:
        print(b, end= " ")
