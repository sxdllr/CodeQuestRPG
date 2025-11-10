import pygame
from core import settings

class Visibility:
    def __init__(self):
        self.width = settings.SCREEN_WIDTH
        self.height = settings.SCREEN_HEIGHT
        self.color = (0,0,0,240)

        self.surface = pygame.Surface((self.width, self.height), 
                                      pygame.SRCALPHA).convert_alpha()
        self.surface.fill(self.color)

    def render(self, screen):
        screen.blit(self.surface, (0, 0))

    def reveal(self, player_pos: tuple[int, int], radius: int):
        self.surface.fill(self.color)

        for r in range(radius, 0, -1):
            alpha = int(self.color[3] * (r / radius))
            pygame.draw.circle(self.surface, (0, 0, 0, alpha), player_pos, r)

    def reset(self):
        self.surface.fill(self.color)