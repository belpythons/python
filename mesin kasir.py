import json
import os

data_file = 'data_barang.json'

stop = False

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

def add_barang(nama_barang, harga):
    data = load_data() 
    data[nama_barang] = harga
    save_data(data)
    print(f"Barang '{nama_barang}' dengan harga {harga} berhasil ditambahkan!")

def show_barang():
    data = load_data()
    if not data:
        print("Belum ada barang yang terdaftar.")
    else:
        print("Daftar barang dan harga:")
        for barang, harga in data.items():
            print(f"- {barang}: {harga}")

def hitung_harga():
    data = load_data()
    total_harga = 0
    while True:
        masukan = input("Masukan nama barang: ")
        if masukan in data:
            jumlah = int(input("Masukan jumlah barang: "))
            total_harga += data[masukan] * jumlah
        else:
            print("Barang tidak ditemukan.")
        lagi = input("Masukan barang lagi? [y/n]: ")
        if lagi.lower() == 'n':
            break
    print(f"Total harga: {total_harga}")
    uang = int(input("Masukan Jumlah uang"))
    if uang < total_harga:
        print(f"Maaf uang anda kurang, tidak bisa melanjutkan pembayaran")
    elif uang >= total_harga:
        kembalian = uang - total_harga
        print(kembalian)


if __name__ == "__main__":
    while True:
        print("\nPilih opsi:")
        print("1. Tambah barang")
        print("2. Lihat daftar barang")
        print("3. Hitung Harga")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            nama_barang = input("Masukkan nama barang: ")
            harga = input("Masukkan harga barang: ")
            try:
                harga = int(harga) 
                add_barang(nama_barang, harga)
            except ValueError:
                print("Harga harus berupa angka.")
        elif pilihan == '2':
            show_barang()
        elif pilihan == '3':
            hitung_harga()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")