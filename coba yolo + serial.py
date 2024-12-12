from ultralytics import YOLO
import cv2
import math
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

# Fungsi untuk mengirim data via serial
def kirim_serial(data):
    if ser.is_open:
        ser.write((data + "\n").encode())  # Mengirim data dengan newline
        print(f"Data yang dikirim: {data}")
    else:
        print("Port serial tidak terbuka.")

# Mulai webcam
cap = cv2.VideoCapture(0)
cap.set(3, 540)
cap.set(4, 380)

# Load model YOLO
model = YOLO("yolo-Weights/Hanif.pt")

# Object classes
classNames = ["Boncabe", "Powerbank"]

# Inisialisasi status sebelumnya
previous_status = ""

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # Variabel untuk mengecek keberadaan objek
    boncabe_detected = False
    powerbank_detected = False

    # Process coordinates and classes
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

            # Draw box on image
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # Class name
            cls = int(box.cls[0])
            class_name = classNames[cls]
            print("Class name -->", class_name)

            # Display object details on image
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img, class_name, org, font, fontScale, color, thickness)

            # Update detection status
            if class_name == "Boncabe":
                boncabe_detected = True
            elif class_name == "Powerbank":
                powerbank_detected = True

    # Tentukan status saat ini berdasarkan deteksi objek
    if boncabe_detected and powerbank_detected:
        current_status = "11"  # Kedua LED menyala
    elif boncabe_detected:
        current_status = "10"  # LED 1 (Boncabe) menyala
    elif powerbank_detected:
        current_status = "01"  # LED 2 (Powerbank) menyala
    else:
        current_status = "00"  # Tidak ada LED yang menyala

    # Hanya kirim data jika status berubah dari sebelumnya
    if current_status != previous_status:
        kirim_serial(current_status)
        previous_status = current_status

    # Tampilkan video dengan deteksi bounding box
    img = cv2.flip(img, 1)
    cv2.imshow('Webcam', img)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) == ord('q'):
        break

# Bersihkan resources
cap.release()
cv2.destroyAllWindows()
ser.close()
