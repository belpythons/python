
print('==========PROGRAM UNTUK MENAMPILKAN LIST============')
# Progam untuk menampilkan List
# Buat list untuk menampung nama-nama teman
my_friends = ["Anggun", "Dian", "Agung", "Adi", "Adam"]

# Tampilkan isi list my_friends dengan nomer indeks 3
print ("Isi my_friends indeks ke-3 adalah: {}".format(my_friends[3]))

# Tampilkan semua daftar teman
print ("Semua teman: ada {} orang".format(len(my_friends)))
for friend in my_friends:
    print (friend)

print('\n\n =========MENAMBAHKAN LIST==========')
# Dijumlah menggunakan + dan dikali menggunakan *

makan_pagi = [
    'Nasi', 'Tempe', 'Telur', 'Mie'  # Bisa diginiin tapi tetap sama saja
    ]
makan_siang = ['Nasi', 'sayur', 'ayam'] # Seperti ini juga tidak ada bedanya
makan_malam = ['mie ayam', 'es teh']

hari_ini = makan_pagi + makan_siang + makan_malam
print ('hari ini saya makan:', hari_ini)


print('\n\n ==========LIST MULTIDIMENSI=======')
minuman = [
    ["air putih", "susu", "es buah"],
    ["es jeruk", "es melon", "es teler"],
    ["es jagung", "es kuwut", "es lainya"]
]
for p in minuman:
    print(p)



print('\n\n==========PROGRAM MEMASUKAN DATA LIST========')
# Membuat List Kosong
Hobi = []
stop = False

# Menambah isi
while not stop:
    tambah_hobi = input("tambahkan hobimu: ")
    Hobi.append(tambah_hobi)

    tanya = input('apakah akan ditambahkan lagi? (y/n): ')
    if(tanya== 'n'):
        stop = True

print('kamu memiliki hobi sebanyak: {}'. format(len(Hobi)))
for apa_saja in Hobi:
    print('-{}'.format(apa_saja))









