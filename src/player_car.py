import pygame

class PlayerCar:
    def __init__(self, image_path, x, y, speed):
        self.image = pygame.image.load("assets/cars/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self, keys, screen_width):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:  # or use config.SCREEN_HEIGHT
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
