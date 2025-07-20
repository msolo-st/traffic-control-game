import pygame
print(pygame.__version__)
pygame.init()

#Main Game Loop
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Traffic Control")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60) #60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Update game state
    #Draw everything
    pygame.display.flip()
    pygame.quit()