import pygame
import os
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, LANES, ENEMY_MAX_SPEED, PLAYER_SPEED
from src.car import Car
from src.player_car import PlayerCar
from src.spawner import spawn_enemy_car
from src.music_note import MusicNote

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

#Music Note Spawning
SPAWN_NOTE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_NOTE_EVENT, 7000)  # every 7 seconds
music_notes = []

# Score
score = 0
start_time = pygame.time.get_ticks()

running = True
current_spawn_interval = spawn_interval  # track what the timer is currently set to

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
        elif event.type == SPAWN_NOTE_EVENT:
            note_options = [
                ("assets/images/red.png",  "assets/sounds/rock.mp3"),
                ("assets/images/blue.png", "assets/sounds/calm.mp3"),
                ("assets/images/black.png", "assets/sounds/background.mp3"),
                ("assets/images/green.png", "assets/sounds/drake.mp3"),
                ("assets/images/purple.png", "assets/sounds/mellow.mp3"),
                ("assets/images/yellow.png", "assets/sounds/cool.mp3")
                    ]
            note_img, note_song = random.choice(note_options)
            lane_x = random.choice(LANES)
            music_notes.append(MusicNote(note_img, lane_x, -30, speed=4, song_path=note_song))



    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    difficulty_level = elapsed_time // 10

        # Adjust difficulty
    SCROLL_SPEED = min(4 + difficulty_level, 12)
    new_spawn_interval = max(1200 - difficulty_level * 100, 400)

    # ✅ Only update the timer if the interval has changed
    if new_spawn_interval != current_spawn_interval:
        current_spawn_interval = new_spawn_interval
        pygame.time.set_timer(SPAWN_CAR_EVENT, current_spawn_interval)


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
            game_over = True
            running = False  # Exit main loop
    
    for note in music_notes[:]:
        note.update()
        note.draw(screen)
        if note.off_screen(SCREEN_HEIGHT):
            music_notes.remove(note)
        elif note.rect.colliderect(player.rect):
            music_notes.remove(note)
            pygame.mixer.music.load(note.song_path)
            pygame.mixer.music.play(-1)






    player.draw(screen)

    # Draw score
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

# Show "You Lost" screen
font_big = pygame.font.SysFont(None, 72)
font_small = pygame.font.SysFont(None, 36)

text1 = font_big.render("You Lost!", True, (255, 0, 0))
text2 = font_small.render(f"Final Score: {score}", True, (255, 255, 255))
text3 = font_small.render("Closing in 3 seconds...", True, (200, 200, 200))

# Clear screen and show background again (optional)
screen.blit(background, (0, 0))

# Draw messages centered
screen.blit(text1, (SCREEN_WIDTH // 2 - text1.get_width() // 2, SCREEN_HEIGHT // 2 - 60))
screen.blit(text2, (SCREEN_WIDTH // 2 - text2.get_width() // 2, SCREEN_HEIGHT // 2))
screen.blit(text3, (SCREEN_WIDTH // 2 - text3.get_width() // 2, SCREEN_HEIGHT // 2 + 40))

pygame.display.flip()
pygame.time.wait(5000)

pygame.quit()