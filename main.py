import pygame
import os
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, LANES, ENEMY_MAX_SPEED, PLAYER_SPEED
from src.car import Car
from src.player_car import PlayerCar
from src.spawner import spawn_enemy_car

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("High Speed")
clock = pygame.time.Clock()


# Load background image
# Load tile
background = pygame.image.load("assets/images/background.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, 128))

# scroll effect
scroll_y = 0
SCROLL_SPEED = 4

# Load player
player = PlayerCar("/Users/matty/Documents/SEO TECH DEV/traffic-control-game/assets/images/player.png", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, speed=7)

# Initialize and play background music
pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/background.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# Load crash sound
crash_sound = pygame.mixer.Sound("assets/sounds/crash.mp3")

# Enemy cars list
enemy_cars = []

# Spawn event
SPAWN_CAR_EVENT = pygame.USEREVENT + 1
spawn_interval = 1200
pygame.time.set_timer(SPAWN_CAR_EVENT, spawn_interval)

# Score
score = 0
start_time = pygame.time.get_ticks()

running = True
while running:
    clock.tick(60)
    screen.blit(background, (0, 0))  # Draw background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == SPAWN_CAR_EVENT:
            enemy_cars.append(spawn_enemy_car())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.switch_lane("LEFT")
            elif event.key == pygame.K_RIGHT:
                player.switch_lane("RIGHT")


    #Tile scroll functionality
    scroll_y = (scroll_y + SCROLL_SPEED) % 128
    for y in range(-128, SCREEN_HEIGHT, 128):
        screen.blit(background, (0, y + scroll_y))


    # Update enemy cars
    for car in enemy_cars[:]:
        car.update()
        car.draw(screen)

        if car.off_screen(SCREEN_HEIGHT):
            enemy_cars.remove(car)
            score += 1
        elif car.rect.colliderect(player.rect):
            crash_sound.play()
            pygame.time.wait(1500)
            running = False  # Game over

    player.draw(screen)

    # Draw score
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()