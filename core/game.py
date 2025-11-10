import pygame

from core import settings
from entities.player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.init_window()

        sprite_w, sprite_h = Player.get_sprite_size()
        center_x = settings.SCREEN_WIDTH / 2 - sprite_w / 2
        center_y = settings.SCREEN_HEIGHT / 2 - sprite_h / 2
        self.player = Player(center_x , center_y)

    def init_window(self):
        pygame.display.set_caption(settings.TITLE)
        #icon = pygame.image.load("assets/icon.png")
        #pygame.display.set_icon(icon)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(settings.FRAMERATE)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):
        self.screen.fill((128,128,128))
        self.player.draw(self.screen)
        pygame.display.flip()