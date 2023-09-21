import pygame
from pygame.locals import Rect
from .widget import Widget

class Container(Widget):
    # client_rect = property(lambda self: Rect(0, 0, (100, 100)))
    # client_size = property()

    def __init__(self, parent, position=(0, 0), size=(100, 100)) -> None:
        super().__init__(parent, position, size)

        self.widgets = []
        self.surf = None

        # self.refresh()

    # def refresh(self):
    #     return super().refresh()

    def draw(self, surf):
        surf.blit(self.surf, (0, 0))