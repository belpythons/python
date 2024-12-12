import pygame
import random
import math

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Judul dan Ikon
pygame.display.set_caption("Sederhana FPS")
icon = pygame.image.load('icon.JPEG')  # Masukkan gambar ikon jika ada
pygame.display.set_icon(icon)

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Pemain
playerImg = pygame.image.load('player.png')  # Masukkan gambar pemain
playerX = 370
playerY = 480
playerX_change = 0

# Musuh
enemyImg = pygame.image.load('enemy.png')  # Masukkan gambar musuh
enemyX = random.randint(0, SCREEN_WIDTH - 64)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

# Peluru
bulletImg = pygame.image.load('bullet.png')  # Masukkan gambar peluru
bulletX = 0
bulletY = 480
bulletY_change = 1
bullet_state = "ready"  # "ready" = tidak terlihat, "fire" = terlihat dan menembak

# Skor
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Fungsi menggambar pemain
def player(x, y):
    screen.blit(playerImg, (x, y))

# Fungsi menggambar musuh
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Fungsi menembak peluru
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Fungsi deteksi tabrakan antara peluru dan musuh
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

# Fungsi untuk menampilkan skor
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, WHITE)
    screen.blit(score, (x, y))

# Loop game
running = True
while running:
    # Latar belakang layar
    screen.fill(BLACK)

    # Menangani input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Deteksi jika tombol arah ditekan
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # Deteksi jika tombol arah dilepas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Gerakan pemain
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64

    # Gerakan musuh
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= SCREEN_WIDTH - 64:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Gerakan peluru
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Deteksi tabrakan
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX = random.randint(0, SCREEN_WIDTH - 64)
        enemyY = random.randint(50, 150)

    # Menampilkan pemain, musuh, dan skor
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)

    # Update layar
    pygame.display.update()
