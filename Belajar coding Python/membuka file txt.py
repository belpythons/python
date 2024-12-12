import os
os.system("cls")

print("\n", 5*"=", "INI ADALAH PERCOBAAN FILE", 5*"=", "\n")

#ride = membaca semua isi file
#rideline = membaca perbaris
#ridelines = membaca semua baris secara list

with open("data.txt", "r") as file:
    membuka_file = file.read()
    print(membuka_file)


files = open("data.txt", mode = "r", encoding ="utf-8")
buka = files.read()
print (buka)


#=====percobaan lainya=====
# with open("data.txt", "r") as file:
#     buka_file = file.readable()
#     baca_file = file.read()
#     baca_file = file.readline()
#     if buka_file == True:
#         print ('File Bisa Dibuka')
#     else:
#         print('FILE TIDAK DAPAT DIBUKA')
# print(baca_file)
# file.close()

# file = open('data.txt', mode="r", encoding="utf-8")

# for i in file:
#     print (i)

# file.close()

# def membuka_file():
#     with open("data.txt", "r", encoding="utf-8") as buka:
#         mengeprint = buka.read()
#         print (mengeprint)

# with open("data.txt", "r") as file:
#     for baris in file:
#         print(baris)


# file = 'data.txt'
# with open (file, "r") as buka:
#     print (buka.read())

# try:
#     with open("data.txt", "r") as file:
#         for baris in file:
#             # Memisahkan data dalam CSV (contoh)
#             kolom = baris.split(",")
#             print(kolom)
# except FileNotFoundError:
#     print("File tidak ditemukan!")
# except Exception as e:
#     print("Terjadi kesalahan:", e)
    
# try:
#     with open("data.txt", "r", encoding="utf-8") as file:
#         for baris in file:
#             print(baris.strip())  # .strip() untuk menghapus newline di akhir baris
# except FileNotFoundError:
#     print("File tidak ditemukan!")
# except Exception as e:
#     print("Terjadi kesalahan:", e)


# with open('data.txt', 'r') as nyobo:
#     mbuka_file = nyobo.readline()
#     print (mbuka_file)