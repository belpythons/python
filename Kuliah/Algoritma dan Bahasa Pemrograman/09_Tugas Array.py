from array import *
import os

os.system ("cls")

print("\n","="*30,"\n", "TUGAS ALGORITMA DAN BAHASA PEMROGRAMAN","\n", "="*30, "\n")

Matriks = [
    [20, 50, 10],
    [40, 30, 10],
    [15, 13, 25],
    [18, 12, 30]
]

total_row1 = sum(Matriks[0])
print(f"Total Row 1: {total_row1}")
total_row2 = sum(Matriks[1])
print(f"Total Row 2: {total_row2}")
total_row3 = sum(Matriks[2])
print(f"Total Row 3: {total_row3}")
total_row4 = sum(Matriks[3])
print(f"Total Row 4: {total_row4}")


total_colom1 = sum(i[0] for i in Matriks)
print (f"Total Kolom 1: {total_colom1}")
total_colom2 = sum(i[1] for i in Matriks)
print (f"Total Kolom 2: {total_colom2}")
total_colom3 = sum(i[2] for i in Matriks)
print (f"Total Kolom 3: {total_colom3}")

# Matriks2 = [
#     [total_row1, total_row2, total_row3, total_row4],
#     [total_colom1, total_colom2, total_colom3] 
# ]

# for a in Matriks2:
#     for b in a:
#         print (b, end=" ")
#     print()