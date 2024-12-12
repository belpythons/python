def cek_positif(angka):
    if angka > 0:
        return "Angka positif"
    print("Ini tidak akan dicetak jika angka positif.")

print(cek_positif(5))  # Output: Angka positif

def cek_kelipatan_lima(angka):
    if angka % 5 == 0:
        return True  # Mengembalikan True jika angka adalah kelipatan 5
    return False  # Mengembalikan False jika bukan kelipatan 5

hasil = cek_kelipatan_lima(10)  # Akan mengembalikan True
print(hasil)  # Output: True

hasil = cek_kelipatan_lima(7)  # Akan mengembalikan False
print(hasil)  # Output: False

def penjumlahan(a, b):
    # Fungsi ini akan mengembalikan hasil penjumlahan
    return a + b

hasil = penjumlahan(3, 4)
print(f"Hasil penjumlahan 3 + 4 adalah: {hasil}")

# Fungsi untuk menambahkan dua angka
def tambah(a, b):
    return a + b

# Fungsi untuk mengurangi dua angka
def kurang(a, b):
    return a - b

# Fungsi untuk mengalikan dua angka
def kali(a, b):
    return a * b

# Fungsi untuk membagi dua angka
def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol"
    return a / b

# Fungsi utama untuk menjalankan kalkulator
def kalkulator():
    print("=== Kalkulator Sederhana ===")
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        hasil = tambah(a, b)
        print(f"Hasil dari {a} + {b} adalah: {hasil}")
    elif pilihan == '2':
        hasil = kurang(a, b)
        print(f"Hasil dari {a} - {b} adalah: {hasil}")
    elif pilihan == '3':
        hasil = kali(a, b)
        print(f"Hasil dari {a} * {b} adalah: {hasil}")
    elif pilihan == '4':
        hasil = bagi(a, b)
        print(f"Hasil dari {a} / {b} adalah: {hasil}")
    else:
        print("Pilihan tidak valid")

# Menjalankan kalkulator
kalkulator()
