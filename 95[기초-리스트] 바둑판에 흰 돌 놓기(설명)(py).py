num = int(input())

a=[]
for i in range(19):
  a.append([])
  for j in range(19):
    a[i].append(0)

X = []
Y = []
for i in range(num):
  x, y = input().split()
  x = int(x)
  y = int(y)
  X.append(x)
  Y.append(y)

for i in range(num):
  a[X[i]-1][Y[i]-1] = 1

for i in range(19):
  for j in range(19): 
    print(a[i][j], end=' ')
  print()
