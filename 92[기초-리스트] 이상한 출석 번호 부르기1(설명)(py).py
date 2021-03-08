num = int(input())
a = input().split()
count = []

for i in range(num):
  a[i] = int(a[i])

for i in range(23):
  count.append(0)

for i in range(num):
  count[a[i]-1] += 1

for i in range(23):
  print(count[i], end = " ")
