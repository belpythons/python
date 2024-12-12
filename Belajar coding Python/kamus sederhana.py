import csv

def baca_kamus(file_kamus):
    kamus = {}
    with open(file_kamus, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Melewati baris header
        for row in csv_reader:
            kata = row[0]
            terjemahan = row[1]
            kamus[kata] = terjemahan
    return kamus

def cari_terjemahan(kamus, kata):
    return kamus.get(kata.lower(), "Terjemahan tidak ditemukan")

def main():
    file_kamus = 'kamus.csv'  # Pastikan file ini ada
    kamus = baca_kamus(file_kamus)
    
    while True:
        kata = input("Masukkan kata yang ingin diterjemahkan (atau ketik 'keluar' untuk berhenti): ")
        if kata.lower() == 'keluar':
            break
        terjemahan = cari_terjemahan(kamus, kata)
        print(f"Terjemahan: {terjemahan}")

if __name__ == "__main__":
    main()
