import pygame

from core import settings

class Game:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.init_window()

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
        pass