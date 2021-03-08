a = int(input(), 16)
b = hex(a)[2].upper()

for i in range(1,16):
    c = hex(i)[2].upper()
    print(b,"*",c,"=",hex(int(b,16)*int(c,16))[2:4].upper(), sep='')
