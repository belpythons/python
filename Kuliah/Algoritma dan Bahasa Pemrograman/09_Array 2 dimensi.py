from array import *

mahasiswa = [
    [82, 75, 67, 95, 70], [70, 96, 85, 79, 75], 
    [86, 71, 80, 68, 93], [80, 73, 81, 94, 89],
    [57, 79, 86, 79, 80]
]
print("Before inserting the array elements: ")
for i in mahasiswa:
    print(i)
    for j in i:
        print(j, end=" ")
    print()

mahasiswa.insert(2, [90, 91, 92, 93, 94])
print("After inserting the array element")
for i in mahasiswa:
    for j in i:
        print(j, end =" ")
    print()
