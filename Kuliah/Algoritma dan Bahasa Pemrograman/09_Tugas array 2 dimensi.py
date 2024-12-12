
from array import *

matriks = [
    [],[],[],[]
]
print("masukan matriks ")

masukan11 = int(input("data Array [0][0]: "))
masukan12 = int(input("data Array [0][1]: "))
masukan13 = int(input("data Array [0][2]: "))
masukan14 = int(input("data Array [0][3]: "))
masukan21 = int(input("data Array [1][0]: "))
masukan22 = int(input("data Array [1][1]: "))
masukan23 = int(input("data Array [1][2]: "))
masukan24 = int(input("data Array [1][3]: "))
masukan31 = int(input("data Array [2][0]: "))
masukan32 = int(input("data Array [2][1]: "))
masukan33 = int(input("data Array [2][2]: "))
masukan34 = int(input("data Array [2][3]: "))
masukan41 = int(input("data Array [3][0]: "))
masukan42 = int(input("data Array [3][1]: "))
masukan43 = int(input("data Array [3][2]: "))
masukan44 = int(input("data Array [3][3]: "))

matriks.insert(0,[masukan11, masukan12, masukan13, masukan14])
matriks.insert(1,[masukan21, masukan22, masukan23, masukan24])
matriks.insert(2,[masukan31, masukan32, masukan33, masukan34])
matriks.insert(3,[masukan41, masukan42, masukan43, masukan44])

print("\n", "="*20)
print("Hasil")
for i in matriks:
    for j in i:
        print(j, end =" ")
    print()