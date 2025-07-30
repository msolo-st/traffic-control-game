import pygame

class MusicNote:
    def __init__(self, image_path, x, y, speed, song_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.song_path = song_path

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def off_screen(self, screen_height):
        return self.rect.top > screen_height
