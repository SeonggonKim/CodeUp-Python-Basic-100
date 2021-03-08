color = input().split()
r = int(color[0])
g = int(color[1])
b = int(color[2])

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
print(r*g*b)
