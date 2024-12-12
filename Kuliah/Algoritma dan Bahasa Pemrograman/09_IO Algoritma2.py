a1 = float(input('masukan panjang X1: '))
b1 = float(input('masukan tinggi Y1: '))
c1 = (a1**2) - (b1**2)

a2 = float(input('masukan panjang Y2: '))
b2 = float(input('masukan tinggi X2: '))
c2 = (a2**2) - (b2**2)

a3 = c1
c3 = c2
b3 = (c3**2) - (a3**2)

print (b3)