import cv2
import mediapipe as mp
import numpy as np
import time

# Inisialisasi Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Setup Mediapipe Hand Detection
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Inisialisasi kamera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Tidak dapat membuka kamera.")
    exit()

# Variabel untuk posisi bola
ball_pos = [320, 240]
ball_radius = 20
ball_color = (0, 255, 0)
screen_size = (640, 480)
is_ball_caught = False
ball_speed = [0, 0]  # Kecepatan bola saat dilempar
gravity = 0.5  # Gaya gravitasi saat bola jatuh
ball_throw_time = None  # Untuk menghitung waktu setelah bola dilempar

# Fungsi untuk memetakan nilai koordinat tangan ke layar
def map_hand_to_screen(x, y, screen_size):
    return int(x * screen_size[0]), int(y * screen_size[1])

# Fungsi untuk mendeteksi apakah tangan mengepal (fist) atau terbuka (open palm)
def is_fist(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
    return all([
        thumb_tip.y > wrist.y,
        index_tip.y > wrist.y,
        middle_tip.y > wrist.y,
        ring_tip.y > wrist.y,
        pinky_tip.y > wrist.y
    ])

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal mengambil frame dari kamera.")
        break

    # Konversi ke RGB untuk diproses oleh Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Mirror gambar kamera
    frame = cv2.flip(frame, 1)

    # Proses deteksi tangan
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            wrist_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            hand_x, hand_y = map_hand_to_screen(wrist_landmark.x, wrist_landmark.y, screen_size)

            if is_ball_caught:
                ball_pos[0] = hand_x
                ball_pos[1] = hand_y

                if not is_fist(hand_landmarks):
                    is_ball_caught = False
                    ball_speed = [(hand_x - ball_pos[0]) * 0.2, -10]
                    ball_throw_time = time.time()

            distance = np.linalg.norm(np.array([hand_x, hand_y]) - np.array(ball_pos))
            if distance < ball_radius + 20 and is_fist(hand_landmarks):
                is_ball_caught = True

    if not is_ball_caught:
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]
        ball_speed[1] += gravity

        if ball_pos[1] >= screen_size[1] - ball_radius:
            ball_pos[1] = screen_size[1] - ball_radius
            ball_speed[1] *= -0.7
        if ball_pos[0] <= ball_radius or ball_pos[0] >= screen_size[0] - ball_radius:
            ball_speed[0] *= -1

    # Pastikan koordinat bola adalah integer saat menggambar
    cv2.circle(frame, (int(ball_pos[0]), int(ball_pos[1])), ball_radius, ball_color, -1)

    cv2.imshow('Hand Controlled Game with Action', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
