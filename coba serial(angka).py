import serial
import time

# Inisialisasi koneksi serial (pastikan COM3 benar, jika tidak, ubah sesuai port yang benar)
try:
    ser = serial.Serial('COM3', 9600, timeout=1)  # Sesuaikan 'COM3' jika perlu
    time.sleep(2)  # Tunggu koneksi serial stabil
    print("Koneksi serial berhasil.")
except serial.SerialException as e:
    print(f"Error membuka port: {e}")
    exit()

# Inisialisasi data yang akan dikirim
data = "00"

def kirim_serial(data):
    if ser.is_open:
        ser.write((data + "\n").encode())  # Mengirim data dengan newline
        print(f"Data yang dikirim: {data}")
    else:
        print("Port serial tidak terbuka.")

try:
    while True:
        # Kirim data setiap 1 detik
        kirim_serial(data)
        time.sleep(1)

        # Pilihan untuk mengubah data
        pilihan = input("Ubah data (00, 01, 10, 11) atau tekan Enter untuk lanjut: ").strip()
        if pilihan in ["00", "01", "10", "11"]:
            data = pilihan

except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    ser.close()  # Tutup koneksi serial saat program selesai
    print("Port serial ditutup.")
