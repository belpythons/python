import serial
import time
import keyboard  # Library untuk menangani input keyboard

# Inisialisasi koneksi serial (pastikan COM3 benar, jika tidak, ubah sesuai port yang benar)
try:
    ser = serial.Serial('COM3', 9600, timeout=1)  # Sesuaikan 'COM3' jika perlu
    time.sleep(2)  # Tunggu koneksi serial stabil
    print("Koneksi serial berhasil.")
except serial.SerialException as e:
    print(f"Error membuka port: {e}")
    exit()

# Fungsi untuk mengirim data via serial
def kirim_serial(data):
    if ser.is_open:
        ser.write((data + "\n").encode())  # Mengirim data dengan newline
        print(f"Data yang dikirim: {data}")
    else:
        print("Port serial tidak terbuka.")

try:
    print("Gunakan tombol panah untuk mengontrol LED:")
    print("Panah Kiri: Kedua LED mati (00)")
    print("Panah Atas: LED 1 hidup (10)")
    print("Panah Bawah: LED 2 hidup (01)")
    print("Panah Kanan: Kedua LED hidup (11)")

    while True:
        # Cek apakah tombol panah ditekan
        if keyboard.is_pressed('up'):
            kirim_serial("10")  # LED 1 hidup, LED 2 mati
            time.sleep(0.3)  # Jeda agar tidak mengirim terlalu cepat
        elif keyboard.is_pressed('down'):
            kirim_serial("01")  # LED 2 hidup, LED 1 mati
            time.sleep(0.3)
        elif keyboard.is_pressed('left'):
            kirim_serial("00")  # Kedua LED mati
            time.sleep(0.3)
        elif keyboard.is_pressed('right'):
            kirim_serial("11")  # Kedua LED hidup
            time.sleep(0.3)

except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    ser.close()  # Tutup koneksi serial saat program selesai
    print("Port serial ditutup.")
