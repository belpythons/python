import os


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
        print("Daftar buku di perpustakaan:")
        for i, buku in enumerate(perpustakaan, 1):
            print(f"{i}. Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun: {buku['tahun']}")


def cari_buku(judul):
    hasil_cari = [buku for buku in perpustakaan if judul.lower() in buku['judul'].lower()]
    if len(hasil_cari) > 0:
        print(f"Menemukan {len(hasil_cari)} buku:")
        for buku in hasil_cari:
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun: {buku['tahun']}")
    else:
        print(f"Tidak ditemukan buku dengan judul '{judul}'.")


def menu():
    while True:
        print("\n","="*20, "PERPUSTAKAAN","="*20)
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