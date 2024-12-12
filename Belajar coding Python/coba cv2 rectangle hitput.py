#COBA CV 2 RECTANGLE MENGOLAH GAMBAR HITAM DAN PUTIH

import cv2

cap = cv2.VideoCapture(0)



while True:
    _, frame= cap.read()
    frame = cv2.flip(frame, 1)

    x1 = 100         #untuk kotak rectangle (kotak warna biru)
    y1 = 150

    x2 = 200        #untuk ukuran kotak kamera / frame
    y2 = 300

    cv2.rectangle(frame, (x1,y1), (x2,y2), (255, 10, 10), 2) #ada penjelasan tata urutannya di deskripsi pop up
    
    roi = frame[y1:y2, x1:x2]

    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    _, roi = cv2.threshold(roi,  50, 255, cv2.THRESH_BINARY)


    cv2.imshow("Camera", frame)     #untuk memanggil kamera
    cv2.imshow("Kamera rectangle", roi)     #untuk memanggil kamera dengan ukuran kotak rectangle

    interrupted = cv2.waitKey(10)
    if interrupted & 0xFF == 27:  #esc untuk close
        break                   #jika menekan tombol esc akan keluar sendiri lama-lama
    if interrupted & 0xff == ord('s'):
        cv2.inwrite("saved.jpg", roi)

cap.release()
cv2.destroyAllWindows()