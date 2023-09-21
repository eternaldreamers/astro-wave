import pygame
from .core.desktop import Desktop
from .core.container import Container

class GUIModule:
    def __init__(self) -> None:
        self.running = False
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.desktop = Desktop()

    def _initialize(self):
        self.running = True

        Container(parent=self.desktop, position=(0,0), size=(100, 100))
        # Container()


        pygame.init()

    def run(self):
        self._initialize()

        while self.running:
            pygame.display.set_caption('%d' % self.clock.get_fps())
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # if event.type == pygame.VIDEORESIZE:
                #     self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)

            self.screen.fill((250, 250, 255))
            # self.screen.blit(self.background, (0, 0))

            self.desktop.update()
            self.desktop.draw()

            pygame.display.update()

        pygame.quit()