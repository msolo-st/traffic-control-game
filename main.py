import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.car import Car
from src.player_car import PlayerCar
from src.spawner import spawn_enemy_car

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffic Control")
clock = pygame.time.Clock()

# Load player image
player = PlayerCar("assets/cars/player.png", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, speed=7)

# Enemy cars list
enemy_cars = []

# Timer for spawning enemy cars
SPAWN_CAR_EVENT = pygame.USEREVENT + 1
spawn_interval = 1200  # milliseconds
pygame.time.set_timer(SPAWN_CAR_EVENT, spawn_interval)

# Score / difficulty
score = 0
start_time = pygame.time.get_ticks()

running = True
while running:
    clock.tick(FPS)
    screen.fill((50, 50, 50))  # Dark road background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_CAR_EVENT:
            enemy_cars.append(spawn_enemy_car())

    keys = pygame.key.get_pressed()
    player.update(keys, SCREEN_WIDTH)

    # Update and draw enemy cars
    for car in enemy_cars[:]:
        car.update()
        car.draw(screen)
        if car.off_screen(SCREEN_HEIGHT):
            enemy_cars.remove(car)
            score += 1
        if car.rect.colliderect(player.rect):
            running = False  # Game over

    player.draw(screen)

    # Score display
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
