import cv2
import mediapipe as mp
import pyautogui
import math

# Inisialisasi Mediapipe Hand tracking
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

# Inisialisasi Video Capture (kamera)
cap = cv2.VideoCapture(0)

# Mendapatkan ukuran layar
screen_width, screen_height = pyautogui.size()

# Status klik sebelumnya untuk mencegah multiple-click
click_status = False

def calculate_distance(point1, point2):
    """Menghitung jarak Euclidean antara dua titik."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Membalik frame agar tidak mirroring
    frame = cv2.flip(frame, 1)

    # Konversi frame ke RGB (diperlukan untuk Mediapipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Mendeteksi tangan
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Menggambar landmark di tangan
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Mendapatkan koordinat ibu jari (landmark ke-4) dan telunjuk (landmark ke-8)
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Konversi koordinat landmark ke piksel layar
            thumb_x, thumb_y = int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0])
            index_x, index_y = int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0])

            # Tampilkan lingkaran pada titik ibu jari dan telunjuk
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 0, 255), -1)

            # Konversi koordinat jari ke ukuran layar untuk menggerakkan kursor
            screen_x = int(index_tip.x * screen_width)
            screen_y = int(index_tip.y * screen_height)

            # Menggerakkan kursor dengan telunjuk
            pyautogui.moveTo(screen_x, screen_y)

            # Menghitung jarak antara ujung ibu jari dan telunjuk
            distance = calculate_distance((thumb_x, thumb_y), (index_x, index_y))

            # Jika jaraknya kecil (misalnya < 20), lakukan klik kiri
            if distance < 20 and not click_status:
                pyautogui.click()
                click_status = True
            elif distance >= 20:
                click_status = False

    # Menampilkan frame
    cv2.imshow("Mouse Control with Hand", frame)

    # Keluar jika 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan kamera dan menutup jendela
cap.release()
cv2.destroyAllWindows()
