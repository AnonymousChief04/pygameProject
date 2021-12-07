import pygame
import os
pygame.init()


WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starcraft")

FPS = 60

def main():
    clock = pygame.time()

    run = True
    while run:
        clock.tick(FPS)
        testing
