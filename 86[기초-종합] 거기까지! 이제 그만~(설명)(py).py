a = int(input())
b = 0
sum = 0

while True:
    b += 1
    sum += b
    if sum >= a:
        print(sum)
        break
