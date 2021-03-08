num = input().split()
a = int(num[0])
m = int(num[1])
d = int(num[2])
n = int(num[3])

if n == 1:
  print(a)
else:
  for i in range(2, n+1):
      a = a*m+d
      if i == n:
        print(a)
