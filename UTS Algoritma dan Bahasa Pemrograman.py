import os
os.system("cls")
print('='*15, 'BUKU PERPUSTAKAAN', '='*15)

list_buku = []
while True:
    judul = input('masukan judul buku\t: ')
    penulis = input ('masukan penulis buku \t: ')

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)


    lanjut = input('Data sudah tersimpan \nApakah lanjut atau tidak? (y/n): ')

    if lanjut == 'n':
        break


print ('\n','='*15, 'DATA BUKU', '='*15)


max_len_judul = max(len(buku[0]) for buku in list_buku)

print (f"{'NO':<6} {'JUDUL':<{max_len_judul}} {'PENULIS':<6}")
for indek, buku in enumerate(list_buku):
    print (f'{indek+1:<6} {buku[0]:<{max_len_judul}} {buku[1]:<6} ')






