import pygame
import random
import math

# Inisialisasi pygame
pygame.init()

# Ukuran layar
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Simple FPS Game")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Pemain
player_pos = [400, 300]
player_angle = 0
player_speed = 10

# Peluru
bullets = []

# Musuh
enemies = [[random.randint(0, 800), random.randint(0, 600)] for _ in range(5)]

# Fungsi menggambar pemain
def draw_player(screen, pos, angle):
    pygame.draw.circle(screen, WHITE, pos, 20)
    end_pos = (pos[0] + 20 * math.cos(angle), pos[1] + 20 * math.sin(angle))
    pygame.draw.line(screen, WHITE, pos, end_pos, 2)

# Fungsi menggambar peluru
def draw_bullets(screen, bullets):
    for bullet in bullets:
        pygame.draw.circle(screen, RED, (int(bullet[0]), int(bullet[1])), 5)

# Fungsi menggambar musuh
def draw_enemies(screen, enemies):
    for enemy in enemies:
        pygame.draw.circle(screen, RED, enemy, 20)

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullets.append([player_pos[0], player_pos[1], player_angle])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos[0] += player_speed * math.cos(player_angle)
        player_pos[1] += player_speed * math.sin(player_angle)
    if keys[pygame.K_s]:
        player_pos[0] -= player_speed * math.cos(player_angle)
        player_pos[1] -= player_speed * math.sin(player_angle)
    if keys[pygame.K_a]:
        player_angle -= 0.1
    if keys[pygame.K_d]:
        player_angle += 0.1

    # Update peluru
    for bullet in bullets:
        bullet[0] += 10 * math.cos(bullet[2])
        bullet[1] += 10 * math.sin(bullet[2])

    # Menghapus peluru yang keluar dari layar
    bullets = [bullet for bullet in bullets if 0 < bullet[0] < 800 and 0 < bullet[1] < 600]

    # Menggambar semua objek
    screen.fill(BLACK)
    draw_player(screen, player_pos, player_angle)
    draw_bullets(screen, bullets)
    draw_enemies(screen, enemies)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
