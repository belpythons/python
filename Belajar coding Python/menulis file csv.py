import csv

# Data yang akan ditulis ke file CSV
data = [
    ["Nama", "Umur", "Kota"],
    ["Hanif", "19", "Yogyakarta"],
    ["Ahmad", "20", "Jakarta"]
]

# Membuka file CSV untuk menulis data
with open('coba csv.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    # Menulis setiap baris dari data ke dalam file CSV
    csv_writer.writerows(data) #digunakan untuk menulis beberapa baris sekaligus dari list
