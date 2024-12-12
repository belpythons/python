# Array 3 dimensi
lembar = int(input("Masukkan jumlah halaman: "))
kolom = int(input("Masukkan jumlah kolom: "))
baris = int(input("Masukkan jumlah baris: "))
print()

presensi = [[["" for k in range(kolom)] for j in range(baris)] for i in range(lembar)]
kelas = []

for x in range(lembar):
    presensi[x][0][0] = "Nama"
for x in range (lembar):
    kel = 0
    while kel == 0:
        print(x+1, end = ".")
        nama = input("Masukkan kelas: ").upper()
        if nama == "":
            print("Nama wajib diisi!")
        else:
            kel = 1
    kelas.append(nama)

for x in range(lembar):
    for y in range(kolom):
        if y == 0:
            pass
        else:
            a = str(y)
            presensi[x][0][y] = ("Pertemuan ke-" + a)

print()
print("Masukkan Nama Mahasiswa")

for x in range(lembar):
    print("Kelas", kelas[x], ":")
    for y in range(baris):
        if y == 0:
            pass
        else:
            print(y, end=".")
            char = 0
            while char == 0:
                nama = input("Masukkan nama mahasiswa: ")
                if len(nama) > 20:
                    print("Tidak lebih dari 20 karakter")
                else:
                    char = 1
            presensi[x][y][0] = nama
print()

for z in range(len(presensi)):
    print(kelas[z], ":")
    for x in range(len(presensi[z])):
        if presensi[z][x][0] == "":
            pass
        elif x > 0:
            print(presensi[z][x][0],":")
            for y in range(len(presensi[z][x])):
                if y > 0:
                    print("Pertemuan ke-", y, ":")
                    wh = 0
                    while wh == 0:
                        kehadiran = input("Hadir(h)/Sakit(s)/Alpha(a): ".lower())
                        if kehadiran == "hadir" or kehadiran == "h":
                            presensi[z][x][y] = "Hadir"
                            wh = 1
                        elif kehadiran == "sakit" or kehadiran == "s":
                            presensi[z][x][y] = "Sakit"
                            wh = 1
                        elif kehadiran == "alpha" or kehadiran == "a":
                            presensi[z][x][y] = "Alpha"
                            wh = 1
                        else:
                            print("INPUT SALAH!")
        else:
            pass

for z in range(len(presensi)):
    print(kelas[z], ":")
    for x in range(len(presensi[z])):
        for y in range(len(presensi[z][x])):
            if x == 0:
                if y == 0:
                    print('|{:^20s}'.format(presensi[z][x][y]), end="")
                else:
                    print('|{:<15s}'.format(presensi[z][x][y]), end="")
            else:
                if y == 0:
                    print('|{:<20s}'.format(presensi[z][x][y]), end="")
                else:
                    print('|{:^15s}'.format(presensi[z][x][y]), end="")
        print()
print()