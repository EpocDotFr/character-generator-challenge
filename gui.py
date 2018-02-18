import pygame

elements = pygame.sprite.Group()


def draw(surface):
    """Draw all the GUI elements on the specified surface."""
    elements.draw(surface)


def add(element):
    """Add an element to the GUI elements list."""
    elements.add(element)


def event_handler(event):
    """Handles all the GUI-related events."""
    for element in elements:
        if element.event_handler(event):
            return True

    return False


class Button(pygame.sprite.Sprite):
    """A clickable area on the screen."""
    def __init__(self, image, rect, on_click):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = rect
        self.on_click = on_click

    def event_handler(self, event):
        if self.on_click is None or event.type != pygame.MOUSEBUTTONDOWN or not self.rect.collidepoint(event.pos):
            return False

        self.on_click()

        return True
