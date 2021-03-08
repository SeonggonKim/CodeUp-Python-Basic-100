h, w = map(int, input().split())
n = int(input())

base = []
for i in range(h):
    base.append([])
    for j in range(w):
        base[i].append(0)

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            base[x-1][y-1+j] = 1
    elif d == 1:
        for k in range(l):
            base[x-1+k][y-1] = 1

for i in range(h):
    for j in range(w):
        print(base[i][j], end = ' ')
    print()
