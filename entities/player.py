import pygame
import assets

class Player:
    sprite_path = "assets/human_m.png"

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.speed = 3
        self.sprite = pygame.image.load(self.sprite_path).convert_alpha()

    def move(self, dx: int, dy: int):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    @classmethod
    def get_sprite_size(cls) -> tuple[int, int]:
        sprite = pygame.image.load(cls.sprite_path).convert_alpha()
        return sprite.get_width(), sprite.get_height()
    