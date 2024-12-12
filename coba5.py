import pygame
import sys
import math

# Inisialisasi pygame
pygame.init()

# Ukuran layar
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Kelelawar Mengikuti Kursor')

# Warna
background_color = (255, 255, 255)

# Muat gambar kelelawar
bat_image = pygame.image.load('bat.jpg')
bat_rect = bat_image.get_rect()

# Posisi awal kelelawar
bat_x, bat_y = 100, 100
bat_speed = 100  # Kecepatan kelelawar

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mendapatkan posisi kursor
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Menghitung jarak dan sudut antara kelelawar dan kursor
    dx = mouse_x - bat_x
    dy = mouse_y - bat_y
    distance = math.sqrt(dx**2 + dy**2)

    # Menggerakkan kelelawar menuju kursor
    if distance > 1:
        bat_x += (dx / distance) * bat_speed
        bat_y += (dy / distance) * bat_speed

    # Memperbarui posisi rect kelelawar
    bat_rect.topleft = (bat_x, bat_y)

    # Menggambar latar belakang
    screen.fill(background_color)

    # Menggambar kelelawar
    screen.blit(bat_image, bat_rect)

    # Memperbarui tampilan
    pygame.display.flip()

    # Mengatur kecepatan frame
    pygame.time.delay(30)
