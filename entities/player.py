import pygame
import assets

class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.speed = 3
        
        self.sprite = pygame.image.load('assets/human_m.png').convert_alpha()

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))