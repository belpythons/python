# ===========DAFTAR BUKU PERPUSTAKAAN===========#

import os

os.system("cls")
perpustakaan = []

def tambah_buku(judul, penulis, tahun):
    buku = {
        'judul': judul,
        'penulis': penulis,
        'tahun': tahun
    }
    perpustakaan.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan ke perpustakaan!")

def lihat_buku():
    if len(perpustakaan) == 0:
        print("Belum ada buku di perpustakaan.")
    else:
        max_len_judul = max(len(buku['judul']) for buku in perpustakaan)
        max_len_penulis = max(len(buku['penulis']) for buku in perpustakaan)
        
        print(f"{'NO':<6} {'JUDUL':<{max_len_judul}} {'PENULIS':<{max_len_penulis}} {'TAHUN':<6}")
        print("=" * (6 + max_len_judul + max_len_penulis + 8))
        
        for indek, buku in enumerate(perpustakaan):
            print(f"{indek+1:<6} {buku['judul']:<{max_len_judul}} {buku['penulis']:<{max_len_penulis}} {buku['tahun']:<6}")

def cari_buku(judul):
    hasil_cari = [buku for buku in perpustakaan if judul.lower() in buku['judul'].lower()]
    if len(hasil_cari) > 0:
        max_len_judul = max(len(buku['judul']) for buku in hasil_cari)
        max_len_penulis = max(len(buku['penulis']) for buku in hasil_cari)

        print(f"{'NO':<6} {'JUDUL':<{max_len_judul}} {'PENULIS':<{max_len_penulis}} {'TAHUN':<6}")
        print("=" * (6 + max_len_judul + max_len_penulis + 8))

        for indek, buku in enumerate(hasil_cari):
            print(f"{indek+1:<6} {buku['judul']:<{max_len_judul}} {buku['penulis']:<{max_len_penulis}} {buku['tahun']:<6}")
    else:
        print(f"Tidak ditemukan buku dengan judul '{judul}'.")

def menu():
    while True:
        print("\n","="*15, "PERPUSTAKAAN HANIP","="*15, "\n")
        print("1. Tambah buku")
        print("2. Lihat semua buku")
        print("3. Cari buku berdasarkan judul")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            tahun = input("Masukkan tahun terbit: ")
            tambah_buku(judul, penulis, tahun)
        elif pilihan == '2':
            lihat_buku()
        elif pilihan == '3':
            judul = input("Masukkan judul buku yang ingin dicari: ")
            cari_buku(judul)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

menu()
