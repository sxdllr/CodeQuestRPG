import pygame

from core import settings
from entities.player import Player
from core.visibility import Visibility

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

        self.fog = Visibility()

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
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1

        self.player.move(dx, dy)

    def render(self):
        self.screen.fill((128,128,128))

        sprite_w, sprite_h = Player.get_sprite_size()
        hero_pos = (int(self.player.x + sprite_w / 2), 
                    int(self.player.y + sprite_h / 2))
        
        self.fog.reveal(hero_pos, 100)

        self.fog.render(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()