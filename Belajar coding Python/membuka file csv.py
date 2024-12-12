import csv

# Membuka file CSV dan membaca isinya
with open('coba csv.csv', mode='r') as file:
    csv_reader = csv.reader(file) #membaca file CSV baris per baris.
    for row in csv_reader:
        print(row)  # Mencetak setiap baris dalam file CSV
        #row adalah list yang berisi elemen dari setiap kolom di baris tersebut.
