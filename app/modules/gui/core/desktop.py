import pygame

class Desktop(object):
    width = property(lambda self: pygame.display.get_surface().get_width())
    height = property(lambda self: pygame.display.get_surface().get_height())
    size = property(lambda self: pygame.display.get_surface().get_size())
    client_size = property(lambda self: pygame.display.get_surface().get_size())

    def __init__(self) -> None:
        self.widgets = []

    def add(self, widget):
        widget.parent = self

        # if isinstance(widget, ):
        #     self.widgets.append(widget)
        self.widgets.append(widget)

    def draw(self):
        surf = pygame.display.get_surface()

        for widget in self.widgets:
            widget.draw(surf)

    def update(self):
        pass