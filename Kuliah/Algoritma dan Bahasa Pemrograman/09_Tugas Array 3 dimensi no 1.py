import os
os.system("cls")

lembar = int(input("masukkan jumlah kelas :"))
kolom = int(input("masukkan jumlah pertemuan :"))
baris = int(input("masukkan jumlah mahasiswa :"))
print()
nilai = [[[""for k in range(kolom)]for j in range(baris)]for i in range(lembar)]
kelas = []
for x in range(lembar):
     nilai[x][0][0] = "Nama"
for x in range(lembar):
    kel = 0
    while kel==0:
        print (x+1, end=".")
        nama = input("kelas :").upper()
        if nama =="":
            print("NAMA WAJIB DIISI")
        else:
            kel = 1
        kelas.append(nama)
for x in range(lembar):
    for y in range(kolom):
        if y == 0:
            pass
        else:
            a=str(y)
            nilai[x][0][y]=("nilai ke-" +a) 
print()
print("Nama Mahasiswa")
for x in range(lembar):
    print ("kelas", kelas[x],":")
    for y in range(baris):
        if y==0:
            pass
        else:
            print(y,end=".")
            char = 0
            while char==0:
                nama = input("nama mahasiswa :")
                if len (nama)>20:
                    print("tidak lebih dari 20 karakter")
                else:
                    char=1
            nilai[x][y][0]=nama
print()

for z in range(len(nilai)):
    print(kelas[z],":")
    for x in range(len(nilai[z])):
        if nilai[z][x][0]==" ":
            pass
        elif x > 0:
            print(nilai[z][x][0])
            for y in range(len(nilai[z][x])):
                if y>0:
                    print("Nilai ke-",y,":") 
                    angka = int(input("nilai:").lower())
                    if angka >= 86:
                        nilai[z][x][y] = "A"
                    elif angka >= 81:
                        nilai[z][x][y] = "A-"
                    elif angka >= 76:
                        nilai[z][x][y] = "B+"
                    elif angka >= 71:
                        nilai[z][x][y] = "B"
                    elif angka >= 66:
                       nilai[z][x][y] = "B-"
                    elif angka >= 66:
                        nilai[z][x][y] = "C+"
                    elif angka >= 56:
                        nilai[z][x][y] = "C"
                    elif angka >= 51:
                        nilai[z][x][y] = "C-"
                    elif angka >= 46:
                        nilai[z][x][y] = "D+"
                    elif angka >= 0:
                        nilai[z][x][y] = "D"
                    else:
                        print("INPUT SALAH")
                else:
                    pass
            print()
        else:
            pass
for z in range(len(nilai)):
    print(kelas[z],":")
    for x in range(len(nilai[z])):
        for y in range(len(nilai[z][x])):
            if x == 0:
                if y == 0:
                    print('|{:^20s}|'.format(nilai[z][x][y]),end="")
                else:
                    print('|{:^15s}|'.format(nilai[z][x][y]),end="")
            else:
                if y ==0:
                    print('|{:^20s}|'.format(nilai[z][x][y]),end="")
                else:
                    print('|{:^15s}|'.format(nilai[z][x][y]),end="")
        print()
    print()
print()





