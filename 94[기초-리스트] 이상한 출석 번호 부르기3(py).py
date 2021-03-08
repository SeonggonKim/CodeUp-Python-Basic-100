num = int(input())
a = input().split()

for i in range(num):
  a[i] = int(a[i])

print(min(a))
