base = []

while True:
    for i in range(19):
        row = input().split()
        base.append(row)
    if len(base) == 19:
        break

a = int(input())

for i in range(a):
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    for j in range(19):
        if base[x-1][j] == '0':
            base[x-1][j] = '1'
        elif base[x-1][j] == '1':
            base[x-1][j] = '0'
        if base[j][y-1] == '0':
             base[j][y-1] = '1'
        elif base[j][y-1] == '1':
            base[j][y-1] = '0'

for i in range(19):
    for j in range(19):
        print(base[i][j], end = " ")
    print()
