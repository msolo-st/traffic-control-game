import pygame
print(pygame.__version__)
pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Traffic Control")
clock = pygame.time.Clock()