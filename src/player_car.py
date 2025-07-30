import pygame
from config import LANES

class PlayerCar:
    def __init__(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (35, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

        self.current_lane = min(range(len(LANES)), key=lambda i: abs(LANES[i] - x))
        self.rect.centerx = LANES[self.current_lane]

    def switch_lane(self, direction):
        if direction == "LEFT" and self.current_lane > 0:
            self.current_lane -= 1
        elif direction == "RIGHT" and self.current_lane < len(LANES) - 1:
            self.current_lane += 1
        self.rect.centerx = LANES[self.current_lane]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

