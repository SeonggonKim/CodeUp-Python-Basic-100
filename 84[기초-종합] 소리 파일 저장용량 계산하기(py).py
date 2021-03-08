a = input().split()
h = int(a[0])
b = int(a[1])
c = int(a[2])
s = int(a[3])

print('%.1f'%(h*b*c*s/8/1024/1024), 'MB')
