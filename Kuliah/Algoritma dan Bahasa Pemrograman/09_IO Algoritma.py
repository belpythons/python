import math
import cmath

a = float (input('masukan nilai a: '))
b = float (input('masukan nilai b: '))
c = float (input('masukan nilai c: '))

D = b ** 2
b = b * -1
p = 4 * a * c

R = D - p
if R >= 0:
    R = math.sqrt(R)
else :
    R = cmath.sqrt(R)

Q = 2 * a
S = (b + R)
T = (b - R)

X1 = S/Q
X2 = T/Q

print('Nilai X1: ', X1)
print('Nilai X2: ', X2)