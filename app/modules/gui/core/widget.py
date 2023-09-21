import pygame
from .exceptions import GuiCoreException
from .desktop import Desktop

class Widget(object):
    # REFRESH_ON_MOUSE_OVER = True
    # REFRESH_ON_MOUSE_DOWN = True
    # REFRESH_ON_MOUSE_CLICK = True
    # REFRESH_ON_MOUSE_LEAVE = True
    
    # GETS_FOCUS = False

    # dynamicAttributes = []

    def __init__(self, parent, position = (0,0), size = (100, 20)) -> None:
        self.parent = parent
        self.position = position
        self.size = size

        if isinstance(self.parent, Desktop):
            self.desktop = self.parent
        else:
            self.desktop = self.parent.desktop

        if self.parent:
            self.parent.add(self)

    # def __init__(self, parent, style = None, position = 0, size = (100,20), visible = True, enabled = True, anchor = ANCHOR_TOP | ANCHOR_LEFT):
    #     if parent == None:
    #         raise GuiCoreException("Widget must have a parent.")
        
    #     self.mouseover = False
    #     self.mousedown = False
    #     self.spacedown = False
    #     self.mouseclick = False

    #     self.onClick = []
    #     self.onMouseOver = []
    #     self.onMouseLeave = []
    #     self.onMouseDown = []
    #     self.onGotFocus = []
    #     self.onLostFocus = []
        
    #     self.parent = parent
    #     self.anchor = anchor
    #     self.position = (0,0)

    #     if isinstance(position, int) and self.parent:
    #         self.position = self.parent.nextVertPos(position)
    #     else:
    #         self.position = position
            
    #     if isinstance(self.parent, Desktop):
    #         self.desktop = self.parent
    #     else:
    #         self.desktop = self.parent.desktop
        
    #     self.size = size
    #     self.visible = visible
    #     self.enabled = enabled
    #     self.style = style
        
    #     self.dynamicAttributes = ['style', 'size', 'enabled']
        
    #     self.needsRefresh = False
        
    #     if self.parent:
    #         self.parent.add(self)

    # def __setattr__(self, attribute, value):
    #     if attribute in self.dynamicAttributes:
    #         self.needsRefresh = True
        
    #     object.__setattr__(self, attribute, value)

    def refresh(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass