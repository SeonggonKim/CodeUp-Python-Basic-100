ant = []
x = 1
y = 1

for i in range(10):
    a = input().split()
    ant.append(a)


while True:
    if ant[x][y] == '2':
        ant[x][y] = '9'
        break
    elif ant[x+1][y] == '1' and ant[x][y+1] == '1':
        ant[x][y] = '9'
        break
    ant[x][y] = '9'
    if ant[x][y+1] == '1':
        x += 1
    elif ant[x+1][y] == '1':
        y += 1
    else:
        y += 1

for i in range(10):
    for j in range(10):
        print(ant[i][j], end = ' ')
    print()
